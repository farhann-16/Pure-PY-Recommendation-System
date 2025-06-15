# Network Recommendation System

This is a simple recommendation system built using pure Python. It simulates features commonly seen in social networks, such as suggesting friends and recommending pages based on shared connections and interests.

No external libraries were used — everything is written with built-in Python logic and data structures.

---

## Features

- **Clean and Structure Raw Data**: Parses a JSON-style dataset of users and pages into a usable format.
- **People You May Know**: Recommends friends based on mutual connections.
- **Pages You Might Like**: Suggests pages based on similar user interests.

---

## File Overview

- `user_data.json` – Sample dataset of users, friendships, and liked pages
- `clean_data.py` – Processes and structures the input data
- `recommend_friends.py` – Friend suggestion logic
- `recommend_pages.py` – Page recommendation logic

---

## How to Use

1. Make sure you have Python 3 installed.
2. Clone or download this repository.
3. Run the scripts using:

```bash
python clean_data.py
python recommend_friends.py
python recommend_pages.py
