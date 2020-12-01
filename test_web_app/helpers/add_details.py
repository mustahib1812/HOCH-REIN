from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.conf import settings
from django.http import HttpResponse
from django.db import IntegrityError


from test_web_app.models import Details


from .query_helper import get_raw_detail
from test_web_app.common import messages

# create a session for sql alchemy
session = settings.DB_SESSION

def post_details(self, request):

    try:
        details = request.data["details"]
        
        ex_details = get_raw_detail(details=details)

        if ex_details:
            return Response({
                            "success" : False,
                            "status_code" :status.HTTP_400_BAD_REQUEST,
                            "message" : messages.DUPLICATE_KEY,
                            "data" : None},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            if details and ex_details is None:
                add_details = Details(**request.data )
                session.add(add_details)
                session.commit()
                

                return Response({
                                "success" : True,
                                "status_code" :status.HTTP_201_CREATED,
                                "message" : messages.DETAILS_INSERTED,
                                "data" : None},
                                status=status.HTTP_201_CREATED)
            else:
                session.rollback()
                return Response({
                                "success" : False,
                                "status_code" :status.HTTP_400_BAD_REQUEST,
                                "message" : messages.DETAILS_NEEDED,
                                "data" : None},
                                status=status.HTTP_400_BAD_REQUEST)
    except IntegrityError as e:
        return Response({
                        "success" : False,
                        "status_code" :status.HTTP_400_BAD_REQUEST,
                        "message" : e,
                        "data" : None},
                        status=status.HTTP_400_BAD_REQUEST)