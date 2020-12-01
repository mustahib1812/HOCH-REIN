import datetime
from django.conf import settings

from sqlalchemy import CHAR, Column, DECIMAL, Date, DateTime, Enum, Float, ForeignKey, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, INTEGER, LONGTEXT, MEDIUMTEXT, SMALLINT, TINYINT

from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Details(Base):
    __tablename__ = 'test_details'

    id = Column(INTEGER(), primary_key=True, autoincrement=True)
    details = Column(String(255), nullable=False, unique=True)