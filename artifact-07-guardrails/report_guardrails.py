"""Worked example: run the injection corpus through the guard, baseline vs
defended, and print the before/after the artifact's RESULTS.md is built from.

    python report_guardrails.py

Fully offline and deterministic — no model, no key.
"""
from pathlib import Path

from guardrails.attacks import load_cases, ATTACK_TYPES
from guardrails.harness import evaluate

CORPUS = Path(__file__).resolve().parent / "data" / "injection_cases.json"


def _pct(x: float) -> str:
    return f"{x * 100:.0f}%"


def main() -> None:
    cases = load_cases(CORPUS)
    base = evaluate(cases, defended=False)
    deft = evaluate(cases, defended=True)

    print(f"Corpus: {base['n_attacks']} attacks + {base['n_benign']} benign controls\n")

    print("Headline (lower attack-success is better; higher benign-pass is better)")
    print(f"  {'':22} {'baseline':>10} {'defended':>10}")
    print(f"  {'attack success rate':22} {_pct(base['attack_success_rate']):>10} {_pct(deft['attack_success_rate']):>10}")
    print(f"  {'benign pass rate':22} {_pct(base['benign_pass_rate']):>10} {_pct(deft['benign_pass_rate']):>10}\n")

    print("Attack success by type (defended)")
    for t in ATTACK_TYPES:
        b = base["attack_success_by_type"].get(t, {"n": 0, "succeeded": 0})
        d = deft["attack_success_by_type"].get(t, {"n": 0, "succeeded": 0})
        print(f"  {t:22} baseline {b['succeeded']}/{b['n']}   defended {d['succeeded']}/{d['n']}")

    print("\nWhat the defense still does not stop (residual, defended):")
    for rec in deft["records"]:
        if not rec["is_benign"] and rec["attack_succeeded"]:
            print(f"  {rec['id']:6} [{rec['attack_type']}] evaded the signatures")

    print("\nBenign over-blocking (the cost of the defense):")
    for rec in deft["records"]:
        if rec["is_benign"] and rec.get("over_blocked"):
            print(f"  {rec['id']:6} benign request blocked as a false positive")


if __name__ == "__main__":
    main()
