# Knowledge Check DRAFT (edit into your own words, then paste into notebook cell 12)

1. **Median vs mean for imputing?**
The mean gets pulled toward extreme values, so a few very old passengers would drag
the fill value up. The median is the middle value and barely moves with outliers, so it
is a safer "typical" value for skewed columns like Age (and Fare).

2. **What One-Hot Encoding does and why it is needed**
It turns a text category into 0/1 columns, one per category (e.g. Sex -> Sex_male).
Models do math on numbers, so they cannot use text like "male" directly. One-hot avoids
inventing an order (a plain 1, 2, 3 would imply Q > C). With drop_first=True one column
is dropped because it can be worked out from the others.

3. **Does a Decision Tree need scaling?**
I would say no. A tree splits on thresholds within one feature at a time ("Fare > 50?"), and
rescaling a feature keeps the order of its values, so the same splits are found.
Scaling matters for distance- or gradient-based models (KNN, SVM, linear/logistic
regression, neural nets).
