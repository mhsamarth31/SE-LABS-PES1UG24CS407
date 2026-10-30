# Static Code Analysis Findings — Hotel Booking System

The line numbers below refer to the original `hotel_booking_system.py` from the assigned repository (before fixes). Findings are grouped with security risks first. Tool versions and exact messages should be copied from the local before-fix report files generated during the lab; static-analysis wording can vary by tool version.

| Issue | Type | Original line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Dynamic `eval()` | Security (Bandit B307; high confidence) | 37 | `eval(rate_expr)` executes an arbitrary Python expression, so untrusted input could execute code. | Removed expression evaluation. Seasonal pricing now accepts a numeric multiplier and validates its type and range. |
| MD5 digest | Security (Bandit B324) | 42 | MD5 is a weak cryptographic hash and should not be used where collision resistance is expected. | Replaced MD5 with SHA-256. The digest is explicitly documented as pseudonymous identification, not password storage. |
| Hard-coded secret | Security (Bandit B105) | 57 | An administrative token is embedded directly in source code and printed at runtime. | Removed the hard-coded token and its print statement. Secrets should be supplied through a protected environment/secret manager if later required. |
| Shell command construction | Security (Bandit B602 / B605, depending on analyzer version) | 52–54 | `os.system()` invokes a shell using a string containing a filename, creating command-injection risk. | Removed the shell invocation and used `pathlib.Path.write_text()` to write the ledger. |
| Mutable default argument | Bug / maintainability (Pylint W0102) | 15 | `booking_log=[]` is created once and shared between calls, so entries can leak across separate bookings. | Changed the default to `None` and creates a fresh list within the function. |
| Bare exception handler | Reliability (Pylint W0702) | 24–27 | A bare `except` catches every exception and silently hides programming and runtime errors. | Removed exception swallowing; dictionary lookup now handles an unknown room explicitly and returns `False`. |
| Unused local variable | Code quality (Pylint W0612) | 31 | `cleaning_deposit` is assigned but never used. | Removed the unused variable. |
| Equality comparison to `None` | Style / correctness (Pylint C0121) | 32 | `== None` is less reliable and less idiomatic than identity comparison. | Replaced the old check with `room is None`. |
| Unused imports | Code quality (Pylint W0611) | 4–7 | `math` was imported but unused; the original script also had unnecessary imports after changes. | Removed unused imports from the final file. |
| Naming and formatting | Style (Flake8 / Pylint) | 15,  | `bookRoom` does not follow `snake_case`; extra blank lines and old `%` formatting reduce consistency. | Renamed the function to `book_room`, used f-strings, and applied PEP 8 formatting. |

## Verification note

Run all three tools on the original file before editing and save the outputs as `*_before.txt`. Run them again on the cleaned file and save the outputs as `*_after.txt`. Keep the genuine tool output; do not manually invent or alter analyzer reports.
