# ITAI 1371 Lab 05 — Data Preparation

Scaffold reused from the Module 3 Zero-Defect layout (process, folders, journals). Notebook is Module 05 Data Preparation, not Wine and not Titanic EDA.

## Goal

Complete `Module_05_Lab_Data_Preparation.ipynb`. Run cells in order. Export three PDFs for Canvas.

Due dates on Canvas (not reconciled yet):
- Module / Grades page: Sep 20
- Assignment page: Sep 30 at 11:59 PM CT

Confirm which lock you are using before submit.

## Deliverables (Canvas)

| # | Deliverable | Suggested name |
| --- | --- | --- |
| 1 | Executed notebook PDF | `L05_JosephClay_ITAI1371.pdf` |
| 2 | Reflective journal (1–2 pages) | `L05Journal_R_JosephClay_ITAI1371.pdf` |
| 3 | Contribution journal (1–2 pages) | `L05Journal_C_JosephClay_ITAI1371.pdf` |

Canvas templates may still say group names / JSM1371. You are an independent contributor; personal ITAI1371 naming is the default unless Rao says otherwise.

## Layout

```text
ITAI_1371_Lab05_Data_Prep
├── Module_05_Lab_Data_Preparation.ipynb
├── README.md
├── requirements.txt
├── checkpoints.md
├── progress.md
├── reflections.md
├── HOW_TO_OPEN_IN_CURSOR.md
├── assets/
├── docs/
├── scripts/setup_gate.py
├── specs/
└── tests/
```

Course materials also live in HCC docs on my computer: slides + feature engineering PDFs under `hcc_docs/assignments/lab05/`.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/setup_gate.py
jupyter notebook Module_05_Lab_Data_Preparation.ipynb
```

Kernel → Restart & Run All before PDF export.

## Midterm link

Mid Term EDA (due Oct 3) builds on Lab 04 and Lab 05. Dataset approval window starts around Sep 20.

## Prework

Learner overview and slides: see `PREWORK.md`.
