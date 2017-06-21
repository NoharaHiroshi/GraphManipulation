# coding=utf-8

from ImagesSource.IconFont.base import engine, Base
from ImagesSource.IconFont.Model.icon_data import *

def create_all_table(engine):
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    create_all_table(engine)