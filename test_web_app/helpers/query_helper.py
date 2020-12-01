from test_web_app.models import Details
from test_web_app.helpers.serializer_helper import serialize_sqlalchemy

from sqlalchemy import exc, or_ , case, func
from sqlalchemy.orm import aliased
import logging
from django.conf import settings


# create a session for sql alchemy
session = settings.DB_SESSION

def get_raw_detail(details):
    """
    Returns a raw details object.

    Parameter:
    details: 

    Response:
    sqlalchemy object

    """
    try:
        raw_detail = session.query(Details).filter(Details.details==details).one_or_none()
        session.commit()
        raw_detail = serialize_sqlalchemy(raw_detail)
    except Exception as e:
        session.rollback()
        raw_detail = None

    return raw_detail