# coding=utf-8

from sqlalchemy import Column, Integer, String, Text, DateTime, BigInteger, Float
from ImagesSource.IconFont.base import Base


class IconData(Base):
    __tablename__ = 'icon_font_icon_data'

    icon_id = Column(BigInteger, primary_key=True)
        