# Campus Delivery Fraud Detection Environment

## 📌 Overview

This project simulates a real-world campus delivery system where AI agents must detect fraudulent pickup requests.

The goal is to train an agent to decide whether to:

* Accept a request
* Reject a request
* Verify a request

---

## 🧠 Problem Motivation

Campus delivery systems often face fake order requests, causing time loss and inefficiency.
This environment models fraud detection using realistic signals like payment status, trust score, and order validation.

---

## 📊 Observation Space

Each request contains:

* user_id
* order_id
* user_history
* payment_status
* location_match
* device_trust_score
* active_orders
* screenshot_uploaded
* order_exists
* order_age
* cancel_after_pickup

---

## ⚙️ Action Space

* accept
* reject
* verify

---

## ⭐ Reward Function

The reward is designed with multiple levels:

* Correct decision → positive reward
* Safe verification → partial reward
* Fraud detection signals → additional reward
* Wrong decisions → penalty

---

## 🧪 Tasks

### 🟢 Easy

Detect whether request is real or fake

### 🟡 Medium

Choose correct action (accept / reject / verify)

### 🔴 Hard

Handle complex fraud patterns (missing proof, multiple orders, cancellation abuse)

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
python inference.py
```

---

## 📈 Baseline Result

Total Score: ~6.9

---

## 🧠 Key Features

* Multi-factor fraud detection
* Realistic simulation environment
* Graded reward system
* Edge-case handling

---

## 🐳 Docker Support

```bash
docker build -t campus-env .
docker run campus-env
```
