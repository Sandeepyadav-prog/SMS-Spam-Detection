
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

# Load processed dataset
df = pd.read_csv("dataset/processed_sms.csv")

# Handle missing and empty text values
df["cleaned_message"] = (
    df["cleaned_message"]
    .fillna("")
    .astype(str)
)

# Remove rows with missing labels
df = df.dropna(subset=["label"])

# Remove empty messages
df = df[df["cleaned_message"].str.strip() != ""]

# Separate input and target
X = df["cleaned_message"]
y = df["label"].map({"ham": 0, "spam": 1})

# Remove any invalid labels
valid_rows = y.notna()
X = X[valid_rows]
y = y[valid_rows].astype(int)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# TF-IDF feature extraction
tfidf = TfidfVectorizer(max_features=5000)

X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

# Save vectorizer
joblib.dump(tfidf, "models/tfidf_vectorizer.pkl")

# Save training and testing data
joblib.dump(
    (X_train_tfidf, X_test_tfidf, y_train, y_test),
    "models/train_test_data.pkl"
)

print("\nTF-IDF FEATURE EXTRACTION COMPLETED!")

print("Total valid messages:", len(X))
print("Training samples:", X_train_tfidf.shape[0])
print("Testing samples:", X_test_tfidf.shape[0])
print("TF-IDF features:", X_train_tfidf.shape[1])

print("\nTraining data shape:", X_train_tfidf.shape)
print("Testing data shape:", X_test_tfidf.shape)

print("\nFiles saved successfully in models folder!")
