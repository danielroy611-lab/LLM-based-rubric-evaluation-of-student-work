import json
from app import EvalRequest, evaluate

with open("test_cases.json") as f:
    cases = json.load(f)

passed = 0
for i, case in enumerate(cases, 1):
    req = EvalRequest(submission=case["submission"], criteria=case["criteria"])
    result = evaluate(req)
    total = sum(c.score for c in result.criteria)
    ok = case["min_total"] <= total <= case["max_total"]
    passed += ok
    print(f"Case {i}: total={total}, expected {case['min_total']}-{case['max_total']} -> {'PASS' if ok else 'FAIL'}")

print(f"\nPassed {passed}/{len(cases)}")