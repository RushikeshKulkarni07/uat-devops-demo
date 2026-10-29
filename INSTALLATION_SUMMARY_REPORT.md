# UAT Environment Dry Run - Installation Summary Report

**Prepared by:** DevOps Engineer  |  **Environment:** UAT  |  **Date:** ____/____/______

> Fill the Status column after running each step on YOUR machine
> (Successful / Failed). Paste the verification output as evidence.

| # | Tool / Task               | Version (command)                 | Installation Status    | Evidence / Remarks              |
|---|---------------------------|-----------------------------------|------------------------|---------------------------------|
| 1 | Python                    | `python3 --version`               | Successful / Failed    |                                 |
| 2 | Git                       | `git --version`                   | Successful / Failed    |                                 |
| 3 | VS Code                   | `code --version`                  | Successful / Failed    |                                 |
| 4 | GitHub repo push          | `git log --oneline`               | Successful / Failed    | Repo URL:                       |
| 5 | Java (Jenkins prereq)     | `java -version`                   | Successful / Failed    |                                 |
| 6 | Jenkins                   | `systemctl status jenkins`        | Successful / Failed    | http://localhost:8080           |
| 7 | Jenkins pulls GitHub code | Console Output of build           | Successful / Failed    |                                 |
| 8 | pytest                    | `pytest --version`                | Successful / Failed    | 1 test passed?                  |
| 9 | Evidently                 | `pip show evidently`              | Successful / Failed    | reports/evidently_report.html   |

## Dry-run result (code verified in a clean Linux sandbox)
| Item                         | Result                      |
|------------------------------|-----------------------------|
| hello.py execution           | Successful - prints `Hello, World!` |
| pytest (1 test case)         | Successful - 1 passed       |
| Evidently drift report       | Successful - HTML generated |

## Overall status: PASS / FAIL  (circle one)
Sign-off: ______________________
