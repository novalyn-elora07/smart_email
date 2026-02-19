import pandas as pd
import random
from datetime import datetime, timedelta

complaints = [
"""Hi Team,
My order has not been delivered yet.
Please resolve ASAP.

Regards,
Customer"""
]

requests = [
"""Hello,
Need invoice copy for last purchase.

Thanks"""
]

feedback = [
"""Hi,
Really happy with the service.

Regards"""
]

spam = [
"""Congratulations!!!
Win lottery now click link"""
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
start_date = datetime(2022,1,1)

for i in range(5200):
    category = random.choice(list(category_map.keys()))
    email_text = random.choice(category_map[category])
    urgency = urgency_map[category]
    timestamp = start_date + timedelta(days=random.randint(0,900))

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
