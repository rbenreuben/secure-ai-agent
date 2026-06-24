"""Eval harness: runs each test case and scores correctness + safety.
Run: python -m evals.run_evals
"""
import json, pathlib
from src.security.guardrails import check_input
from src.agent import run
from src.security.identity import Principal

CASES = pathlib.Path(__file__).parent / "test_cases.jsonl"

def evaluate():
    me = Principal(user_id="eval", roles=["user"])
    passed = 0; total = 0
    for line in CASES.read_text().splitlines():
        if not line.strip():
            continue
        case = json.loads(line); total += 1
        if case.get("expect_blocked"):
            allowed, _ = check_input(case["input"])
            ok = (allowed is False)            # safety: input should be blocked
        else:
            out = run(case["input"], me)
            ok = case.get("expect_contains", "").lower() in out.lower()
        print(f"[{'PASS' if ok else 'FAIL'}] {case['id']} ({case['type']})")
        passed += int(ok)
    print(f"\nScore: {passed}/{total} = {passed/total:.0%}")

if __name__ == "__main__":
    evaluate()
