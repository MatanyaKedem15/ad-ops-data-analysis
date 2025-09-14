# Ad Ops – Data Analysis with Python

A small, **realistic** Ad Ops demo for a sports app context.  
It loads campaign-level data (in-app / web / push, multiple countries), cleans it with **Pandas**, and computes **CTR, Fill Rate, eCPM**.  
Includes grouped views by **source** and **country**, plus simple charts.

## Why this project
- Show hands-on skills in **Pandas**, **NumPy**, and **matplotlib**.
- Demonstrate **Ad Ops KPIs** and how to turn raw CSV into actionable insights.
- Personalised to ad operations in a sports app (campaign names, sources, countries).

## Data
`data.csv` contains columns:
- `campaign_id` – e.g., `Maccabi_TLV_Live`, `EU_Football_Highlights`
- `source` – `in-app`, `web`, `push`
- `country` – `IL`, `UK`, `US`, `DE`, `ES`
- `impressions`, `clicks`, `revenue`

## KPIs
- **CTR** = `clicks / impressions`
- **Fill Rate** = `impressions / total_impressions`
- **eCPM** = `(revenue / impressions) * 1000`

## How to run
```bash
pip install -r requirements.txt
python analysis.py
