# 🕷️ Playwright Anti-Detect Scraper

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Playwright](https://img.shields.io/badge/Tool-Playwright-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

## 📖 Overview
This toolkit is a robust web scraping solution designed for **Business Intelligence (BI) data collection**. It utilizes `Playwright` (Async) to handle dynamic content rendering and implements basic anti-detect mechanisms to mimic human behavior.

Unlike traditional requests-based scrapers, this tool can handle JavaScript-heavy websites (e.g., SPAs) and avoid basic bot detection.

## 🚀 Features
- **Stealth Mode:** Rotates `User-Agent` strings automatically to reduce blocking risks.
- **Async Performance:** Uses Python's `asyncio` for high-concurrency scraping.
- **Human Mimicry:** Implements randomized delays and viewport simulation.
- **Data Export:** Automatically parses HTML/DOM and saves structured data to CSV.

## 🛠️ Project Structure

```text
├── data/
│   └── scraped_data.csv    # Output file
├── main.py                 # Core scraper logic (Async)
└── requirements.txt        # Dependencies
```

## 💻 Quick Start

### 1. Clone the repository
```bash
git clone [https://github.com/natecheung/playwright-scraper-toolkit.git](https://github.com/natecheung/playwright-scraper-toolkit.git)
cd playwright-scraper-toolkit
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Install Playwright Browsers
*Required for first-time use*
```bash
playwright install
```

### 4. Run the scraper
```bash
python main.py
```

## ⚠️ Disclaimer
This tool is for educational purposes and legitimate data collection only. Please respect the `robots.txt` of target websites and do not use for DDoSing.

## 📝 License
MIT License.
