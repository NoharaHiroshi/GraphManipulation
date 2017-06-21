# coding=utf-8

import requests
import json
import sqlalchemy
from bs4 import BeautifulSoup as bs
from ImagesSource.session import get_session
from ImagesSource.base import *


class IconFontSource:
    def __init__(self):
        self.index_json_url = r'http://www.iconfont.cn/api/collections.json'
        self.params = {
            'type': 3,
            'page': 1,
            'ctoken': 'mEKnXovYB9Ti5P5Z8Pbyicon-font'
        }
        self.headers = {
            'Host': 'www.iconfont.cn',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
            'Referer': 'http://www.iconfont.cn/collections/index?type=3&page=2',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cookie': cookie
        }

    def get_index_info(self):
        result = {
            'response': 'ok',
            'info': ''
        }
        try:
            response = requests.get(self.index_json_url, params=self.params, headers=self.headers, timeout=30)
            content = json.loads(response.content)
            data = content.get('data', None)
            if data:
                count = data.get('count', 0)
                if count:
                    data_list = data.get('lists', None)
                    for data_info in data_list:
                        print data_info
        except requests.exceptions.ConnectTimeout:
            result.update({
                'response': 'fail',
                'info': 'response connected timeout'
            })
            return result
        except requests.exceptions.Timeout:
            result.update({
                'response': 'fail',
                'info': 'response connected timeout'
            })
            return result

if __name__ == '__main__':
    source = IconFontSource()
    source.get_index_info()
