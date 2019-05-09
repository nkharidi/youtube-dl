# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor


class MindsIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?minds\.com/(?!newsfeed)'
    _TEST = {
        'url': 'https://www.minds.com/archive/view/715172106794442752',
        'md5': '496d4295d0e90ed27f05b222b2f7089e',
        'info_dict': {
            'id': '715172106794442752',
            'ext': 'mp4',
            'title': 'Direct Hit! Protester Hits Police Line with Molotov Cocktail! #Venezuela ',
            'description': 'I am an independent journalist that is always seeking out the truth. '
                           'I cover interesting topics and live stream events from the streets. '
                           'Stay Tuned for More! #MuchLove #Killuminati',
            'creator': 'DAHBOO7'
        }
    }

    def _real_extract(self, url):
        video_id = url.rsplit('/', 1)[-1]
        api_url = 'https://www.minds.com/api/v1/media/%s' % video_id
        website_data = self._download_json(api_url, video_id)
        video_urls = website_data.get('transcodes', {})
        keys = sorted(video_urls.keys())    # orders resolutions to automatically select highest one later
        title = website_data.get('title')
        for format_id in keys:  # selects highest quality
            video_url = video_urls[format_id]
        owner_object = website_data.get('ownerObj')
        creator = owner_object['username']
        description = owner_object['briefdescription']

        return {
            'id': video_id,
            'title': title,
            'url': video_url,
            'ext': 'mp4',
            'creator': creator,
            'description': description
        }
