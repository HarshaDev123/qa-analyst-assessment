# QA Analyst Assessment — SS&C Technologies

**Candidate:** Harsha
**Position:** Software Development Engineer in Test (SDET)
**Language:** Python 3
**Date:** March 2026

## Repository Structure

qa-analyst-assessment/
├── part1-functional/
│   ├── remove_duplicates.py    # Pure function to remove duplicates
│   └── README.md               # Approach & run instructions
└── part2-api-testing/
    ├── test_api.py             # Automated API tests (pytest)
    ├── requirements.txt        # Python dependencies
    └── README.md               # Test details & run instructions

## Quick Start

**Part 1 — Functional Programming**
```bash
python part1-functional/remove_duplicates.py
```

**Part 2 — API Testing**
```bash
pip install -r part2-api-testing/requirements.txt
pytest part2-api-testing/test_api.py -v
```
## Highlights

- **Part 1:** Demonstrates pure functions, immutability, and higher-order functions (filter) with 7 test cases including edge cases.
- **Part 2:** Uses pytest and requests to validate GET/POST endpoints and error handling against the JSONPlaceholder API, with clear test organization and meaningful assertions.
