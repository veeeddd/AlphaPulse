import requests
from bs4 import BeautifulSoup
import time
import random
from config import TICKERS, NEWS_LIMIT

class AlphaScraper:
    def __init__(self):
        # Professional User-Agents to mimic different browsers
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        ]

    def get_headers(self):
        """Returns a random User-Agent to bypass basic bot detection."""
        return {"User-Agent": random.choice(self.user_agents)}

    def fetch_news(self, ticker):
        """Scrapes headlines for a specific ticker with jitter logic."""
        print(f"[*] Fetching news for: {ticker}")
        
        # JITTER: Random delay between 3-7 seconds to avoid rate limiting
        time.sleep(random.uniform(3, 7))
        
        url = f"https://www.google.com/search?q={ticker}+stock+news&tbm=nws"
        
        try:
            response = requests.get(url, headers=self.get_headers(), timeout=10)
            response.raise_for_status() # Raise error for 403/429 status
            
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extracting headline text from specific Google News tags
            headlines = [g.get_text() for g in soup.find_all('div', {'role': 'heading'})]
            
            return headlines[:NEWS_LIMIT]
        
        except Exception as e:
            print(f"[!] Error fetching {ticker}: {e}")
            return []

if __name__ == "__main__":
    scraper = AlphaScraper()
    # Test run for the first ticker in your config
    test_ticker = TICKERS[0]
    results = scraper.fetch_news(test_ticker)
    print(f"Found {len(results)} headlines for {test_ticker}:")
    for h in results:
        print(f"- {h}")