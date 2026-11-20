
# 🛡️ SMS Shield – SMS Spam Detection System

## Project Overview

SMS Shield is a Machine Learning and Natural Language Processing (NLP) based application that identifies whether an SMS message is Spam or Ham (Genuine).

The system analyses message content using text preprocessing, TF-IDF feature extraction and machine learning classification.

## Objectives

- Detect unwanted and fraudulent SMS messages.
- Apply NLP techniques to clean and process text.
- Convert text into numerical features using TF-IDF.
- Compare multiple machine learning algorithms.
- Build an interactive web application for real-time predictions.

## Technologies Used

- Python
- Pandas and NumPy
- NLTK
- Scikit-learn
- Streamlit
- Joblib
- TF-IDF Vectorization

## Dataset

UCI SMS Spam Collection Dataset.

Dataset source:
https://archive.ics.uci.edu/dataset/228/sms+spam+collection

Total messages: 5,572

Classes:
- Ham (Genuine)
- Spam

## Machine Learning Models

Three algorithms were trained and evaluated:

1. Multinomial Naive Bayes
2. Logistic Regression
3. Support Vector Machine (SVM)

## Model Performance

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---:|---:|---:|---:|
| Naive Bayes | 96.41% | 99.11% | 74.00% | 84.73% |
| Logistic Regression | 96.59% | 98.28% | 76.00% | 85.71% |
| SVM | 98.03% | 96.38% | 88.67% | 92.36% |

Best-performing model: Support Vector Machine (SVM).

## Project Workflow

1. Dataset collection
2. Exploratory Data Analysis
3. Text preprocessing
4. TF-IDF feature extraction
5. Model training
6. Model evaluation
7. Best model selection
8. Streamlit web application development

## Project Structure

```text
SMS_Spam_Detection/
├── app/
│   ├── __init__.py
│   ├── predict.py
│   └── streamlit_app.py
├── dataset/
├── models/
├── notebooks/
├── requirements.txt
├── README.md
└── .gitignore
```

## Run Locally

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Move into the project directory:

```bash
cd SMS_Spam_Detection
```

Create and activate a virtual environment, then install dependencies:

```bash
python -m venv venv
```

Windows CMD:

```cmd
venv\Scripts\activate.bat
```

Install requirements:

```bash
pip install -r requirements.txt
```

Launch the application:

```bash
python -m streamlit run app/streamlit_app.py
```

## Expected Output

The application classifies an entered SMS message as:

- Spam Message
- Genuine Message (Ham)

## Future Enhancements

- Deep learning-based spam detection.
- Improved confidence calibration.
- Multilingual SMS classification.
- More advanced security analysis.

## Project Status

Machine learning model and local Streamlit application successfully developed and tested.

Online deployment: In progress.
