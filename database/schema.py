#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import Column, String, Float, ForeignKey, Integer, LargeBinary, DateTime, UniqueConstraint, BigInteger
import uuid
from datetime import datetime

Base = declarative_base()


def generate_uuid():
    return str(uuid.uuid4())


def generate_datetime():
    return datetime.utcnow()


class User(Base):
    __tablename__ = 'user_platform'

    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, unique=False, nullable=True)
    user_name = Column(String, unique=True, nullable=True)
    phone = Column(String, unique=True, nullable=True)
    email = Column(String, unique=True, nullable=True)
    sex = Column(Integer, nullable=True)
    age = Column(Integer, nullable=True)
    info = Column(String, nullable=True)
    password_hash = Column(LargeBinary, nullable=False)
    user_type = Column(Integer, default=1, nullable=False)
    banned_date = Column(DateTime, default=None, nullable=True)
    banned = Column(Integer, default=0, nullable=False)
    operator = Column(String, nullable=False)
    operate_date = Column(DateTime, default=None, nullable=False)
    create_date = Column(DateTime, default=None, nullable=False)
