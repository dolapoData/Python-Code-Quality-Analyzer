# Python-Code-Quality-Analyzer

## Problem Statement
Development teams often lack the time to manually review every script for readability, maintainability, and structural issues. This project builds an educational prototype that automatically analyzes Python source files and reports measurable quality indicators.

## Business Context
As software teams grow, manual code review becomes slow and expensive. Static analysis tools like SonarQube solve this at scale, this project demonstrates the same underlying concept using only Python's built-in tools (no external libraries).

## Objectives
- Read a Python file and extract measurable characteristics
- Detect common code-quality issues (long lines, unclear names, duplication, excessive nesting, missing documentation)
- Calculate a weighted quality score and severity rating
- Generate actionable recommendations

## Features
- Interactive file analysis via user input
- Line/blank/comment/code line counts
- Long line detection
- Unclear variable name detection
- Duplicate line detection
- Function count and function-length analysis
- Maximum nesting depth detection
- Missing docstring detection
- Basic risky pattern detection (`eval`, `exec`)
- Weighted quality score (0–100) with severity rating
- Auto-generated recommendations
- Folder-level comparison across multiple files (simplified scoring - see limitations)
- Error handling for missing/invalid files

## Methodology
The analyzer reads a `.py` file line by line and applies rule-based checks (no AST parsing) to flag issues. Each category is weighted (e.g. naming 15%, nesting 20%, duplication 15%) and subtracted from a starting score of 100 to produce a final quality score and rating (Excellent/Good/Fair/Needs Improvement/Poor).

## Technologies
- Python 3 (standard library only — no external packages)
- Jupyter Notebook

## Limitations
- This is an educational prototype, not a substitute for professional static-analysis, security, or code-review tools.
- Naming and duplication checks are simplified (string-based, not AST-based) and may produce false positives/negatives.
- The folder-level comparison (`analyze_folder`) uses a simplified subset of checks for the summary table; the single-file report (`analyze_file`) is the authoritative, complete analysis.
- Risky pattern detection only flags `eval()`/`exec()` and does not confirm actual vulnerabilities and therefore manual review is still required.

## Results
Sample files (`good_code.py`, `average_code.py`, `poor_code.py`) were created at three intentional quality levels to validate the analyzer. Results confirmed the tool correctly distinguishes quality tiers based on naming, duplication, nesting, and documentation.

## Future Improvements
- Use Python's `ast` module for more accurate structural analysis
- Align folder-level scoring with the full single-file scoring logic
- Save reports to `.txt` files automatically
- Expand risky-pattern detection
