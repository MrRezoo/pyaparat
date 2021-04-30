import requests
from bs4 import BeautifulSoup
import re


class Scrapper:
    def __init__(self, url, quality=None):
        self.url = url
        self.quality = quality

    def get_all_link(self):
        result = requests.get(self.url)
        content = BeautifulSoup(result.text, 'html.parser')
        video_links = content.find_all('a', href=re.compile('.mp4'))
        links = [link['href'] for link in video_links]
        return links


s = Scrapper('https://www.aparat.com/v/1LV4i')

print(s.get_all_link())
