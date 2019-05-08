from __future__ import unicode_literals

from .common import InfoExtractor

import re


class NewsweekIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?newsweek\.com/'

    _TEST = {
        'url': 'https://www.newsweek.com/fortune-100-companies-list-federal-fund-399-billion-1417998',
        'md5': '3020300c06082a864886f70d020505000410',
        'info_dict': {
            'id': '1417998',
            'title': 'Fortune 100 Companies Received $399 billion in Federal Funding Over 4 Years'
        }
    }

    def _real_extract(self, url):

        video_id = url.rsplit('-', 1)[-1]
        website_data = self._download_webpage(url, video_id)
        video_url = re.findall(r'"contentUrl": "(.*?)"', website_data)
        title = re.findall(r'<title>(.*?)</title>', website_data)

        return {
            'id': video_id,
            'title': title[0],
            'url': video_url[0]
        }


