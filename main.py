import asyncio
from playwright.async_api import async_playwright
from fake_useragent import UserAgent
import pandas as pd
import random
import time

# --- Configuration ---
TARGET_URL = 'https://quotes.toscrape.com/' # Demo site for practice
OUTPUT_FILE = 'data/scraped_data.csv'

async def scrape_data():
    print("🚀 Starting Anti-Detect Scraper...")
    
    # 1. Setup Fake User-Agent
    ua = UserAgent()
    user_agent = ua.random
    print(f"🎭 Using Fake User-Agent: {user_agent}")

    async with async_playwright() as p:
        # 2. Launch Browser (Headless=True for speed, False for debugging)
        browser = await p.chromium.launch(headless=True)
        
        # 3. Create Context with stealth settings
        context = await browser.new_context(
            user_agent=user_agent,
            viewport={'width': 1920, 'height': 1080}
        )
        page = await context.new_page()

        # 4. Navigate with random delay (Human behavior)
        print(f"🔗 Navigating to {TARGET_URL}...")
        await page.goto(TARGET_URL)
        await page.wait_for_timeout(random.randint(2000, 5000)) # Random wait 2-5s

        # 5. Extract Data (Example: Scrape Quotes)
        quotes = await page.locator('.quote').all()
        data_list = []

        print(f"📥 Found {len(quotes)} items. Extracting...")
        
        for quote in quotes:
            text = await quote.locator('.text').inner_text()
            author = await quote.locator('.author').inner_text()
            data_list.append({
                'Quote': text,
                'Author': author,
                'Scraped_At': time.strftime("%Y-%m-%d %H:%M:%S")
            })

        # 6. Save to CSV using Pandas
        df = pd.DataFrame(data_list)
        df.to_csv(OUTPUT_FILE, index=False)
        print(f"✅ Data saved to {OUTPUT_FILE}")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(scrape_data())
