import requests
from bs4 import BeautifulSoup
import time
import random
from config import TICKERS, NEWS_LIMIT

class AlphaScraper:
    def __init__(self):
        # Rotating User-Agents to mimic different browsers
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"
        ]

    def get_headers(self):
        """Returns a random User-Agent header."""
        return {"User-Agent": random.choice(self.user_agents)}

    def fetch_news(self, ticker, retry_count=0):
        """
        Scrapes news headlines with Day 6 fault tolerance:
        - Recursive retry for 429 (Rate Limit) errors.
        - 60-second cooldown penalty.
        - Random jitter (5-10s).
        """
        if retry_count > 2:  
            print(f"[!] Max retries reached for {ticker}. Skipping.")
            return []

        print(f"[*] Fetching news for: {ticker} (Attempt {retry_count + 1})")
        time.sleep(random.uniform(5, 10))
        
        url = f"https://www.google.com/search?q={ticker}+stock+news&tbm=nws"
        
        try:
            response = requests.get(url, headers=self.get_headers(), timeout=15)
            
            if response.status_code == 429:
                print(f"[!] Rate limited (429) for {ticker}. Cooling down for 60s...")
                time.sleep(60) 
                return self.fetch_news(ticker, retry_count + 1)
                
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            headlines = [g.get_text() for g in soup.find_all('div', {'role': 'heading'})]
            
            valid_headlines = headlines[:NEWS_LIMIT]
            print(f"[OK] Successfully retrieved {len(valid_headlines)} headlines for {ticker}.")
            return valid_headlines
        
        except Exception as e:
            print(f"[!] Error fetching {ticker}: {e}")
            return []

if __name__ == "__main__":
    scraper = AlphaScraper()
    test_ticker = TICKERS[0]
    results = scraper.fetch_news(test_ticker)
    print(f"\nResults for {test_ticker}:")
    for idx, h in enumerate(results, 1):
        print(f"{idx}. {h}")