# Lab 05 changes vs the original handout notebook (2026-09-20)

Original handout: Module_05_Lab_Data_Preparation.ipynb as downloaded. No pristine copy
was kept: the only backup (session scratchpad nb_backup.ipynb) was taken after the
cell 5/8/11 edits, before newline normalization. Original cell contents = the
commented placeholders shown in the handout.

```text
Cell 2   unchanged
Cell 5   Task 1  filled in
         ├── DEVIATION: df['Age'] = df['Age'].fillna(m)   (handout: fillna(..., inplace=True))
         │   verified 2026-09-20: handout line leaves 177 NaN on pandas 3.0.6. See ADR 0001.
         └── ADDED: assert Age NaN == 0, print of median
Cell 8   Task 2  filled in
         ├── fill 2 Embarked NaN with mode before get_dummies. In scope: handout Part 2 names mode for categorical
         │   missing values and says the dataset has missing values; Task 2 just doesn't spell out this step. See ADR 0002.
         │   approved by Joseph 2026-09-20
         └── ADDED: asserts (no NaN, Sex/Embarked dropped, Sex_male/Embarked_Q/Embarked_S exist)
Cell 11  Task 3  filled in per handout
         └── ADDED: asserts (no NaN, mean ~0, std ~1)
Cell 12  Knowledge Check answered (2026-09-20); answers added under an '### Answers' heading, question text unchanged
All      source lines now end with \n (file formatting only; no visible change)
Text     no handout instruction text edited (only cell 12 answers appended)
specs/   not edited
```

Everything else logged with dates in progress.md. Journals should mention the two
deviations (inplace, Embarked) as findings.
