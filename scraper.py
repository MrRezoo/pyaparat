import requests
from bs4 import BeautifulSoup
import re

qualities = {

    '144': '0',
    '240': '1',
    '360': '2',
    '480': '3',
    '720': '4',
    '840': '4',
    '1080': '5',
}


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

    def get_qualities(self):
        links = self.get_all_link()
        qua = list(qualities.keys())
        available_qualities = list()

        for item in range(len(links)):
            available_qualities.append(qua[item])

        return available_qualities


s = Scrapper('https://www.aparat.com/v/1LV4i')

print(s.get_qualities())
