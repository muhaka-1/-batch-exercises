import csv
import random
import time
from datetime import datetime

users = ["alice", "bob", "charlie", "diana"]
file_path = "/data/payments.csv"

with open(file_path, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["timestamp", "user", "amount"])
    writer.writeheader()

print("Generator started", flush=True)

while True:
    payment = {
        "timestamp": datetime.now().isoformat(),
        "user": random.choice(users),
        "amount": random.randint(10, 5000),
    }

    with open(file_path, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["timestamp", "user", "amount"])
        writer.writerow(payment)

    print("Generated:", payment, flush=True)
    time.sleep(1)
