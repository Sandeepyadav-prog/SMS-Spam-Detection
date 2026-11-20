
import pandas as pd

# Dataset file path
file_path = "dataset/SMSSpamCollection"

# Load the SMS dataset
df = pd.read_csv(
    file_path,
    sep="\t",
    header=None,
    names=["label", "message"],
    encoding="utf-8"
)

# Display first 10 records
print("FIRST 10 SMS MESSAGES:")
print(df.head(10))

# Display dataset information
print("\nDATASET INFORMATION:")
print(df.info())

# Count spam and ham messages
print("\nMESSAGE CATEGORY COUNTS:")
print(df["label"].value_counts())

# Display dataset shape
print("\nDATASET SHAPE:")
print(df.shape)
