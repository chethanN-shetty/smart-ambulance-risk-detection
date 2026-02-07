# Smart Ambulance Risk Detection System

The project is a computer simulation of an ambulance monitoring pipeline in real-time to identify early patient deterioration in a setting that is noisy and has high motion rates.


## What This System Does
- Simulates realistic vital streams (HR, SpO₂, BP, Motion)
- Detects and suppresses motion-induced sensor artifacts
- Identifies early deterioration using trend-based logic
- Risk scoring is exposed to a FastAPI service.
##  📢❗🚨 Demo Configuration Note  📢❗🚨

Some tuning of certain thresholds (analysis window size and risk sensitivity) was required to visualize gradual deterioration within the short demo period to view alert behavior in the course of the simulation.ety.
These parameters are developed only to demonstrate and visualize. More conservative thresholds and windows would be applied in a real deployment to both favor false-suppression of alerts and patient safety.

## How to Run

### 1. Generate Data
python src/simulate_stream.py

