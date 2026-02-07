# Simulate 30 minutes of ambulance transport data
# Sampling rate: 1 Hz
# Includes:
# - normal transport
# - road-induced motion
# - gradual patient distress
# - sensor artifacts (motion-related)
# 0–10 min   : stable patient, city traffic
# 10–15 min  : rough road (motion spikes)
# 15–25 min  : patient starts deteriorating
# 25–30 min  : combined motion + distress



import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

np.random.seed(42)

seconds = 30 * 60
time = np.arange(seconds)
motion = np.zeros(seconds)
WINDOW = 30

hr = []
spo2 = []
spo2_clean = []
spo2_artifact = []
anomaly_flag = []
risk_score = []
bp_sys = []
bp_dia = []




for t in time:
    base = 72

    if t > 900:
        base += (t - 900) * 0.005

    m = np.random.normal(0, 0.05)

    if 600 < t < 900:
        m += np.random.uniform(0.5, 1.2)

    if np.random.rand() < 0.003:
        m += np.random.uniform(1.5, 3.0)

    motion[t] = max(0, m)

    noise = np.random.normal(0, 1.2)

    if m > 1.0:
        noise += np.random.randint(10, 20)

    spo2_base = 98 + np.random.normal(0, 0.3)

    if m > 1.2:
        spo2_base -= np.random.uniform(5, 12)

    if t > 900:
        spo2_base -= (t - 900) * 0.004

    spo2.append(max(85, spo2_base))

    is_artifact = False

    if m > 1.2 and spo2_base < 94:
        is_artifact = True

    if is_artifact:
        spo2_artifact.append(1)

        if len(spo2_clean) > 0:
            spo2_clean.append(spo2_clean[-1])
        else:
            spo2_clean.append(spo2_base)
    else:
        spo2_artifact.append(0)
        spo2_clean.append(spo2_base)

    bp_sys_base = 120 + np.random.normal(0, 3)
    bp_dia_base = 80 + np.random.normal(0, 2)

    if t > 900:
        bp_sys_base -= (t - 900) * 0.004
        bp_dia_base -= (t - 900) * 0.003

    if m > 1.2:
        bp_sys_base += np.random.uniform(-10, 10)
        bp_dia_base += np.random.uniform(-6, 6)

    bp_sys.append(bp_sys_base)
    bp_dia.append(bp_dia_base)




    hr.append(base + noise)


df = pd.DataFrame({
    "time_sec": time,
    "heart_rate": hr,
    "spo2_raw": spo2,
    "spo2_clean": spo2_clean,
    "spo2_artifact": spo2_artifact,
    "motion": motion,
    "bp_sys": bp_sys,
    "bp_dia": bp_dia
})
baseline_spo2 = df["spo2_clean"].iloc[:600].mean()

df.to_csv("data/patient_001.csv", index=False)

plt.figure(figsize=(12, 10))

plt.subplot(4, 1, 1)
plt.plot(df["time_sec"], df["heart_rate"], color="blue")
plt.ylabel("Heart Rate (bpm)")
plt.title("Vitals During Ambulance Transport")

plt.subplot(4, 1, 2)
plt.plot(df["time_sec"], df["spo2_raw"], color="green", alpha=0.5, label="Raw SpO2")
plt.plot(df["time_sec"], df["spo2_clean"], color="black", linewidth=2, label="Clean SpO2")
plt.ylabel("SpO2 (%)")
plt.legend()

plt.subplot(4, 1, 3)
plt.plot(df["time_sec"], df["motion"], color="orange")

plt.subplot(4, 1, 4)
plt.plot(df["time_sec"], df["spo2_artifact"], color="red")
plt.ylabel("Artifact Flag")
plt.xlabel("Time (seconds)")

plt.tight_layout()
plt.show()

for i in range(len(df)):
    if i < WINDOW:
        anomaly_flag.append(0)
        risk_score.append(0.0)
        continue

    hr_window = df["heart_rate"].iloc[i-WINDOW:i]
    spo2_window = df["spo2_clean"].iloc[i-WINDOW:i]

    hr_trend = hr_window.iloc[-1] - hr_window.iloc[0]
    spo2_trend = spo2_window.iloc[-1] - spo2_window.iloc[0]

    risk = 0.0
    # baseline SpO2 deviation check
    current_spo2 = df["spo2_clean"].iloc[i]

    if baseline_spo2 - current_spo2 > 2.5:
        risk += 0.4


    if hr_trend > 5:
        risk += 0.4

    if spo2_trend < -1.5:
        risk += 0.4

    recent_artifacts = df["spo2_artifact"].iloc[i-WINDOW:i].mean()
    risk *= (1 - recent_artifacts)

    risk_score.append(min(risk, 1.0))

    if risk > 0.4:
        anomaly_flag.append(1)
    else:
        anomaly_flag.append(0)

df["risk_score"] = risk_score
df["anomaly"] = anomaly_flag
baseline_spo2 = df["spo2_clean"].iloc[:600].mean()


alert_rate = df["anomaly"].mean()

stable_period = df[df["time_sec"] < 900]
false_alert_rate = stable_period["anomaly"].mean()

print("Alert Rate:", round(alert_rate, 3))
print("False Alert Rate (stable phase):", round(false_alert_rate, 3))


plt.figure(figsize=(12, 6))

plt.plot(df["time_sec"], df["heart_rate"], label="Heart Rate")
plt.plot(df["time_sec"], df["spo2_clean"], label="SpO2 Clean")

anomalies = df[df["anomaly"] == 1]
plt.scatter(
    anomalies["time_sec"],
    anomalies["heart_rate"],
    color="red",
    label="Anomaly",
    s=10
)

plt.xlabel("Time (seconds)")
plt.ylabel("Value")
plt.title("Early Anomaly Detection Based on Trends")
plt.legend()
plt.tight_layout()
plt.show()
