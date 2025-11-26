import pandas as pd

df = pd.read_csv("mental_health_data.csv")
print(df['treatment'].value_counts())
print(df['treatment'].value_counts(normalize=True))
