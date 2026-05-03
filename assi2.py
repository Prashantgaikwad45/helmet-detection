import pandas as pd
import numpy as np

df = pd.read_csv("fifa.csv")

avg_age = np.mean(df['Age'].values)
print("Average Age:", avg_age)