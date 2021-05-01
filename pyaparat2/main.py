import requests

from scraper import Scraper


class Main:
    def __init__(self, url, quality):
        self.url = url
        self.quality = quality
        self.scraper = Scraper(self.url, self.quality)

    def download(self):
        video_url = str(self.scraper.get_link())
        video_name = video_url.split('/')

        video_name = video_name[4].split('?')
        with open(video_name[0], 'wb') as f:
            print('Downloading...')
            result = requests.get(video_url, stream=True)
            total = result.headers.get('content-length')

            if total is None:
                f.write(result.content)
            else:
                download = 0
                total = int(total)
                for data in result.iter_content(chunk_size=4096):
                    download += len(data)
                    f.write(data)
                    self.show_done(download, total)
        print('\n video downloaded ...')

    @staticmethod
    def show_done(downloaded_volume, size):
        done = int(50 * downloaded_volume / size)
        print('\r{}[{}{}]'.format(downloaded_volume, '=' * done,
                                  ' ' * (50 - done)), end='')


main = Main('https://www.aparat.com/v/Z3zdQ', '144')
main.download()
