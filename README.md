# Intent2Policy

Convert intent JSON into firewall/ACL rules and detect simple conflicts.

## Why
Shows intent to policy translation and basic rule verification: an essential step for policy-based management compatibility in intent-based security.

## Features
- Deterministic rule generation (templates)
- Conflict detection and warnings (overlapping rules, contradictory actions)
- Streamlit preview and downloadable policy snippet
- Unit tests for conversion logic

## Quick Start
1. Clone:
   ```
   git clone https://github.com/zain-ramzan/intent2policy.git
   ```
2. Create venv and install:
   ```
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Run:
   ```
   streamlit run app.py
   ```
4. Paste an intent JSON or upload file, press Generate

## Policy format
- Output is a simple ACL-like text:
  `deny tcp from vlan_finance to any port 22`

## Evaluation
- Correctness against manual mapping
- Conflict detection precision
- Human readability score

## Files
- `app.py` - UI
- `convert.py` - intent→policy logic
- `tests/` - unit tests
- `requirements.txt`
