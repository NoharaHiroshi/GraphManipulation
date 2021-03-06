# coding=utf-8

import contextlib
import datetime
import time
import random
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, DateTime, text
from sqlalchemy.ext.declarative import declarative_base

cookie = 'EGG_SESS=e6hqBJuT__uHyIYJpkwc761g_WS8J_ECmGvD25nL3K0I5KwtfjOcIcVA6-uWX3R9iSMnxkNhYqp4O0i90NFqZNhy6ACyV3iY' \
         'Y3AR0Eu0ylIIa_PmQ46C88vmgnxy6DANGyE_nmOlA2G1bouqd9v3GgXFssTggBlTaUhoThL1GMuBKSh8D-16bmAPDG5elF4HuhSyHTQN2Y' \
         'Dh-VzaF4mc0Fs9BM8ytLKDLxoqUbLhOdGr8kTKo3UrMUls9jA3eOTcrpBDeoMnDuOvjCf3h_YtQguNzKuk9hmyVb8JWJm4VHPhZ1V082KI' \
         '3zV3qO1Ybrb6sjQFMuRNZsKrFtdS_fVz1Za0H6LNBZXvsEJxUy2_nYK8k7oCWCyxDOrrTjxnNJzxFyLemT2Z0VM7Fo2o1mrMFimzwkNUd' \
         'geRvbGZG51l9Ybi6n4VlzmGvFORQ9wXHIWG4tKm9xHAhqvcEY0hmRqwotLtR4DkwSWiDEu9u93uDTcbeD2FxraGFupIqN8lQM8sGM8F-P' \
         'OOzIp7O2JlH8Lxx52IOMeULZzYh2ti-Hd9JRH1LR2LpA5b5P1ZT_RJiy2Q9WRC37P21z6U9L2Tr1xCMCu4GTsf8ByeMVB3NYjcgn8EFLj' \
         'ZPyJt4x3jR0pZ_xxUixcSFbT2mPbbYjq4GtC5MwSeSBtdPxiTtwTumZdOm6HKdk_4hF_DFtuzmI1_Vng5jtgTSlOV3jD214eFrDaKp5TU' \
         'UCqIGvvjSID54ImybKJoj7P2UDQc-JZNYIlclnCH3bgqFVF6Tt6t_0BQyhaAPSq0xhUnej1oJWJnaFfNUa3Jo7pS8AWB8GEzQ5qy-piGcM' \
         '__Gahn1lNTPDnu-W6yW3FoXqW1f8vK3nxjI11ZAXWARH2ElSqgrlAowWBJHVJW8mwE276zwAocgU04nTbBvtpz-2E4DKxl_ubCWzyGgblM' \
         'SeVchuQasefEG7hHd7h3Z07Un1OplCtMY97SNB1sfbEgVAL1YJw6Ct3ApZBjhOyY1CXk5hvYSArL1XGC1v2bkCX1aWJN7XXRWsmZ-1EEtvE' \
         'I77i6fuE5ONPV7w-uPT576BI3v0D-LKTFj3oF0kki0lG2dfzeqZs6UW6oZX7LMsirzk1BSb963sjYR5BDlfdG4fJwKWNpEHJQs7pxSPJuB' \
         '3JXFX2PHOk5iP7Pmq-R6A==; UM_distinctid=15ad5d438f3184-0bc1f6a88-671b107a-1aeaa0-15ad5d438f49a6; CNZZDATA10' \
         '00158776=1015333910-1484289687-null%7C1493793808; l=AggI1TraSqZ9ypPUq-PdYrx1WHgORWyB; ctoken=mEKnXovYB9Ti5' \
         'P5Z8Pbyicon-font; cna=RHDcDoXo+nECAdrxqmpBN3kE; CNZZDATA1260547936=554937167-1493946988-null%7C1498030029;' \
         ' u=304428; isg=AsrKoy-Kp09dECug_1LX1X-rG7CsE3YUo0Qb81QDdp2oB2rBPEueJRBxY0Yh'

database_name = 'icon_font_source'
database_user = 'root'
database_password = '123456'
database_host = 'localhost'
database_src = 'mysql://%s:%s@%s/%s?charset=utf8' % (database_user, database_password, database_host, database_name)

engine = create_engine(
    database_src,
    echo=False,
    pool_recycle=3600,
    pool_size=5
)

Session = sessionmaker(bind=engine, autocommit=True)


@contextlib.contextmanager
def get_session(auto_commit=False):
    session = Session(autocommit=auto_commit)
    try:
        yield session
    except Exception as e:
        session.rollback()
        print 'CANT GET SESSION, ERROR: '
        print e
        raise
    finally:
        session.close()


class TBase(object):
    created_date = Column(DateTime, default=datetime.datetime.now)
    modified_date = Column(DateTime, default=datetime.datetime.now, onupdate=text('current_timestamp'))

Base = declarative_base(cls=TBase)


def id_generate():
    part_date = str(time.time())[:10]
    part_random = str(random.random())[-6:]
    u_id = int(''.join([part_date, part_random]))
    return u_id
