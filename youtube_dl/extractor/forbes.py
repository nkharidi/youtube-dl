# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor

from .brightcove import BrightcoveNewIE


class ForbesIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?forbes\.com/video/(?P<id>[0-9]+)'
    _TEST = {
        'url': 'https://www.forbes.com/video/5118388570001',
        'md5': 'e0668a8d8ea2d2e52c84dca2387c6c20',
        'info_dict': {
            'id': '5118388570001',
            'ext': 'mp4',
            'title': 'Forbes CMO Interview: Kia\u2019s Michael Sprague',
            'description':
                'COO and marketing chief talks Hamsters, Soul and why TV advertising still scores big for the brand.',
            'uploader_id': '2097119709001',
            'upload_date': '20160909',
            'timestamp': 1473436985,
        }
    }

    def _real_extract(self, url):
        video_id = self._match_id(url)
        brightcove_url = \
            "https://players.brightcove.net/2097119709001/HJYQ1lY8Z_default/index.html?videoId=%s" % video_id
        return self.url_result(brightcove_url, BrightcoveNewIE.ie_key(), video_id)  # pass data to brightcove extractor
