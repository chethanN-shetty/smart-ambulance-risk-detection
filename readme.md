# Smart Ambulance Risk Detection System

The project is a computer simulation of an ambulance monitoring pipeline in real-time to identify early patient deterioration in a setting that is noisy and has high motion rates.


## What This System Does
- Simulates realistic vital streams (HR, SpO₂, BP, Motion)
- Detects and suppresses motion-induced sensor artifacts
- Identifies early deterioration using trend-based logic
- Risk scoring is exposed to a FastAPI service.
##  📢❗🚨 Demo Configuration Note  📢❗🚨

there are some values been altered for demo execution for example like analysis **##window size and risk sensitivity** requierd visualize gradual deterioration within the short demo period to view alert behavior
These parameters are developed only to demonstrate and visualize.

## How to Run

### 1. Generate Data
python src/simulate_stream.py


