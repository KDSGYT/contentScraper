# contentScraper
Get an email of all the video ideas daily with a report of the videos posted yesterday in your email.
contentScraper/
├── scraper/
│   ├── instagram.py
│   ├── tiktok.py
│   └── analytics.py
├── emailer.py
├── scheduler.py
├── config.py
└── main.py

# Function Workflow
1. Scrape new posts/videos.
2. Filter by your criteria.
3. Analyze video metrics for significant changes.
4. Compose and send an email report.

# Video Criteria
1. Views >= 5xFollowers
2. Viewer Retention>= 50%
3. Video length >= 15 seconds

# Todo
1. Install selected package
