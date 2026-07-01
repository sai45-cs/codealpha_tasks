import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Unemployment in India.csv")

df.columns = df.columns.str.strip()

df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

print("Dataset Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSummary Statistics:")
print(df.describe())

avg_unemployment = df.groupby("Region")["Estimated Unemployment Rate (%)"].mean()

print("\nAverage Unemployment Rate by Region:")
print(avg_unemployment.sort_values(ascending=False))

plt.figure(figsize=(12, 6))
monthly_unemployment = df.groupby("Date")["Estimated Unemployment Rate (%)"].mean()
plt.plot(monthly_unemployment.index, monthly_unemployment.values)
plt.title("Average Unemployment Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.grid(True)
plt.show()

covid_period = df[df["Date"] >= "2020-03-01"]

plt.figure(figsize=(12, 6))
covid_monthly = covid_period.groupby("Date")["Estimated Unemployment Rate (%)"].mean()
plt.plot(covid_monthly.index, covid_monthly.values)
plt.title("Unemployment Rate During COVID-19")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.grid(True)
plt.show()

top_regions = avg_unemployment.sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
top_regions.plot(kind="bar")
plt.title("Top 10 Regions by Average Unemployment Rate")
plt.ylabel("Unemployment Rate (%)")
plt.show()