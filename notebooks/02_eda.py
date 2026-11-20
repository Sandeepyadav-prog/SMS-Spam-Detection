
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(
    "dataset/SMSSpamCollection",
    sep="\t",
    header=None,
    names=["label", "message"],
    encoding="utf-8"
)

# Display dataset overview
print("TOTAL MESSAGES:", len(df))
print("\nCATEGORY DISTRIBUTION:")
print(df["label"].value_counts())

# Calculate message length
df["message_length"] = df["message"].apply(len)

print("\nAVERAGE MESSAGE LENGTH:")
print(df.groupby("label")["message_length"].mean())

# Plot spam and ham distribution
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="label")
plt.title("Spam vs Ham Message Distribution")
plt.xlabel("Message Category")
plt.ylabel("Number of Messages")
plt.tight_layout()
plt.show()

# Plot message length distribution
plt.figure(figsize=(8, 5))
sns.histplot(
    data=df,
    x="message_length",
    hue="label",
    bins=40,
    kde=True
)
plt.title("Message Length Distribution")
plt.xlabel("Message Length")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
