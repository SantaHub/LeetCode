# LeetCode

Personal practice solutions. Each problem lives in its own directory:

```
<id>-<slug>/
  PROBLEM.md
  solution.py
  test_solution.py
  requirements.txt
```

## Problems

| # | Title | Status |
|---|--------|--------|
| 588 | Design In-Memory File System | Complete |
| 981 | Time Based Key-Value Store | Complete |
| 1396 | Design Underground System | Complete |

Incomplete work stays local until solutions pass tests.

## Run tests

```bash
cd <problem-dir>
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```
