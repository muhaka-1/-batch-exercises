import os
import time
from collections import defaultdict, deque
from datetime import datetime, timedelta

file_path = "/data/payments.csv"
last_position = 0
recent_payments = defaultdict(deque)

print("Realtime monitor started", flush=True)

while not os.path.exists(file_path):
    time.sleep(1)

while True:
    with open(file_path, "r") as file:
        file.seek(last_position)
        lines = file.readlines()
        last_position = file.tell()

    for line in lines:
        if line.startswith("timestamp") or not line.strip():
            continue

        timestamp, user, amount = line.strip().split(",")
        amount = int(amount)
        now = datetime.fromisoformat(timestamp)

        print("Realtime received:", user, amount, flush=True)

    
        while recent_payments[user] and recent_payments[user][0] < now - timedelta(seconds=10):
            recent_payments[user].popleft()

        if len(recent_payments[user]) >= 3:
            print("🚨 ALERT: Many payments in short time:", user, flush=True)

    time.sleep(1)
