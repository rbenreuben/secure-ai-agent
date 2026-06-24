# Secure AI Agent

A production-minded AI agent built on the Anthropic Claude API + MCP, with the two things most demo agents skip: **a security layer** and an **evaluation suite**. Built to demonstrate end-to-end secure AI deployment — identity, guardrails, tool-call observability, and measurable quality/safety.

> Personal portfolio project. Uses only synthetic data and my own accounts — no employer data or code.

## Why this exists
Most agent demos are toys: no auth, no input/output filtering, no way to measure whether the agent is actually good or safe. Real deployments need all three. This project shows the full loop:

- **Identity & least privilege** — the agent runs under a scoped identity; tools are allow-listed.
- **Guardrails** — input/output filtering (prompt-injection checks, secret/PII redaction).
- **Observability** — every tool call is logged with inputs, outputs, and timing.
- **Evaluation** — an eval harness scores the agent on a test set for correctness AND safety (e.g., resisting prompt-injection / system-prompt leakage).

## Architecture
```
User ── input guardrail ──> Agent (Claude + tools) ── tool-call log ──> Tools (allow-listed)
                                  │
                          output guardrail ──> User
                                  │
                            Eval harness  (scores correctness + safety on a test set)
```

## Project layout
```
src/
  agent.py            # Claude agent loop with tool use + security hooks
  security/
    guardrails.py     # input/output filtering, redaction, injection checks
    identity.py       # scoped-credential / least-privilege stub
  tools/
    example_tool.py   # sample allow-listed tool
evals/
  run_evals.py        # runs the agent over test cases, scores pass-rate + safety
  test_cases.jsonl    # eval cases (correctness + adversarial/safety)
```

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # add your ANTHROPIC_API_KEY
python -m src.agent         # run the agent
python -m evals.run_evals   # run the eval suite
```

## Eval results
| Metric | Score |
|---|---|
| Correctness (test set) | _TODO after first run_ |
| Prompt-injection resistance | _TODO_ |
| System-prompt leakage blocked | _TODO_ |

## Roadmap
- [ ] Wire a real MCP server as a tool source
- [ ] Add OIDC/Okta login in front of the agent
- [ ] Expand the eval set to 30+ cases; track regressions
- [ ] Add a kill-switch + rate limiting
