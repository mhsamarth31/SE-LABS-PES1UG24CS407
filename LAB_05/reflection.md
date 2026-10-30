# Lab 5 Reflection — Static Code Analysis

## 1. What is static code analysis, and how is it different from testing?

Static code analysis examines source code without executing the program. It can identify suspicious code patterns, potential bugs, security weaknesses, and style violations early in development. Testing executes the program with selected inputs and checks its runtime behaviour. The two techniques complement each other: static analysis can flag risky constructs that a test suite may not exercise, while tests help confirm that the program behaves as intended.

## 2. What kinds of issues did Pylint, Bandit, and Flake8 help identify?

Pylint focuses on code quality and likely programming mistakes, such as mutable default arguments, broad exception handling, unused variables, and naming problems. Bandit focuses on common security weaknesses, such as dynamic evaluation, weak cryptographic hashes, hard-coded secrets, and unsafe shell execution. Flake8 checks Python syntax/style conventions, including whitespace, blank lines, line length, and other PEP 8 violations.

## 3. Which issue was most important to fix, and why?

The dynamic `eval()` call was among the most important findings because it could execute arbitrary Python code from the supplied expression. If that expression were influenced by a user or another untrusted source, an attacker could potentially execute unintended operations. Replacing it with a numeric multiplier and explicit validation preserves seasonal pricing without evaluating arbitrary code.

## 4. How does static analysis improve software quality and maintainability?

Static analysis provides fast, repeatable feedback before code is deployed. It helps developers discover security risks, reduce defects, keep style consistent, and make code easier for teammates to review. Running the tools regularly also helps prevent regressions as the project changes. Static analysis is not a substitute for tests or human review, but it is a useful additional quality gate.
