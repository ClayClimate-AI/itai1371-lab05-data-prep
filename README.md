# ITAI 1371 Lab 05: Data Preparation

Module 05 lab for ITAI 1371. The notebook prepares the Titanic passenger data for machine
learning: it fills missing values, encodes categorical columns, and scales numeric columns.

- Author: Joseph Clay (independent contributor)
- Notebook: `Module_05_Lab_Data_Preparation.ipynb`
- Dataset: Titanic (891 rows x 12 columns), loaded by URL inside the notebook. Nothing to download.
- Python 3.14 / pandas 3.0 tested. `requirements.txt` allows pandas 2.0 or newer.

## Assignment requirements and where they are met

| Requirement (Canvas / `specs/lab05_acceptance.md`) | Where it is met |
| --- | --- |
| Complete the Module 05 Lab notebook | Tasks 1-3 and the Knowledge Check are filled in (below) |
| PDF 1: executed notebook | `L05_JosephClay_ITAI1371.pdf` |
| PDF 2: reflective journal | `L05Journal_R_JosephClay_ITAI1371.pdf` |
| PDF 3: contribution journal | `L05Journal_C_JosephClay_ITAI1371.pdf` |
| Rubric: Project 70 (working 50 + documentation 20), Reflection 10, Contribution 20 | Notebook + this README + `docs/`; the two journals |
| Due date | Sep 20 (module page). The assignment page shows Sep 30, 11:59 PM CT. Sep 20 was treated as the deadline. |

Canvas templates may print group tokens (JSM1371). This was an individual submission, so the
PDFs use personal ITAI1371 names.

## What the notebook does

| Step | Cell | What happens | Check in the cell |
| --- | --- | --- | --- |
| Setup | 2 | Load the data and count missing values (Age 177, Cabin 687, Embarked 2) | Printed counts |
| Task 1 | 5 | Fill `Age` with the median | Assert: 0 missing in `Age` |
| Task 2 | 8 | Fill `Embarked` with its mode, then one-hot encode `Sex` and `Embarked` (`drop_first=True`) | Asserts: no missing values, original columns removed, `Sex_male`, `Embarked_Q`, `Embarked_S` present |
| Task 3 | 11 | Standardize `Age` and `Fare` with `StandardScaler` | Asserts: no missing values, mean ~0, std ~1 |
| Knowledge Check | 12 | Written answers: median vs mean, one-hot encoding, scaling and decision trees | n/a |

## Differences from the handout

Full list in `docs/CHANGES_vs_handout.md`. In short:

1. **Age fill uses explicit assignment.** The handout's `df['Age'].fillna(median, inplace=True)`
   left all 177 missing values in place on pandas 3.0.6 (it changes a temporary copy).
   The notebook uses `df['Age'] = df['Age'].fillna(median_age)` and asserts the result.
2. **Embarked is filled before encoding.** Two missing `Embarked` values would otherwise encode as
   all zeros and look like the dropped category. This follows the handout's guidance to use the mode for
   categorical columns.
3. **Assert statements added** to each task cell so silent failures stop the run.

No handout instruction text was changed. Cell 12 has the answers added below the questions.

## Repository layout

```text
itai1371-lab05-data-prep
├── Module_05_Lab_Data_Preparation.ipynb
├── L05_JosephClay_ITAI1371.pdf              executed notebook
├── L05Journal_R_JosephClay_ITAI1371.pdf     reflective journal
├── L05Journal_C_JosephClay_ITAI1371.pdf     contribution journal
├── README.md
├── requirements.txt
├── scripts/setup_gate.py                    environment check
├── specs/lab05_acceptance.md                acceptance criteria from Canvas
├── tests/test_imports.py                    import smoke test
└── docs/CHANGES_vs_handout.md               deviations from the handout
```

## Reproduce

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/setup_gate.py        # expect: OK Lab 05 environment gate passed
python -m pytest tests -q           # expect: 1 passed
jupyter notebook Module_05_Lab_Data_Preparation.ipynb
```

In Jupyter, use Kernel > Restart & Run All. Cells should number 1-4 in order with no failed asserts.
The PDF was exported from a fresh run.

## Scope

This is a shorter lab than most in the course: three coding tasks and a knowledge check, with
four code cells in total. It covers data preparation only, so the documentation is sized to match.
Modeling and full exploratory analysis belong to other assignments and are not part of this repository.
