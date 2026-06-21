# Batch vs Realtime Lab

Lab for demonstrating:
- Batch processing
- Realtime systems
- Event streams
- Fraud detection
- Data pipelines

## Run

```bash
docker compose up
```

## Components

- generator -> creates fake payment events
- realtime -> processes events immediately
- batch -> generates 30-second windowed reports every 30 seconds

## View data

```bash
tail -f data/payments.csv
```


# Batch vs Realtime Lab

 Docker lab for learning:

- Big Data
- Distributed systems
- Batch processing
- Realtime systems
- Event-driven architecture
- Fraud detection
- Data pipelines
- Event streams
- Scaling tradeoffs


# Overview

This lab simulates a simplified payment platform similar to:

- Swish
- Stripe
- Klarna
- PayPal

We will work with:

- realtime fraud detection
- batch analytics
- event streams
- distributed consumers
- scaling problems
- data quality issues

The goal is to understand the architectural differences between:

- batch systems
- realtime systems
- queues
- streams
- analytics systems
- operational systems

# Architecture

```text
                +----------------+
                |   Generator    |
                | payment events |
                +--------+-------+
                         |
                         v
               payments.csv
                         |
         +---------------+---------------+
         |                               |
         v                               v
+----------------+          +----------------------+
| Realtime       |          | Batch Processing     |
| Fraud Detection|          | Analytics & Reports  |
+----------------+          +----------------------+
```


# Components

## Generator

Continuously generates fake payment events.

Example:

```json
{
  "timestamp": "2025-05-27T09:00:01",
  "user": "alice",
  "amount": 4200
}
```


## Realtime Service

Processes events immediately.

Detects:
- suspicious payments
- fraud patterns
- high transaction frequency

Examples:
- payment > 3000
- many payments within short time


## Batch Service

Processes historical data periodically.

Creates:
- analytics reports
- user statistics
- revenue summaries
- top spender reports

Runs every 30 seconds.


# Getting Started

## Requirements

- Docker
- Docker Compose


# Run the Lab

```bash
docker compose up
```


# Watch Events

```bash
tail -f data/payments.csv
```


# Stop the Lab

```bash
docker compose down
```


# Goals

Students should understand:

- why realtime systems are expensive
- why batch still exists
- why distributed systems are difficult
- eventual consistency
- event streams
- backpressure
- scaling tradeoffs
- data quality problems

---

# Exercise 1 — Fraud Team

## Goal

Detect suspicious payments in realtime.

## Tasks

Implement detection for:
- payments over 3000
- multiple payments within 10 seconds
- repeated payment amounts

## Bonus

Add:
- blacklisted users
- fraud score
- suspicious country detection

## Concepts

- realtime processing
- stateful systems
- event windows

---

# Exercise 2 — Data Quality Team

## Goal

Handle bad events safely.

## Tasks

Inject broken events:

```python
{
    "user": None,
    "amount": "INVALID"
}
```

Students must:
- validate events
- reject invalid data
- create error logs

## Concepts

- schema validation
- garbage in → garbage out
- defensive programming

---

# Exercise 3 — Batch Analytics Team

## Goal

Improve batch reporting.

## Tasks

Add:
- revenue per user
- average transaction
- top spender
- hourly transaction volume

## Bonus

Export reports to:
- JSON
- CSV

## Concepts

- batch processing
- OLAP systems
- analytics workloads

---

# Exercise 4 — Backpressure

## Goal

Simulate overloaded systems.

## Tasks

Increase event generation speed:

```python
time.sleep(0.01)
```

Observe:
- lagging consumers
- growing files
- delayed processing

## Discussion

What happens when:
- producers are faster than consumers?
- systems cannot keep up?

## Concepts

- backpressure
- buffering
- queues
- scaling

---

# Key Concepts
- batch vs realtime
- event-driven systems
- streams vs queues
- scaling
- partitioning
- replication
- eventual consistency
- OLTP vs OLAP
- backpressure
- distributed failures


# Discussion Questions

- Why not process everything realtime?
- Why does Big Data require distributed systems?
- When is eventual consistency acceptable?
- Why are queues useful?
- Why do companies separate OLTP and OLAP?
- Why is observability critical?
- Why is scaling difficult?


# Suggested Extensions

Advanced students can add:

- Kafka
- Redis
- PostgreSQL
- WebSockets
- Dashboards
- Kubernetes
- Metrics collection
- Distributed tracing


# Educational Goal
The focus is understanding:
- architecture
- tradeoffs
- scaling challenges
