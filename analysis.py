import pandas as pd
import matplotlib.pyplot as plt

# === Load & prep ===
df = pd.read_csv("data.csv")
df = df.fillna(0)

# KPIs per campaign
df["CTR"] = df["clicks"] / df["impressions"]
df["eCPM"] = (df["revenue"] / df["impressions"]) * 1000
total_impr = df["impressions"].sum()
df["Fill_Rate"] = df["impressions"] / total_impr

print("KPI Summary per campaign:")
print(df[["campaign_id", "source", "country", "CTR", "eCPM", "Fill_Rate"]].round(4))

# === Aggregations ===
by_source = df.groupby("source", as_index=False).agg(
    impressions=("impressions","sum"),
    clicks=("clicks","sum"),
    revenue=("revenue","sum"),
)
by_source["CTR"]  = by_source["clicks"] / by_source["impressions"]
by_source["eCPM"] = (by_source["revenue"] / by_source["impressions"]) * 1000

by_country = df.groupby("country", as_index=False).agg(
    impressions=("impressions","sum"),
    clicks=("clicks","sum"),
    revenue=("revenue","sum"),
)
by_country["CTR"]  = by_country["clicks"] / by_country["impressions"]
by_country["eCPM"] = (by_country["revenue"] / by_country["impressions"]) * 1000

print("\nBy source:")
print(by_source.round(4))
print("\nBy country:")
print(by_country.round(4))

# === Charts ===
# 1) CTR by campaign
plt.figure()
plt.bar(df["campaign_id"], df["CTR"])
plt.title("CTR by Campaign")
plt.xlabel("Campaign")
plt.ylabel("CTR")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("ctr_by_campaign.png")

# 2) eCPM by campaign
plt.figure()
plt.bar(df["campaign_id"], df["eCPM"])
plt.title("eCPM by Campaign")
plt.xlabel("Campaign")
plt.ylabel("eCPM")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("ecpm_by_campaign.png")

# 3) CTR by source
plt.figure()
plt.bar(by_source["source"], by_source["CTR"])
plt.title("CTR by Source")
plt.xlabel("Source")
plt.ylabel("CTR")
plt.tight_layout()
plt.savefig("ctr_by_source.png")

# 4) eCPM by country
plt.figure()
plt.bar(by_country["country"], by_country["eCPM"])
plt.title("eCPM by Country")
plt.xlabel("Country")
plt.ylabel("eCPM")
plt.tight_layout()
plt.savefig("ecpm_by_country.png")

print("\nSaved charts: ctr_by_campaign.png, ecpm_by_campaign.png, ctr_by_source.png, ecpm_by_country.png")
