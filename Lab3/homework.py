import requests
from bs4 import BeautifulSoup
import re

def parse(local_url):
    print("Scrapping URL: " + local_url)
    response = requests.get(local_url)
    if response.status_code == 200:
        print("Response: OK")
        print("----------------------------")
        soup = BeautifulSoup(response.text, 'html.parser')

        product_details = []

        title = soup.find('h1').text.strip()
        product_details.append(f"Title: {title}")

        li_elements = soup.find_all('li', class_='m-value')
        for li in li_elements:
            key = li.find('span', class_='adPage__content__features__key').text.strip()
            value = li.find('span', class_='adPage__content__features__value').text.strip()

            product_details.append(f"{key}: {value}")

        return product_details
    else:
        print(f"Failed to fetch the web page. Status code: {response.status_code}")

print(*parse("https://999.md/ro/83066091"), sep='\n')
