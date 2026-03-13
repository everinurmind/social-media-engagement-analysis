# Social Media Fan Engagement Analysis

**Tools:** SQL · Python · pandas · Matplotlib · Seaborn  
**Author:** Nurbol Sultanov | [LinkedIn](https://www.linkedin.com/in/everinurmind/) | [GitHub](https://github.com/everinurmind)

---

## Project Overview

Analysis of 10,000+ social media posts across 5 platforms to identify engagement drivers, top-performing content types, and campaign effectiveness. Built to simulate a real-world fan engagement analytics workflow.

**Business Questions Answered:**
- Which platform drives the highest engagement rate?
- What content type performs best across campaigns?
- Which campaigns generate the most new followers?
- What are the monthly engagement trends across 2024?

---

## Dataset

- **Records:** 10,000 posts
- **Date range:** January 2024 – December 2024
- **Platforms:** Instagram, Facebook, YouTube, TikTok, Twitter
- **Metrics:** impressions, likes, comments, shares, saves, clicks, new followers, engagement rate

---

## Key Findings

| Metric | Result |
|---|---|
| Total impressions | 2.49 billion |
| Total new followers | 2.49 million |
| Avg engagement rate | 10.03% |
| Top platform | Instagram (10.22% avg engagement) |
| Top content type | Story & Image (10.06%) |
| Top campaign | NBA_Playoffs (10.10%) |
| Best combination | Instagram + Video (10.50%) |

---

## Project Structure
```
├── data/
│   ├── generate_data.py       # Dataset generation script
│   ├── social_media_data.csv  # Generated dataset (10,000 rows)
│   └── engagement_analysis.png # Visualization output
├── notebooks/
│   ├── analysis.py            # Python EDA + visualizations
│   ├── analysis.sql           # SQL queries
│   └── run_sql.py             # SQL execution via SQLite
└── README.md
```

---

## How to Run
```bash
# 1. Install dependencies
pip install pandas numpy matplotlib seaborn

# 2. Generate dataset
python data/generate_data.py

# 3. Run Python analysis + charts
python notebooks/analysis.py

# 4. Run SQL analysis
python notebooks/run_sql.py
```