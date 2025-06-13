import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
digits = load_digits()
X, y = digits.data, digits.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Define hyperparameters to evaluate
logreg_C_values = [0.01, 0.1, 1, 10]
svm_C_values = [0.1, 1, 10]
rf_n_estimators = [10, 50, 100]

# Evaluation storage
results = {}

# Logistic Regression
for C in logreg_C_values:
    model = LogisticRegression(C=C, max_iter=1000)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    results[f'LogReg_C={C}'] = acc

# SVM
for C in svm_C_values:
    model = SVC(C=C)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    results[f'SVM_C={C}'] = acc

# Random Forest
for n in rf_n_estimators:
    model = RandomForestClassifier(n_estimators=n, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    results[f'RF_n={n}'] = acc

# Display results
print("\nEvaluation Results:")
for key, val in results.items():
    print(f"{key}: {val:.4f}")
