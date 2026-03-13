import pandas as pd
import sqlite3

# Загружаем CSV в SQLite базу данных
df = pd.read_csv('data/social_media_data.csv')
conn = sqlite3.connect(':memory:')
df.to_sql('social_media_data', conn, index=False)

print("=== 1. TOTAL OVERVIEW ===")
print(pd.read_sql("""
    SELECT
        COUNT(*) AS total_posts,
        ROUND(AVG(engagement_rate), 2) AS avg_engagement_rate,
        SUM(impressions) AS total_impressions,
        SUM(likes) AS total_likes,
        SUM(new_followers) AS total_new_followers
    FROM social_media_data
""", conn))

print("\n=== 2. ENGAGEMENT BY PLATFORM ===")
print(pd.read_sql("""
    SELECT platform,
        COUNT(*) AS total_posts,
        ROUND(AVG(engagement_rate), 2) AS avg_engagement_rate,
        SUM(new_followers) AS total_new_followers
    FROM social_media_data
    GROUP BY platform
    ORDER BY avg_engagement_rate DESC
""", conn))

print("\n=== 3. ENGAGEMENT BY CONTENT TYPE ===")
print(pd.read_sql("""
    SELECT content_type,
        COUNT(*) AS total_posts,
        ROUND(AVG(engagement_rate), 2) AS avg_engagement_rate,
        ROUND(AVG(likes), 0) AS avg_likes
    FROM social_media_data
    GROUP BY content_type
    ORDER BY avg_engagement_rate DESC
""", conn))

print("\n=== 4. CAMPAIGN PERFORMANCE ===")
print(pd.read_sql("""
    SELECT campaign,
        COUNT(*) AS total_posts,
        ROUND(AVG(engagement_rate), 2) AS avg_engagement_rate,
        SUM(clicks) AS total_clicks,
        SUM(new_followers) AS total_new_followers
    FROM social_media_data
    GROUP BY campaign
    ORDER BY avg_engagement_rate DESC
""", conn))

print("\n=== 5. TOP 10 POSTS BY ENGAGEMENT ===")
print(pd.read_sql("""
    SELECT post_id, date, platform, content_type, campaign, engagement_rate
    FROM social_media_data
    ORDER BY engagement_rate DESC
    LIMIT 10
""", conn))

print("\n=== 6. MONTHLY TREND ===")
print(pd.read_sql("""
    SELECT SUBSTR(date, 1, 7) AS month,
        COUNT(*) AS total_posts,
        ROUND(AVG(engagement_rate), 2) AS avg_engagement_rate,
        SUM(new_followers) AS new_followers
    FROM social_media_data
    GROUP BY SUBSTR(date, 1, 7)
    ORDER BY month
""", conn))

print("\n=== 7. BEST PLATFORM + CONTENT COMBINATION ===")
print(pd.read_sql("""
    SELECT platform, content_type,
        COUNT(*) AS total_posts,
        ROUND(AVG(engagement_rate), 2) AS avg_engagement_rate
    FROM social_media_data
    GROUP BY platform, content_type
    ORDER BY avg_engagement_rate DESC
    LIMIT 10
""", conn))

conn.close()
print("\nSQL analysis complete.")