import pandas as pd
from datetime import datetime, timezone

df = pd.read_csv("data/clean/events.csv")

df["timestamp"] = pd.to_datetime(df["timestamp"])
df['date'] = df['timestamp'].dt.date


df.to_csv("data/transformed/events.csv", index=False)