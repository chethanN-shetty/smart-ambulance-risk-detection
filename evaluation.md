## – Alert Quality Metrics

The alerting system is evaluated using precision, recall, false alert rate, and alert latency.

Precision measures how many triggered alerts correspond to true patient deterioration. In an ambulance setting, moderate precision is acceptable as long as alerts are not excessively noisy.

Recall measures how many true deterioration events are successfully detected. Low recall is dangerous in emergency transport and is considered the most critical failure mode.

False alert rate represents how often alerts are triggered due to noise or artifacts. This system reduces false alerts by explicitly handling motion-induced SpO₂ artifacts before anomaly detection.

Alert latency measures how early the system raises an alert relative to the onset of deterioration. Earlier alerts with slightly lower confidence are preferable to delayed alerts in time-critical scenarios.

### – Failure Analysis

### Failure Case 1: Motion Masking True Deterioration
In cases where severe motion overlaps with genuine SpO₂ decline, artifact suppression may reduce sensitivity. This could delay detection of real hypoxia. A possible improvement would be multi-signal confirmation using heart rate and blood pressure trends.

### Failure Case 2: Slow Deterioration Below Trend Threshold
Very gradual physiological decline may not exceed the trend thresholds within the defined window. Increasing multi-window analysis or adaptive thresholds could reduce this risk.

### Failure Case 3: Sensor Dropout or Missing Data
Extended sensor dropout can reduce confidence and suppress alerts. Future versions should explicitly detect missing data segments and escalate alerts based on uncertainty rather than suppression alone.
