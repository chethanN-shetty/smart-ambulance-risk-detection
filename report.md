
The system is not based on predetermined vitals. Rather, it employs short-term trends and signal reliability to approximate patient risk.

Heart rate risk has been computed using an increasing trend within a 60-sec period. Constant rise means that there is a likelihood of physiological stress and not transient noise.

Cleaned SpO2 signal is used to compute SpO2 risk. A decreasing tendency during the same window shows the possibility of respiratory degradation.

The artifacts brought about by motion are explicitly identified at an earlier stage in the pipeline. The risk score is penalized to minimize false alerts in case the proportion of artifacts in the recent window is high.

The risk score is the final weighted score of heart rate trend and SpO2 trend which is adjusted with signal confidence. An anomaly alert gets raised when the risk score is beyond a conservative level and makes anomaly alerts resilient and clinically significant.

