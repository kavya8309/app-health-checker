#  Application Health Checker

## Overview
A Python automation tool that monitors website uptime using HTTP status codes and logs real-time application status (UP/DOWN) with timestamps.

---

##  Features
- Monitors application availability
- Uses HTTP status code (200 = UP)
- Detects DOWN or timeout errors
- Real-time continuous monitoring
- Timestamp-based logging

---

## Technologies Used
- Python
- Requests library
- Time module
- Datetime module

---

##  How to Run

```bash
pip install requests
python app_health.py
