from xbmcswift2 import Plugin
from resources.lib import firingline


PLUGIN_URL = 'plugin://plugin.video.youtube/?action=play_video&videoid'
plugin = Plugin()


@plugin.route('/')
def main_menu():

    items = [
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('recent_episodes'),
            'thumbnail': 'https://i.ytimg.com/vi/ZupYLPhqcUY/maxresdefault.jpg',
        },
        {
            'label': plugin.get_string(30001),
            'path': plugin.url_for('episodes_by_playlist'),
            'thumbnail': 'https://cdn4.static.ovimg.com/m/03dztw/?width=1200',
        }
    ]

    return items


@plugin.route('/recent_episodes/')
def recent_episodes():
    url = 'https://www.youtube.com/user/firinglinevideos/videos'

    items = []

    content = firingline.get_latest_content(url)

    for i in content:
        items.append({
            'label': i['label'],
            'path': PLUGIN_URL + i['path'],
            'thumbnail': i['thumbnail'],
            'is_playable': True,
        })

    return items



if __name__ == '__main__':
    plugin.run()
