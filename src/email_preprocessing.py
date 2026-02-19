import pandas as pd
import re

df = pd.read_csv("data/email_raw_dataset.csv")

def clean_email(text):
    text = text.lower()
    text = re.sub(r"hi|hello|dear|regards|thanks", "", text)
    text = re.sub(r"[^a-z ]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

df["email_text"] = df["email_text"].apply(clean_email)

df.to_csv("data/email_cleaned_dataset.csv", index=False)

print("Clean email dataset ready")
