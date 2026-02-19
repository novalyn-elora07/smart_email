import pandas as pd
import re

# load raw dataset
df = pd.read_csv("data/email_raw_dataset.csv")

# function to clean enterprise emails
def clean_email(text):
    text = text.lower()

    # remove greetings & signatures
    text = re.sub(r"hi|hello|dear|regards|thanks", "", text)

    # remove special characters
    text = re.sub(r"[^a-z ]", "", text)

    # remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()

# apply cleaning
df["email_text"] = df["email_text"].apply(clean_email)

# save cleaned dataset
df.to_csv("data/email_cleaned_dataset.csv", index=False)

print("Clean email dataset ready")
