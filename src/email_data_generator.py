import pandas as pd
import random
from datetime import datetime, timedelta

# Enterprise-style email templates
complaints = [
"""Hi Team,
My payment was deducted but order not confirmed.
This is urgent. Please resolve immediately.

Regards,
Customer""",

"""Hello Support,
The application keeps crashing during checkout.
Need urgent fix.

Thanks"""
]

requests = [
"""Dear Team,
Can you please share the invoice for last month?

Regards""",

"""Hello,
I would like to upgrade my subscription plan.
Please guide me.

Thanks"""
]

feedback = [
"""Hi,
Really happy with the service provided.
Great support team.

Regards""",

"""Hello Team,
Loved the recent update.
Very smooth experience.

Thanks"""
]

spam = [
"""Congratulations!!!
You have won a free vacation. Click here now!!!""",

"""Earn money fast from home.
Limited time offer. Visit this link."""
]

category_map = {
    "complaint": complaints,
    "request": requests,
    "feedback": feedback,
    "spam": spam
}

urgency_map = {
    "complaint": "high",
    "request": "medium",
    "feedback": "low",
    "spam": "low"
}

rows = []
start_date = datetime(2022, 1, 1)

for i in range(5200):
    category = random.choice(list(category_map.keys()))
    email_text = random.choice(category_map[category])
    urgency = urgency_map[category]
    timestamp = start_date + timedelta(days=random.randint(0, 900))

    rows.append([i, email_text, category, urgency, timestamp])

df = pd.DataFrame(rows, columns=[
    "email_id",
    "email_text",
    "category",
    "urgency",
    "timestamp"
])

df.to_csv("data/email_raw_dataset.csv", index=False)

print("Raw enterprise email dataset created")
