# coding=utf-8

from sqlalchemy import Column, Integer, String, Text, DateTime, BigInteger, Float
from ImagesSource.IconFont.base import Base, id_generate


class IconData(Base):
    __tablename__ = 'icon_font_icon_data'

    icon_id = Column(BigInteger, default=id_generate, primary_key=True)
    name = Column(String(30))
    svg = Column(Text, nullable=False)
    author = Column(String(30))
    desc = Column(String(100))
    series_name = Column(String(30))
    series_id = Column(String(30))
    slug = Column(String(100))
    width = Column(String(30))
    height = Column(String(30))

if __name__ == '__main__':
    pass