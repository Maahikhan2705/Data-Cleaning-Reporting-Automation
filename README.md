# Data Cleaning & Reporting Automation

Automate data cleaning and reporting workflows for historical concert tour datasets. This project processes raw, inconsistent tour data (containing special formatting symbols, footnote tags, and region-specific encoding) to generate structured datasets and automated summary insights.

## Key Features

* **Multi-Tool Automation:** Built using Python (Pandas) with workflow designs adaptable for Excel or Power BI pipelines.
* **Robust Data Cleaning:** Handles missing values, removes structural duplicates, and normalizes inconsistent string/numeric fields.
* **Automated Reporting:** Generates visual summaries and structural breakdowns of top-performing assets.

---

## Dataset & Technical Challenges Solved

The automation pipeline directly targets several common real-world data anomalies present in the source dataset:

1. **Invisible Character Normalization:** Detects and replaces hidden web artifacts like non-breaking spaces (`\xa0`) in column headers with standard spaces to avoid standard dictionary `KeyError` exceptions.
2. **Unicode Character Compatibility:** Automatically maps special character variants (such as `é` to `e` and en-dashes `–` to standard hyphens `-`) ensuring text strings render seamlessly across various OS shells and terminal environments.
3. **Numeric Disinfection:** Strips extraneous symbols (e.g., `$`, commas) and trailing citation elements (e.g., `[b]`, `[a]`) to convert textual currency fields into clean numeric forms (`float64`/`int64`) for computational analysis.
4. **Noise Symbol Stripping:** Leverages Regular Expressions to drop editorial status indicator markers like `†` or `‡` from category strings.

---

## Getting Started

### Prerequisites
Make sure you have Python 3.10+ and the `pandas` library installed:
```bash
pip install pandas
