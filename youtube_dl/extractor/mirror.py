# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor

import re


class MirrorIE(InfoExtractor):
    _VALID_URL = r'https?://.*?\.mirror\.co\.uk/(.*?)'
    _TEST = {
        'url': 'https://www.mirror.co.uk/tv/tv-news/who-won-dancing-ice-2019-14115379',
        'md5': 'b36b94250f6411836f01453b065971b8',
        'info_dict': {
            'id': '14115379',
            'ext': 'mp4',
            'title': 'James Jordan wins Dancing On Ice - and his reaction is very revealing',
            'description': '&#xa; Dancing On Ice viewers voted for James Jordan and pro partner Alexandra Schauman to be their surprise winners&#xa; ',
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
