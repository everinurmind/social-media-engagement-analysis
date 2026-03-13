import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ── 1. LOAD DATA
df = pd.read_csv('data/social_media_data.csv')
print("=== DATASET OVERVIEW ===")
print(f"Rows: {len(df)}")
print(f"Columns: {list(df.columns)}")
print(f"\nDate range: {df['date'].min()} to {df['date'].max()}")
print(f"\nMissing values:\n{df.isnull().sum()}")

# ── 2. ENGAGEMENT BY PLATFORM
print("\n=== AVG ENGAGEMENT RATE BY PLATFORM ===")
platform_eng = df.groupby('platform')['engagement_rate'].mean().sort_values(ascending=False).round(2)
print(platform_eng)

# ── 3. ENGAGEMENT BY CONTENT TYPE
print("\n=== AVG ENGAGEMENT RATE BY CONTENT TYPE ===")
content_eng = df.groupby('content_type')['engagement_rate'].mean().sort_values(ascending=False).round(2)
print(content_eng)

# ── 4. ENGAGEMENT BY CAMPAIGN
print("\n=== AVG ENGAGEMENT RATE BY CAMPAIGN ===")
campaign_eng = df.groupby('campaign')['engagement_rate'].mean().sort_values(ascending=False).round(2)
print(campaign_eng)

# ── 5. TOP PERFORMING POSTS
print("\n=== TOP 5 POSTS BY ENGAGEMENT RATE ===")
top_posts = df.nlargest(5, 'engagement_rate')[['post_id','platform','content_type','campaign','engagement_rate']]
print(top_posts)

# ── 6. NEW FOLLOWERS BY PLATFORM
print("\n=== TOTAL NEW FOLLOWERS BY PLATFORM ===")
followers = df.groupby('platform')['new_followers'].sum().sort_values(ascending=False)
print(followers)

# ── 7. VISUALIZATIONS
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Social Media Fan Engagement Analysis', fontsize=16, fontweight='bold')

# Plot 1 - Engagement by Platform
axes[0,0].bar(platform_eng.index, platform_eng.values, color='steelblue')
axes[0,0].set_title('Avg Engagement Rate by Platform')
axes[0,0].set_ylabel('Engagement Rate (%)')
axes[0,0].set_xlabel('Platform')

# Plot 2 - Engagement by Content Type
axes[0,1].bar(content_eng.index, content_eng.values, color='darkorange')
axes[0,1].set_title('Avg Engagement Rate by Content Type')
axes[0,1].set_ylabel('Engagement Rate (%)')
axes[0,1].set_xlabel('Content Type')

# Plot 3 - New Followers by Platform
axes[1,0].bar(followers.index, followers.values, color='seagreen')
axes[1,0].set_title('Total New Followers by Platform')
axes[1,0].set_ylabel('New Followers')
axes[1,0].set_xlabel('Platform')

# Plot 4 - Engagement Rate Distribution
axes[1,1].hist(df['engagement_rate'], bins=40, color='mediumpurple', edgecolor='white')
axes[1,1].set_title('Engagement Rate Distribution')
axes[1,1].set_xlabel('Engagement Rate (%)')
axes[1,1].set_ylabel('Number of Posts')

plt.tight_layout()
plt.savefig('data/engagement_analysis.png', dpi=150, bbox_inches='tight')
plt.show()
print("\nChart saved to data/engagement_analysis.png")