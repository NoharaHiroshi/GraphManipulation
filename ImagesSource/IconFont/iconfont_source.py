# coding=utf-8

import json
import requests
from ImagesSource.IconFont.base import *
from ImagesSource.IconFont.Model.icon_data import IconData


class IconFontSource:
    def __init__(self, page):
        self.index_json_url = r'http://www.iconfont.cn/api/collections.json'
        self.params = {
            'type': 3,
            'page': page,
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
                        author = data_info.get('create_user_id', None)
                        desc = data_info.get('description', None)
                        series_name = data_info.get('name', None)
                        series_id = data_info.get('id', None)
                        slug = data_info.get('slug', None)
                        icons = data_info.get('icons', None)
                        if icons:
                            for info in icons:
                                store_icon(info, author, desc, series_name, series_id, slug)
                        else:
                            result.update({
                                'response': 'fail',
                                'info': 'can not get icons'
                            })
                            print result
                else:
                    result.update({
                        'response': 'fail',
                        'info': 'count is zero'
                    })
                    return result
            else:
                result.update({
                    'response': 'fail',
                    'info': 'can not get data'
                })
                return result
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


def store_icon(info, author, desc, series_name, series_id, slug):
    try:
        with get_session() as db_session:
            svg = info.get('show_svg', None)
            width = info.get('width', None)
            height = info.get('height', None)
            name = info.get('name', None)
            if svg:
                icon = IconData()
                icon.author = author
                icon.svg = svg
                icon.height = height
                icon.width = width
                icon.name = name
                icon.series_name = series_name
                icon.series_id = series_id
                icon.slug = slug
                icon.desc = desc
                db_session.add(icon)
                db_session.commit()
    except Exception as e:
        print e

if __name__ == '__main__':
    for page in range(1, 114):
        print '当前页数: %s' % page
        source = IconFontSource(page)
        source.get_index_info()
