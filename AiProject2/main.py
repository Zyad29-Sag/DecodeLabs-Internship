# ============================================================
# DecodeLabs | Project 2: Data Classification Using AI
# Algorithm  : K-Nearest Neighbors (KNN)
# Dataset    : Iris Benchmark (150 samples, 3 classes, 4 features)
# ============================================================

# ── IMPORTS ──────────────────────────────────────────────────
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    f1_score,
    ConfusionMatrixDisplay,
)

# ─────────────────────────────────────────────────────────────
# STEP 1 — LOAD & EXPLORE THE DATASET
# ─────────────────────────────────────────────────────────────
iris = load_iris()

# Wrap in a DataFrame so it reads like a spreadsheet
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = pd.Categorical.from_codes(iris.target, iris.target_names)

print("=" * 55)
print("  STEP 1 — DATASET OVERVIEW")
print("=" * 55)
print(f"  Shape   : {df.shape}  (rows × columns)")
print(f"  Classes : {list(iris.target_names)}")
print(f"  Features: {list(iris.feature_names)}")
print()
print(df.head(5).to_string(index=False))
print()
print("  Class distribution:")
print(df["species"].value_counts().to_string())
print()

# ─────────────────────────────────────────────────────────────
# STEP 2 — SEPARATE FEATURES (X) AND LABELS (y)
# ─────────────────────────────────────────────────────────────
X = iris.data        # shape (150, 4)
y = iris.target      # 0 = setosa | 1 = versicolor | 2 = virginica

# ─────────────────────────────────────────────────────────────
# STEP 3 — TRAIN / TEST SPLIT  (80 % train | 20 % test)
#           shuffle=True removes order bias (as shown in the PDF)
# ─────────────────────────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    shuffle=True,
    stratify=y,          # keeps class ratios equal in both sets
)

print("=" * 55)
print("  STEP 3 — TRAIN / TEST SPLIT")
print("=" * 55)
print(f"  Training samples : {len(X_train)}  (80 %)")
print(f"  Test samples     : {len(X_test)}   (20 %)")
print()

# ─────────────────────────────────────────────────────────────
# STEP 4 — FEATURE SCALING  (StandardScaler → mean=0, var=1)
#           Fit ONLY on training data; transform both sets.
#           This prevents data leakage from the test set.
# ─────────────────────────────────────────────────────────────
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)   # learn + apply
X_test_scaled  = scaler.transform(X_test)        # apply only

print("=" * 55)
print("  STEP 4 — FEATURE SCALING (StandardScaler)")
print("=" * 55)
print(f"  Training mean (after scaling): {X_train_scaled.mean(axis=0).round(4)}")
print(f"  Training std  (after scaling): {X_train_scaled.std(axis=0).round(4)}")
print()

# ─────────────────────────────────────────────────────────────
# STEP 5 — FIND THE OPTIMAL K  (the Elbow Method)
#           Try odd values of k to avoid ties in voting.
# ─────────────────────────────────────────────────────────────
k_range   = range(1, 21, 2)   # 1, 3, 5, … 19
error_rates = []

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    preds      = knn.predict(X_test_scaled)
    error_rate = 1 - f1_score(y_test, preds, average="macro")
    error_rates.append(error_rate)

optimal_k = list(k_range)[error_rates.index(min(error_rates))]

print("=" * 55)
print("  STEP 5 — CHOOSING OPTIMAL K (Elbow Method)")
print("=" * 55)
for k, e in zip(k_range, error_rates):
    marker = " ◀ OPTIMAL" if k == optimal_k else ""
    print(f"    k={k:2d}  error={e:.4f}{marker}")
print()

# ─────────────────────────────────────────────────────────────
# STEP 6 — TRAIN THE FINAL KNN MODEL
# ─────────────────────────────────────────────────────────────
model = KNeighborsClassifier(n_neighbors=optimal_k)
model.fit(X_train_scaled, y_train)           # FIT  — memorize the map
predictions = model.predict(X_test_scaled)   # PREDICT — apply logic

print("=" * 55)
print(f"  STEP 6 — MODEL TRAINED  (k = {optimal_k})")
print("=" * 55)
print()

# ─────────────────────────────────────────────────────────────
# STEP 7 — EVALUATE  (Confusion Matrix + F1 Score)
# ─────────────────────────────────────────────────────────────
cm = confusion_matrix(y_test, predictions)
f1 = f1_score(y_test, predictions, average="macro")

print("=" * 55)
print("  STEP 7 — EVALUATION RESULTS")
print("=" * 55)
print()
print(classification_report(
    y_test, predictions,
    target_names=iris.target_names
))
print(f"  Macro F1 Score : {f1:.4f}  (1.0 = perfect)")
print()

# ─────────────────────────────────────────────────────────────
# STEP 8 — VISUALISATIONS
# ─────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle("DecodeLabs | Project 2 — KNN Iris Classification",
             fontsize=14, fontweight="bold")

# --- Plot A: Elbow Curve ---
ax = axes[0]
ax.plot(list(k_range), error_rates, marker="o",
        color="#1a3a6b", linewidth=2, markersize=7)
ax.axvline(optimal_k, color="#e85d04", linestyle="--",
           label=f"Optimal k = {optimal_k}")
ax.set_title("Elbow Curve — Choosing K")
ax.set_xlabel("K Value")
ax.set_ylabel("Error Rate  (1 − F1)")
ax.legend()
ax.grid(True, alpha=0.3)

# --- Plot B: Confusion Matrix ---
ax = axes[1]
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=iris.target_names
)
disp.plot(ax=ax, colorbar=False, cmap="Blues")
ax.set_title(f"Confusion Matrix  (k = {optimal_k},  F1 = {f1:.2f})")

plt.tight_layout()
plt.savefig("project2_results.png",
            dpi=150, bbox_inches="tight")
plt.close()

print("  Chart saved → project2_results.png")
print()
print("=" * 55)
print("Done")
print("=" * 55)