
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download stopwords
nltk.download("stopwords")

# Load dataset
df = pd.read_csv(
    "dataset/SMSSpamCollection",
    sep="\t",
    header=None,
    names=["label", "message"],
    encoding="utf-8"
)

# Initialize NLP tools
stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()

# Text cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    words = text.split()

    words = [
        stemmer.stem(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)

# Apply preprocessing
df["message"] = df["message"].fillna("").astype(str)

df["cleaned_message"] = df["message"].apply(clean_text)

df["cleaned_message"] = df["cleaned_message"].fillna("")

# Display original and cleaned messages
print("\nORIGINAL AND CLEANED MESSAGES:\n")

for i in range(10):
    print("Original:", df["message"].iloc[i])
    print("Cleaned :", df["cleaned_message"].iloc[i])
    print("-" * 60)

# Save processed dataset
df.to_csv(
    "dataset/processed_sms.csv",
    index=False
)

print("\nPreprocessing completed successfully!")
print("Processed dataset saved in dataset folder.")
