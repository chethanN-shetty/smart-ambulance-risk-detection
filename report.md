
The system does not rely on fixed thresholds for vitals. Instead, it uses short-term trends and signal reliability to estimate patient risk.

Heart rate risk is calculated based on a rising trend over a 60-second window. A sustained increase indicates possible physiological stress rather than momentary noise.

SpO₂ risk is calculated using the cleaned SpO₂ signal. A falling trend over the same window indicates potential respiratory deterioration.

Motion-induced artifacts are explicitly detected earlier in the pipeline. If a high percentage of artifacts are present in the recent window, the risk score is penalized to reduce false alerts.

The final risk score is a weighted combination of heart rate trend and SpO₂ trend, adjusted by signal confidence. An anomaly alert is triggered only when the risk score exceeds a conservative threshold, ensuring alerts are persistent and clinically meaningful.
