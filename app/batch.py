import csv
import os
import time
from collections import defaultdict
from datetime import datetime, timedelta

file_path = "/data/payments.csv"
BATCH_INTERVAL_SECONDS = 30

print("Batch job started", flush=True)

while not os.path.exists(file_path):
    time.sleep(1)

while True:
    time.sleep(BATCH_INTERVAL_SECONDS)
    window_end = datetime.now()
    window_start = window_end - timedelta(seconds=BATCH_INTERVAL_SECONDS)

    payments = []

    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                event_time = datetime.fromisoformat(row["timestamp"])
                amount = int(row["amount"])
            except (KeyError, ValueError):
                continue

            if window_start <= event_time <= window_end:
                row["amount"] = amount
                payments.append(row)

    print("\n📊 BATCH REPORT", flush=True)
    print(
        "Window:",
        f"{window_start.isoformat()} -> {window_end.isoformat()}",
        flush=True,
    )

    if not payments:
        print("No transactions in this window", flush=True)
        print("-" * 40, flush=True)
        continue

    total = sum(p["amount"] for p in payments)
    count = len(payments)

    per_user = defaultdict(int)
    for payment in payments:
        per_user[payment["user"]] += payment["amount"]

    top_3 = sorted(payments, key=lambda p: p["amount"], reverse=True)[:3]

    print("Transactions:", count, flush=True)
    print("Total amount:", total, flush=True)
    print("Average:", round(total / count, 2), flush=True)
    print("Revenue per user:", dict(per_user), flush=True)
    print("Top 3 payments:", top_3, flush=True)
    print("-" * 40, flush=True)
