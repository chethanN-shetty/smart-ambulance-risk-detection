# Smart Ambulance Risk Detection System

This project simulates a real-time ambulance monitoring pipeline for detecting early patient deterioration under noisy, motion-heavy conditions.

## What This System Does
- Simulates realistic vital streams (HR, SpO₂, BP, Motion)
- Detects and suppresses motion-induced sensor artifacts
- Identifies early deterioration using trend-based logic
- Exposes risk scoring via a FastAPI service
##  📢❗🚨 Demo Configuration Note  📢❗🚨

To visualize alert behavior during simulation, certain thresholds (such as analysis window size and risk sensitivity) were tuned to make gradual deterioration observable within a short demo duration.

These parameters are intended for demonstration and visualization purposes only. In a real deployment setting, more conservative thresholds and longer windows would be used to prioritize false-alert suppression and patient safety.

## How to Run

### 1. Generate Data
```bash
python src/simulate_stream.py
