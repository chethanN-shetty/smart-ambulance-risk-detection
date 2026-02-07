from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Smart Ambulance Risk API")

class VitalInput(BaseModel):
    heart_rate: float
    spo2: float
    motion: float

WINDOW = 60
hr_buffer = []
spo2_buffer = []
artifact_buffer = []

@app.post("/analyze")
def analyze_vitals(vitals: VitalInput):

    hr_buffer.append(vitals.heart_rate)
    spo2_buffer.append(vitals.spo2)

    if vitals.motion > 1.2 and vitals.spo2 < 94:
        artifact_buffer.append(1)
    else:
        artifact_buffer.append(0)

    if len(hr_buffer) > WINDOW:
        hr_buffer.pop(0)
        spo2_buffer.pop(0)
        artifact_buffer.pop(0)

    if len(hr_buffer) < WINDOW:
        return {
            "risk_score": 0.0,
            "anomaly": False,
            "confidence": 0.5
        }

    hr_trend = hr_buffer[-1] - hr_buffer[0]
    spo2_trend = spo2_buffer[-1] - spo2_buffer[0]

    risk = 0.0

    if hr_trend > 5:
        risk += 0.4

    if spo2_trend < -2:
        risk += 0.4

    artifact_ratio = sum(artifact_buffer) / len(artifact_buffer)
    risk = risk * (1 - artifact_ratio)

    anomaly = risk > 0.6

    return {
        "risk_score": round(risk, 2),
        "anomaly": anomaly,
        "confidence": round(1 - artifact_ratio, 2)
    }
