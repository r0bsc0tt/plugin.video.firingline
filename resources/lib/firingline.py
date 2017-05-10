from bs4 import BeautifulSoup as bs
import re
import requests


URL = "https://www.youtube.com"
CHANNEL_URL = "https://www.youtube.com/user/firinglinevideos/videos"


def get_latest_content(url):
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')
    content = soup.find_all('div', {'class': 'yt-lockup-dismissable'})

    output = []

    for i in content:

        label = i.find('h3', {'class': 'yt-lockup-title '})
        label = label.find('a').get('title')
        path_thumb = i.find('a')

        path = path_thumb.get('href')
        path = re.search(r'\=(.*)', path).group(0)

        thumbdiv = i.find('span', {'class': 'yt-thumb-default'} )
        thumb = thumbdiv.find('img').get('src')

        items = {
                'label': label,
                'path': path,
                'thumbnail': thumb,
            }

        output.append(items)

    return output


def get_playlist_content(url):
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')
    content = soup.find_all('tr', {'class': 'pl-video'})

    output = []

    for i in content:

        label = i.get('data-title')
        path_thumb = i.find('a')

        path = path_thumb.get('href')
        path = re.search(r'\=(.*)', path).group(0)

        thumb = i.find('img').get('src')
        thumb = 'https:' + thumb

        items = {
                'label': label,
                'path': path,
                'thumbnail': thumb,
            }

        output.append(items)

    return output


def get_playlists(url):
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')
    content = soup.find_all('li', {'class': 'channels-content-item'})

    output = []

    for i in content:

        currlink = i.find('a', {'class': 'yt-uix-tile-link'})
        label = currlink.get('title')
        path_thumb = i.find('a', {'class': 'yt-uix-sessionlink'})

        path = currlink.get('href')
        path = URL + path

        thumb = i.find('img').get('src')
        thumb = 'https:' + thumb

        items = {
                'label': label,
                'path': path,
                'thumbnail': thumb,
            }

        output.append(items)

    return output
