## Alert Quality Metrics

Precision, recall, false alert rate, and alert latency are used as the measures of evaluation of the alerting system.

Precision is the proportion of patient deterioration that is being reported by the alerts being activated. In ambulance environment, moderate accuracy is agreeable provided that alerts are not too loud.

Recall defines the number of true deterioration events that are detected. The problem of low recall is perilous in emergency transportation and can be regarded as the most critical failure mode.

False alert rate: It is the frequency with which alerts are issued as a result of noise or artifact. This system minimizes false alerts through explicitly addressing motion induced SpO2 artifact, prior to anomaly detection.

The value of alert latency determines the timing of an alert of the system compared to the deterioration start. Precautionary measures that have a lower confidence level are better than delayed alerts in time-sensitive situations.

###  Failure Analysis

### Failure Case 1: Motion Masking True Deterioration
In cases where severe motion overlaps with genuine SpO₂ decline, artifact suppression may reduce sensitivity. This could delay detection of real hypoxia. A possible improvement would be multi-signal confirmation using heart rate and blood pressure trends.

### Failure Case 2: Slow Deterioration Below Trend Threshold
Very gradual physiological decline may not exceed the trend thresholds within the defined window. Increasing multi-window analysis or adaptive thresholds could reduce this risk.

### Failure Case 3: Sensor Dropout or Missing Data
Extended sensor dropout can reduce confidence and suppress alerts. Future versions should explicitly detect missing data segments and escalate alerts based on uncertainty rather than suppression alone.

