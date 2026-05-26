<<<<<<< HEAD
# Project 2 — Data Classification Using AI
**DecodeLabs Industrial Training Kit | Batch 2026**

---

## Overview

This project builds a supervised machine learning pipeline that classifies iris flowers into one of three species using the K-Nearest Neighbors (KNN) algorithm. It covers the full ML workflow: loading data, preprocessing, training, and evaluation.

---

## File

| File | Description |
|------|-------------|
| `project2_iris_knn.py` | Main script — runs the full pipeline end to end |
| `project2_results.png` | Output chart — elbow curve + confusion matrix |

---

## Requirements

Install dependencies before running:

```bash
pip install scikit-learn pandas matplotlib seaborn
```

> On Windows with the Microsoft Store Python, use:
> ```bash
> pip install scikit-learn pandas matplotlib seaborn --break-system-packages
> ```

---

## How to Run

```bash
python project2_iris_knn.py
```

The script prints results to the console and saves a chart as `project2_results.png` in the same folder.

---

## Pipeline — Step by Step

### Step 1 — Load the dataset
```python
from sklearn.datasets import load_iris
iris = load_iris()
```
Loads the built-in Iris benchmark dataset: 150 flower samples, 4 features each (sepal length, sepal width, petal length, petal width), belonging to 3 species (setosa, versicolor, virginica).

---

### Step 2 — Separate features and labels
```python
X = iris.data    # shape (150, 4) — the measurements
y = iris.target  # shape (150,)   — 0, 1, or 2
```
`X` is what the model sees. `y` is the correct answer it must learn to predict.

---

### Step 3 — Train / test split (80% / 20%)
```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, shuffle=True, stratify=y
)
```
- 120 samples for training, 30 samples locked away for testing
- `shuffle=True` removes order bias
- `stratify=y` keeps all 3 classes equally represented in both sets
- `random_state=42` makes the split reproducible

---

### Step 4 — Feature scaling (StandardScaler)
```python
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)
```
KNN uses distances between points. Without scaling, features with large ranges dominate. `StandardScaler` normalizes every feature to **mean = 0, variance = 1**.

> The scaler is **fitted on training data only** — applying it to the test set separately prevents data leakage.

---

### Step 5 — Find the optimal K (elbow method)
```python
for k in range(1, 21, 2):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    error_rate = 1 - f1_score(y_test, preds, average="macro")
```
Tests odd values of k from 1 to 19. The optimal k is the one with the lowest error — the "elbow" of the error curve.

| k too low | k too high |
|-----------|------------|
| Overfits to noise | Underfits — too generic |
| k = 1 | k = 100 |

---

### Step 6 — Train the final model
```python
model = KNeighborsClassifier(n_neighbors=optimal_k)
model.fit(X_train_scaled, y_train)
predictions = model.predict(X_test_scaled)
```
Three lines: instantiate → fit → predict. KNN works by majority vote — a new sample is classified by looking at its k nearest neighbors in the training set.

---

### Step 7 — Evaluate
```python
confusion_matrix(y_test, predictions)
f1_score(y_test, predictions, average="macro")
```
- **Confusion matrix** — shows exactly which classes were confused with which (TP, FP, FN, TN per class)
- **F1 score** — harmonic mean of precision and recall; more reliable than accuracy alone on multi-class problems

---

### Step 8 — Visualize
```python
plt.savefig("project2_results.png", dpi=150, bbox_inches="tight")
```
Saves two side-by-side charts:
1. **Elbow curve** — error rate vs k value
2. **Confusion matrix heatmap** — predicted vs actual classes

---

## Sample Output

```
Macro F1 Score : 0.9666  (1.0 = perfect)

              precision    recall  f1-score   support
      setosa       1.00      1.00      1.00        10
  versicolor       0.91      1.00      0.95        10
   virginica       1.00      0.90      0.95        10
=======

## 👤 Author

**Ziad** — DecodeLab Internship Project
>>>>>>> d3477d4889b2d052708060f80fda322a2a57a48a
