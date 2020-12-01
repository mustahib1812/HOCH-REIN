from rest_framework import status
from rest_framework.exceptions import APIException

from test_web_app.common import messages

class InternalServerError(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = messages.INTERNAL_SERVER_ERROR
    default_code = 'internal_server_error'

class UnknownColumnError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = messages.UNKNOWN_COLUMN
    default_code = 'unknown_column'

class DuplicateKey(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = messages.DUPLICATE_KEY
    default_code = 'duplicate_key'

