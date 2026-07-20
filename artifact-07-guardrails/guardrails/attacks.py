"""Attack taxonomy + corpus loader for the injection slice.

Each case is either an attack (``is_benign=False``, tagged with an attack type)
or a benign control (``is_benign=True``, ``attack_type="benign"``). Benign
controls are load-bearing: without them you cannot tell a real defense from a
guard that simply blocks everything.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

# The attack families the corpus is tagged against (spec §4 Artifact #4).
ATTACK_TYPES = (
    "prompt_injection",       # override the standing instructions
    "instruction_smuggling",  # fake role turns / control tokens in content
    "system_prompt_exfil",    # make it reveal its hidden instructions
    "data_exfil",             # move a secret out of band
    "off_policy",             # requests it should refuse outright
)


@dataclass(frozen=True)
class Case:
    id: str
    attack_type: str
    is_benign: bool
    text: str


def load_cases(path: str | Path) -> list[Case]:
    raw = json.loads(Path(path).read_text())
    return [
        Case(
            id=c["id"],
            attack_type=c["attack_type"],
            is_benign=bool(c["is_benign"]),
            text=c["text"],
        )
        for c in raw
    ]
