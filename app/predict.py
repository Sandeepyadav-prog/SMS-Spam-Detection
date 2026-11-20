
import re
import joblib
import nltk

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Load saved model and TF-IDF vectorizer
model = joblib.load("models/best_spam_model.pkl")
tfidf = joblib.load("models/tfidf_vectorizer.pkl")

# Initialize NLP tools
nltk.download("stopwords", quiet=True)
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


# Prediction function
def predict_sms(message):

    cleaned_message = clean_text(message)

    message_vector = tfidf.transform([cleaned_message])

    prediction = model.predict(message_vector)[0]

    if hasattr(model, "predict_proba"):
        confidence = model.predict_proba(message_vector).max() * 100
    elif hasattr(model, "decision_function"):
        score = model.decision_function(message_vector)[0]
        confidence = None
    else:
        confidence = None

    result = "SPAM" if prediction == 1 else "HAM"

    return result, confidence


# Test prediction
if __name__ == "__main__":

    test_message = input("Enter an SMS message: ")

    result, confidence = predict_sms(test_message)

    print("\n========== PREDICTION RESULT ==========")
    print("Message:", test_message)
    print("Prediction:", result)

    if confidence is not None:
        print("Model confidence:", round(confidence, 2), "%")
    else:
        print("Confidence score: Not available for this model.")
