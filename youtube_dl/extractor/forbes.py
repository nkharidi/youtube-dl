# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor

from .brightcove import BrightcoveNewIE


class ForbesIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?forbes\.com/video/(?P<id>[0-9]+)'
    _TEST = {
        'url': 'https://www.forbes.com/video/5118388570001',
        'md5': '7',
        'info_dict': {
            'id': '5118388570001',
            'ext': 'mp4',
            'title': 'Forbes CMO Interview: Kia\u2019s Michael Sprague',
            'description': 'COO and marketing chief talks Hamsters, Soul and why TV advertising still scores big for the brand.',
            # TODO more properties, either as:
            # * A value
            # * MD5 checksum; start the string with md5:
            # * A regular expression; start the string with re:
            # * Any Python type (for example int or float)
        }
    }

    def _real_extract(self, url):
        video_id = self._match_id(url)
        brightcove_url = "https://players.brightcove.net/2097119709001/598f142b-5fda-4057-8ece-b03c43222b3f_default/index.html?videoId=%s" % video_id
        return self.url_result(brightcove_url, BrightcoveNewIE.ie_key(), video_id)  # pass data to brightcove extractor
