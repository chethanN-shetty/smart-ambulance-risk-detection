# Smart Ambulance Risk Detection System

This project simulates a real-time ambulance monitoring pipeline for detecting early patient deterioration under noisy, motion-heavy conditions.

## What This System Does
- Simulates realistic vital streams (HR, SpO₂, BP, Motion)
- Detects and suppresses motion-induced sensor artifacts
- Identifies early deterioration using trend-based logic
- Exposes risk scoring via a FastAPI service

## How to Run

### 1. Generate Data
```bash
python src/simulate_stream.py
