# Python Web Scraping
import requests
from bs4 import beautifulsoup

url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)
status = response.status_code
print(status)
