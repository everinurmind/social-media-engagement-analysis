import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

random.seed(42)
np.random.seed(42)

platforms = ['Instagram', 'Twitter', 'Facebook', 'TikTok', 'YouTube']
content_types = ['Video', 'Image', 'Story', 'Reel', 'Post']
campaigns = ['Summer2024', 'NBA_Playoffs', 'NewSeason', 'FanEngagement', 'Merchandise']

rows = []
start_date = datetime(2024, 1, 1)

for i in range(10000):
    platform = random.choice(platforms)
    content = random.choice(content_types)
    campaign = random.choice(campaigns)
    date = start_date + timedelta(days=random.randint(0, 364))

    followers = random.randint(10000, 5000000)
    impressions = random.randint(1000, 500000)
    likes = int(impressions * random.uniform(0.02, 0.15))
    comments = int(likes * random.uniform(0.05, 0.2))
    shares = int(likes * random.uniform(0.01, 0.1))
    saves = int(likes * random.uniform(0.02, 0.12))
    clicks = int(impressions * random.uniform(0.01, 0.08))
    new_followers = random.randint(0, 500)

    engagement_rate = round((likes + comments + shares) / impressions * 100, 4)

    rows.append({
        'post_id': i + 1,
        'date': date.strftime('%Y-%m-%d'),
        'platform': platform,
        'content_type': content,
        'campaign': campaign,
        'followers': followers,
        'impressions': impressions,
        'likes': likes,
        'comments': comments,
        'shares': shares,
        'saves': saves,
        'clicks': clicks,
        'new_followers': new_followers,
        'engagement_rate': engagement_rate
    })

df = pd.DataFrame(rows)
df.to_csv('data/social_media_data.csv', index=False)
print(f"Dataset created: {len(df)} rows")
print(df.head())