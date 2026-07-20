"""The defensive layer under test.

Two modes, so the artifact can report a real before/after:

- ``defended=False`` (baseline): a naive guard that only catches the single most
  blatant literal injection ("ignore all previous instructions", verbatim). Every
  other attack family sails through. This is what "we added a guardrail" looks
  like when the guardrail is a vibe.
- ``defended=True``: a signature set covering the attack families in the corpus.
  It catches far more — and, honestly, occasionally trips on benign text that
  shares surface tokens. That false-positive cost is not hidden; it is measured
  (benign-pass-rate) alongside the attack-success-rate.

Deterministic and offline: the "guard" is pattern matching over the incoming
text, not a model call. The point of the artifact is the *measurement* of a
defense, not the sophistication of the defense.
"""
from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Decision:
    blocked: bool
    reason: str  # the signature name that fired, or "" if allowed


# The one thing even the naive baseline blocks: the canonical blatant phrase.
_BASELINE = [
    ("blatant_ignore", re.compile(r"\bignore all previous instructions\b", re.I)),
]

# Defended signatures, grouped by the attack family each is meant to catch.
# Ordered; the first match wins and names the reason.
_DEFENDED = [
    # Prompt injection: override / disregard the standing instructions.
    ("prompt_injection",
     re.compile(r"\b(ignore|disregard|forget)\b.{0,40}\b(previous|prior|above|earlier|all)\b", re.I)),
    # Instruction smuggling: fake role turns / chat control tokens embedded in content.
    ("instruction_smuggling",
     re.compile(r"(^|\n)\s*(system|assistant|developer)\s*:", re.I)),
    ("instruction_smuggling",
     re.compile(r"(\[/?INST\]|<\|[^|]+\|>|###\s*(system|instruction))", re.I)),
    # System-prompt exfiltration: reveal the hidden instructions.
    ("system_prompt_exfil",
     re.compile(r"\b(reveal|show|print|repeat|display)\b.{0,30}\b(system prompt|your (prompt|instructions)|hidden (prompt|instructions))\b", re.I)),
    # Data exfiltration: move a secret out of band.
    ("data_exfil",
     re.compile(r"\b(send|email|post|upload|exfiltrate|leak|forward)\b.{0,40}\b(api[ _-]?keys?|passwords?|secrets?|credentials?|tokens?|system prompt|conversation)\b", re.I)),
    # Off-policy: requests the assistant should refuse outright.
    ("off_policy",
     re.compile(r"\b(how to|help me|instructions to|steps to)\b.{0,40}\b(bomb|malware|ransomware|phishing|launder money|hack into)\b", re.I)),
]


def inspect(text: str, *, defended: bool) -> Decision:
    """Return a block/allow Decision for one piece of incoming text."""
    signatures = _DEFENDED if defended else _BASELINE
    for name, pattern in signatures:
        if pattern.search(text):
            return Decision(blocked=True, reason=name)
    return Decision(blocked=False, reason="")
