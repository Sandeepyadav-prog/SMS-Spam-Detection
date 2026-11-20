# 📱 SMS Shield – Intelligent SMS Spam Detection Using NLP & Machine Learning

## 🚀 Live Demo

**Try the live application here:**

https://sms-spam-detection-omcd3vztcjkbixjqcykv9v.streamlit.app/

## 📌 Project Overview

SMS Shield is an intelligent SMS Spam Detection system developed using Natural Language Processing (NLP) and Machine Learning.

The system automatically classifies SMS messages into two categories:

- **Spam:** Unwanted, fraudulent, promotional, or suspicious messages.
- **Ham:** Genuine and legitimate messages.

The application uses text preprocessing, TF-IDF feature extraction, and machine learning algorithms to identify spam messages. It provides an interactive web interface built with Streamlit, allowing users to enter SMS messages and receive instant predictions.

## 🎯 Project Objectives

- Develop an automated SMS spam detection system.
- Apply NLP techniques to clean and process text messages.
- Perform exploratory data analysis on SMS data.
- Convert textual messages into numerical features using TF-IDF.
- Train and compare multiple machine learning models.
- Evaluate models using accuracy, precision, recall, and F1-score.
- Deploy the best-performing model through an interactive web application.

## 📂 Dataset

**Dataset:** SMS Spam Collection Dataset

**Source:** UCI Machine Learning Repository

Dataset link: https://archive.ics.uci.edu/dataset/228/sms+spam+collection

The dataset contains approximately 5,572 SMS messages labelled as:

- `ham` – Legitimate messages.
- `spam` – Unwanted or fraudulent messages.

The dataset was used for text preprocessing, exploratory analysis, model training, and evaluation.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Exploratory data analysis |
| NLTK | Natural Language Processing |
| Scikit-learn | Machine Learning |
| TF-IDF | Text feature extraction |
| Joblib | Model serialization |
| Streamlit | Web application |
| Git & GitHub | Version control and project hosting |

## ⚙️ Project Workflow

### 1. Dataset Collection
Collected the SMS Spam Collection dataset from the UCI Machine Learning Repository.

### 2. Exploratory Data Analysis (EDA)
- Analyzed the dataset structure.
- Examined spam and ham distribution.
- Studied message lengths.
- Visualized the distribution of message categories.

### 3. Text Preprocessing
Applied the following NLP techniques:

- Lowercase conversion.
- URL removal.
- Removal of unnecessary characters.
- Stopword removal.
- Stemming using Porter Stemmer.
- Handling missing and empty messages.

### 4. Feature Extraction

Used **TF-IDF (Term Frequency–Inverse Document Frequency)** to convert text messages into numerical feature vectors.

Configuration:
- Maximum features: 5,000.
- Training and testing split: 80:20.
- Stratified sampling.
- Random state: 42.

### 5. Model Development

Three machine learning algorithms were trained and compared:

1. Multinomial Naive Bayes
2. Logistic Regression
3. Support Vector Machine (LinearSVC)

### 6. Model Evaluation

Models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score

### 7. Web Application Development

Developed an interactive Streamlit application that allows users to:

- Enter SMS messages.
- Analyze messages instantly.
- Identify spam and legitimate messages.
- View prediction results.
- Test sample spam and ham messages.

### 8. Deployment