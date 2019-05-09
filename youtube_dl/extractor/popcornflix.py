# coding: utf-8
from __future__ import unicode_literals
from .common import InfoExtractor
import re
class PopcornFlixIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)popcornflix.com/watch/channel/'
    # _TEST = {
    #     'url': 'https://www.popcornflix.com/watch/channel/new-releases/movie/18-jpxvh475xgqk-the-gift',
    #     'md5': 'TODO: md5 sum of the first 10241 bytes of the video file (use --test)',
    #     'info_dict': {
    #         'id': '42',
    #         'ext': 'mp4',
    #         'title': 'Video title goes here',
    #         'thumbnail': r're:^https?://.*\.jpg$',
    #     }
    #}

    def _real_extract(self, url):
          video_id = url.rsplit('/', 1)[-1]
          JSON_Url = ('https://api.unreel.me/oembed?url=%s' % url)
          JSON = self._download_json(JSON_Url, video_id)

          title = JSON.get('title')

          return {
              'url': url,
              'id': video_id,
              'title': title,
              # TODO more properties (see youtube_dl/extractor/common.py)
          }