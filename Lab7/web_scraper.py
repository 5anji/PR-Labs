import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from time import sleep
import re

def find_last_page_number(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        page_link = soup.find("li", class_="is-last-page") and soup.find("li", class_="is-last-page").find("a")

        if page_link:
            page_url = page_link.get("href")
            page_number = int(page_url.split("=")[-1])

            return page_number

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    return None


prefix = 'https://999.md'
url = 'https://999.md/ro/list/real-estate/apartments-and-rooms'
pages_found = find_last_page_number(url)

def parse(local_url):
    response = requests.get(local_url)
    if response.status_code == 200:
        # print("URL: " + local_url)
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

def start_web_scraping(max_pages=find_last_page_number(url)):
    result = []
    if max_pages == 1:
        result.extend(parse(url))
    else:
        result.extend(parse(url + '?page=' + str(max_pages)))
        result.extend(start_web_scraping(max_pages - 1))
    return result
