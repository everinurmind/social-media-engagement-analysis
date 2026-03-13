-- =============================================
-- Social Media Fan Engagement Analysis
-- Author: Nurbol Sultanov
-- =============================================

-- 1. Total overview
SELECT
    COUNT(*)                        AS total_posts,
    ROUND(AVG(engagement_rate), 2)  AS avg_engagement_rate,
    SUM(impressions)                AS total_impressions,
    SUM(likes)                      AS total_likes,
    SUM(comments)                   AS total_comments,
    SUM(shares)                     AS total_shares,
    SUM(new_followers)              AS total_new_followers
FROM social_media_data;

-- 2. Engagement rate by platform
SELECT
    platform,
    COUNT(*)                        AS total_posts,
    ROUND(AVG(engagement_rate), 2)  AS avg_engagement_rate,
    SUM(new_followers)              AS total_new_followers,
    SUM(impressions)                AS total_impressions
FROM social_media_data
GROUP BY platform
ORDER BY avg_engagement_rate DESC;

-- 3. Engagement rate by content type
SELECT
    content_type,
    COUNT(*)                        AS total_posts,
    ROUND(AVG(engagement_rate), 2)  AS avg_engagement_rate,
    ROUND(AVG(likes), 0)            AS avg_likes,
    ROUND(AVG(shares), 0)           AS avg_shares
FROM social_media_data
GROUP BY content_type
ORDER BY avg_engagement_rate DESC;

-- 4. Campaign performance
SELECT
    campaign,
    COUNT(*)                        AS total_posts,
    ROUND(AVG(engagement_rate), 2)  AS avg_engagement_rate,
    SUM(clicks)                     AS total_clicks,
    SUM(new_followers)              AS total_new_followers
FROM social_media_data
GROUP BY campaign
ORDER BY avg_engagement_rate DESC;

-- 5. Top 10 posts by engagement
SELECT
    post_id,
    date,
    platform,
    content_type,
    campaign,
    impressions,
    likes,
    engagement_rate
FROM social_media_data
ORDER BY engagement_rate DESC
LIMIT 10;

-- 6. Monthly engagement trend
SELECT
    SUBSTR(date, 1, 7)              AS month,
    COUNT(*)                        AS total_posts,
    ROUND(AVG(engagement_rate), 2)  AS avg_engagement_rate,
    SUM(new_followers)              AS new_followers
FROM social_media_data
GROUP BY SUBSTR(date, 1, 7)
ORDER BY month;

-- 7. Best platform + content type combination
SELECT
    platform,
    content_type,
    COUNT(*)                        AS total_posts,
    ROUND(AVG(engagement_rate), 2)  AS avg_engagement_rate
FROM social_media_data
GROUP BY platform, content_type
ORDER BY avg_engagement_rate DESC
LIMIT 10;