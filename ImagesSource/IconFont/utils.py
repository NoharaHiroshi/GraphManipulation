# coding=utf-8

import os
import re
from ImagesSource.IconFont.base import get_session
from ImagesSource.IconFont.Model.icon_data import IconData

FILE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORE_PATH = os.path.join(FILE_PATH, 'IconFont\Icon')


def clean_file_name(file_name):
    file_name = re.sub(r"/|' '", '_', file_name)
    return file_name


def create_svg_file(file_name, content):
    try:
        with open(file_name, 'w') as f:
            f.write(content)
    except Exception as e:
        print e


def convert_svg_file():
    try:
        with get_session() as db_session:
            query = db_session.query(IconData).group_by(IconData.series_id).all()
            for icon_series in query:
                series_name = clean_file_name(icon_series.series_name)
                print series_name
                series_id = icon_series.series_id
                file_name_dir = os.path.join(STORE_PATH, '%s' % series_name)
                if not os.path.exists(file_name_dir):
                    os.mkdir(file_name_dir)
                icon_query = db_session.query(IconData).filter(
                    IconData.series_id == series_id
                ).all()
                if icon_query:
                    for icon_obj in icon_query:
                        name = clean_file_name(icon_obj.name)
                        icon_file_name = os.path.join(file_name_dir, '%s.svg' % name)
                        create_svg_file(icon_file_name, icon_obj.svg)
    except Exception as e:
        print e


if __name__ == '__main__':
    convert_svg_file()