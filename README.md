---
title: Campus Delivery Env
emoji: 🚚
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
---

# 🚚 Campus Delivery Fraud Detection Environment

## 📌 Overview

This project simulates a **real-world campus delivery system** where an AI agent must detect **fraudulent pickup requests**.

The agent interacts with the environment and decides whether to:

- ✅ Accept a request  
- ❌ Reject a request  
- 🔍 Verify a request  

The environment follows the **OpenEnv standard** with `reset()`, `step()`, and `state()` APIs.

---

## 🧠 Problem Motivation

Delivery platforms (like **Swiggy / Zomato-style systems**) often face:

- Fake order pickups  
- Refund abuse  
- Identity spoofing  
- Multiple active order fraud  

This environment models these real-world fraud patterns using structured signals, enabling agents to **learn safe and efficient decision-making**.

---

## 📊 Observation Space

Each request includes structured signals:

- `user_id` – Unique user identifier  
- `order_id` – Order reference  
- `user_history` – Number of past orders  
- `payment_status` – Payment verification  
- `location_match` – Location consistency  
- `device_trust_score` – Trustworthiness (0–1)  
- `active_orders` – Current active deliveries  
- `screenshot_uploaded` – Proof of order  
- `order_exists` – Backend validation  
- `order_age` – Time since order placed  
- `cancel_after_pickup` – Fraud indicator  

---

## ⚙️ Action Space

The agent can choose:

- `accept` → Approve request  
- `reject` → Deny request  
- `verify` → Ask for additional confirmation  

---

## ⭐ Reward Function

The reward system is **multi-level and realistic**:

- ✔ Correct decisions → High reward  
- ⚖️ Safe verification → Partial reward  
- 🚨 Fraud detection signals → Bonus reward  
- ❌ Wrong actions → Penalty  

All rewards are normalized to **0.0 – 1.0**, ensuring stable learning.

---

## 🧪 Tasks

The environment includes **3 progressively difficult tasks**:

### 🟢 Easy — `easy_detect_fake`
- Detect whether a request is real or fake  

### 🟡 Medium — `medium_choose_action`
- Choose correct action (accept / reject / verify)  

### 🔴 Hard — `hard_edge_cases`
- Handle complex fraud patterns:
  - Missing proof  
  - Multiple active orders  
  - Cancellation abuse  
  - Device trust anomalies  

---

## 🤖 Agent Strategy (Baseline)

A simple rule-based agent is implemented:

- High user history → Accept  
- Invalid order → Reject  
- Uncertain cases → Verify  

This baseline ensures reproducible evaluation across all tasks.

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
python inference.py
---

## 📈 Baseline Performance

- Average Score: **~0.45 – 0.7 (varies by task)**
- Demonstrates stable decision-making across all difficulty levels

---

## 🧠 Key Features

- ✅ Real-world inspired fraud detection  
- ✅ Multi-task environment (easy → hard)  
- ✅ Structured observation space  
- ✅ Reward shaping with partial signals  
- ✅ OpenEnv compliant design  
- ✅ Safe LLM integration (OpenAI client)  

---

## 🐳 Docker Support

```bash
docker build -t campus-env .
docker run campus-env