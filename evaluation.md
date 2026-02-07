## Alert Quality Metrics

Precision, recall, false alert rate, and alert latency are used as the measures of evaluation of the alerting system.

Precision is the proportion of patient deterioration that is being reported by the alerts being activated. In ambulance environment, moderate accuracy is agreeable provided that alerts are not too loud.

Recall defines the number of true deterioration events that are detected. The problem of low recall is perilous in emergency transportation and can be regarded as the most critical failure mode.

False alert rate: It is the frequency with which alerts are issued as a result of noise or artifact. This system minimizes false alerts through explicitly addressing motion induced SpO2 artifact, prior to anomaly detection.

The value of alert latency determines the timing of an alert of the system compared to the deterioration start. Precautionary measures that have a lower confidence level are better than delayed alerts in time-sensitive situations.

###  Failure Analysis

### Failure Case 1: Motion Masking True Deterioration
Artifact suppression can suppress sensitivity in a situation where severe motion is overlapping with true SpO2 fall. This may cause a postponement of actual hypoxia. Multi-signal confirmation based on heart rate and blood pressure trends would be a potential improvement.

### Failure Case 2: Slow Deterioration Below Trend Threshold
Slow physiological deterioration can lie within the trend limits in the set time frame. This risk could be minimized by increasing multi-window analysis or by changing the thresholds.

### Failure Case 3: Sensor Dropout or Missing Data
Long sensor drop out may decrease confidence and inhibit alerts. Future iterations must explicitly identify missing data segments and raise more alarm on basis of uncertainty and not by suppression alone.

