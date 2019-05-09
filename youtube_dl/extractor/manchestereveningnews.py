# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor

from .brightcove import BrightcoveNewIE

import re

class ManchesterEveningNewsIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?manchestereveningnews.co.uk/news/'
    _TEST = {
        'url': 'https://www.manchestereveningnews.co.uk/news/greater-manchester-news/moment-mcflys-danny-jones-surprises-16247191',
        'md5': 'd1f4229ce36196f8a8818f74e781d34d',
        'info_dict': {
            'id': '16247191',
            'ext': 'mp4',
            'title': "Moment McFly's Danny Jones surprises Pride of Manchester award winner on stage",
            'description' : '&#xa; Emma Harris was delighted at seeing McFly star Danny Jones on stage to present her with a Pride of Manchester award&#xa; '
        }
    }

    def _real_extract(self, url):
        video_id = url.rsplit('-', 1)[-1]
        webpage = self._download_webpage(url, video_id)
        brightcove_url = re.findall('<meta property="videoUrl" content="(.*?)">', webpage)
        title = re.findall('<meta property="og:title" content="(.*?)">', webpage)
        description = re.findall('<meta name="description" content="(.*?)">', webpage)

        return {
            'title': title[0],
            'url': brightcove_url[0],
            'id': video_id,
            'description': description[0]
            }