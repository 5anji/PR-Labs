import requests
from bs4 import BeautifulSoup
import re

prefix = 'https://999.md'
url = 'https://999.md/ru/list/real-estate/apartments-and-rooms'

def parse(local_url):
    response = requests.get(local_url)
    if response.status_code == 200:
        print("Scrapping URL: " + local_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        links = []
        pattern = r'^/ro/\d{8}$'
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and re.match(pattern, href):
                links.append(prefix + href)

        return list(set(links))
    else:
        print(f"Failed to fetch the web page. Status code: {response.status_code}")

def recurse_pages(max_pages):
    result = []
    if max_pages == 1:
        result.extend(parse(url))
    else:
        result.extend(parse(url + '?page=' + str(max_pages)))
        result.extend(recurse_pages(max_pages - 1))
    return result


print(*recurse_pages(10), sep='\n')
