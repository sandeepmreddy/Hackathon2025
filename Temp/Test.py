import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

plt.rcParams["figure.figsize"] = (9,6)
df = pd.read_csv('~\Desktop\Archana\ec2_cpu_utilization.csv') # Downloaded from the link above
df.head()
anomalies_timestamp = [
        "2014-02-26 22:05:00",
        "2014-02-27 17:15:00"
    ]

df['timestamp'] = pd.to_datetime(df['timestamp'])

df.head()

df['is_anomaly'] = 1

for each in anomalies_timestamp:
    df.loc[df['timestamp'] == each, 'is_anomaly'] = -1
    
df.head()
