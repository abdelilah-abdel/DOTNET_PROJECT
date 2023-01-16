import requests
from bs4 import BeautifulSoup

def scrape_links(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    links = soup.find_all('a')
    urls = []
    for link in links:
        link_url = link.get('href')
        urls.append(link_url)
    return urls

url = 'https://www.tripadvisor.com/Hotels-g304012-Asilah_Tanger_Tetouan_Al_Hoceima-Hotels.html'
urls = scrape_links(url)
for url in urls :
    print(urls)