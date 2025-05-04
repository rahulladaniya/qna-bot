import requests
from bs4 import BeautifulSoup
from logger import Logger
import traceback


class scrape_data:

    def __init__(self):
        self.logger = Logger.get_logger(self.__class__.__name__) 

    def scrape_url(self,url: str):
            
        try:

            self.logger.info(f"Scraping started for {url}")
            
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                self.logger.info(f"Fetched {url}")

            except Exception as e:
                e=traceback.format_exc()
                self.logger.error(f"Error fetching {url}: {e}")
                print(f"Error fetching {url}: {e}")
                return ""

            soup = BeautifulSoup(response.text, "html.parser")

            for script_or_style in soup(['script', 'style', 'noscript']):
                script_or_style.decompose()

            # Extract main content heuristically (prefer <article>, fallback to <body>)
            main_content = soup.find('article')
            if main_content is None:
                main_content = soup.body

            if main_content is None:
                print(f"Could not find main content in {url}")
                return ""

            # Get text, collapse whitespace
            text = main_content.get_text(separator=' ', strip=True)
            text = ' '.join(text.split())

            self.logger.info(f"text: {text} ")
            return text
        
        except Exception as e:
            e=traceback.format_exc()
            self.logger.error(f"Error scrapping {url}: {e}")
            print(f"Error in scrapping: {e}")
            return ""


obj_scrap_data=scrape_data()

# if __name__ == "__main__":
#     # Example usage
#     test_url = "https://www.freepressjournal.in/sports/itne-toh-virat-bhai-ke-paas-bhi-nahin-hain-nitish-rana-vaibhav-suryavanshi-engage-in-hilarious-chat-after-rr-vs-mi-ipl-2025-match-video"
#     content = scrape_url(test_url)
#     print(content)  # Print first 2000 chars for inspection