# Web Scraping
import requests
from bs4 import beautifulsoup

url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)
status = response.status_code
print(status)

# Using BeautifulSoup to parse content from the page
content = response.content
soup = beautifulsoup(content, 'html.parser')
print(soup.title)
print(soup.title.get_text())
print(soup.body)
print(soup.status_code)

tables = soup.find_all('table', {'cellpadding': '3'})

table = tables[0]
for td in table.find('tr').find_all('td'):
    print(td.text)