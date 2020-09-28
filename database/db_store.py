from .schema import Base, User

import uuid
import json
from datetime import datetime
import os
from sqlalchemy import create_engine, distinct, or_
from sqlalchemy.orm import sessionmaker

class DbStore(object):
    def __init__(self, **kwargs):
        if kwargs.get('db_type', 'postgresql') == 'mysql':
            host = kwargs.get('host', os.environ.get('DB_HOST', 'mysql-dc'))
            port = kwargs.get('port', os.environ.get('DB_PORT', '3307'))
            user = kwargs.get('user', os.environ.get('DB_USER', 'datacleaning'))
            database = kwargs.get('database', os.environ.get('DB_NAME', 'datacleaning'))
            password = kwargs.get('password', os.environ.get('DB_PASSWD', 'datacleaning'))

            db_connection_url = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
                user, password, host, port, database
            )
        elif kwargs.get('db_type', 'postgresql') == 'postgresql':
            host = kwargs.get('host', os.environ.get('DB_HOST', '192.168.100.103'))
            port = kwargs.get('port', os.environ.get('DB_PORT', '10202'))
            user = kwargs.get('user', os.environ.get('DB_USER', 'postgres'))
            database = kwargs.get('database', os.environ.get('DB_NAME', 'sugar2'))
            password = kwargs.get('password', os.environ.get('DB_PASSWD', 'postgres'))

            db_connection_url = 'postgresql://{}:{}@{}:{}/{}'.format(
                user, password, host, port, database
            )
        elif kwargs.get('db_type', 'postgresql'):
            db_connection_url = 'sqlite:///{}'.format(kwargs.get('file_path'))

        self._engine = create_engine(db_connection_url)
        self._sessionmaker = sessionmaker(bind=self._engine)
        self._session = None
        self._define_tables()

    def _define_tables(self):
        Base.metadata.create_all(bind=self._engine)

    def __enter__(self):
        self.connect()

    def connect(self):
        self._session = self._sessionmaker()

    def __exit__(self, exception_type, exception_value, traceback):
        self.disconnect()

    def commit(self):
        try:
            self._session.commit()
        except Exception as ex:
            raise ex
    
    def rollback(self):
        try:
            self._session.rollback()
        except Exception as ex:
            raise ex

    # Ensures that future database queries load fresh data from underlying database
    def expire(self):
        self._session.expire_all()

    def disconnect(self, commit=True):
        if self._session is not None:
            if commit:
                self._session.commit()
            else:
                self._session.rollback()
            self._session.close()
            self._session = None

    def get_user_by_id(self, user_id):
        return self._session.query(User).filter(User.id==user_id).one()