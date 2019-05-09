
from __future__ import unicode_literals

from .common import InfoExtractor


import re

class InfowarsIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www.)infowars.com/watch/'
    _TEST = {
        'url': 'https://www.infowars.com/watch/?video=5cd328a403b66e001274c5f4',
        'md5': '03ca7b1648af0cd437e978e7fba07ef3',
        'info_dict': {
            'id': '5cd328a403b66e001274c5f4',
            'ext': 'mp4',
            'title': '8May19 NYT “Audits” Trump: Adjusted Gross Lies'

        }
    }

    def _real_extract(self, url):
        video_id = url.rsplit('=', 1)[-1]
        webpage = self._download_webpage(url, video_id)
        video_url = re.findall(r'<meta property="og:video" content="(.*?)"/>', webpage)
        title = self._html_search_regex(r'<title>(.+?)</title>', webpage, 'title')

        return {
            'url': video_url[0],
            'ext': 'mp4',
            'title': title,
            'id': video_id,
        }