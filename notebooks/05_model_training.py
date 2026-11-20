
import joblib
import pandas as pd

from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

# Load TF-IDF training and testing data
X_train, X_test, y_train, y_test = joblib.load(
    "models/train_test_data.pkl"
)

# Define machine learning models
models = {
    "Naive Bayes": MultinomialNB(),
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "SVM": LinearSVC()
}

results = []
trained_models = {}

# Train and evaluate each model
for name, model in models.items():

    print("\nTraining:", name)

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions, zero_division=0)
    recall = recall_score(y_test, predictions, zero_division=0)
    f1 = f1_score(y_test, predictions, zero_division=0)

    results.append({
        "Model": name,
        "Accuracy": round(accuracy * 100, 2),
        "Precision": round(precision * 100, 2),
        "Recall": round(recall * 100, 2),
        "F1 Score": round(f1 * 100, 2)
    })

    trained_models[name] = model

    print("Accuracy:", round(accuracy * 100, 2), "%")
    print("Precision:", round(precision * 100, 2), "%")
    print("Recall:", round(recall * 100, 2), "%")
    print("F1 Score:", round(f1 * 100, 2), "%")

# Display comparison
results_df = pd.DataFrame(results)

print("\n========== MODEL COMPARISON ==========")
print(results_df.to_string(index=False))

# Select model with highest F1 score
best_model_name = results_df.loc[
    results_df["F1 Score"].idxmax(), "Model"
]

best_model = trained_models[best_model_name]

# Save best model
joblib.dump(best_model, "models/best_spam_model.pkl")

# Save results
results_df.to_csv("models/model_comparison.csv", index=False)

print("\nBEST MODEL:", best_model_name)
print("Best model saved successfully!")
