from django.conf import settings

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


from rest_framework.renderers import TemplateHTMLRenderer

from django.template import loader
from test_web_app.helpers.add_details import post_details


class Details(APIView):
    """
    This class adds the details data into table

    Methods
    -------
    POST:
    Parameter : details

    """


    def post(self, request):
        """
        Method : POST
        Create new object in the test_details table.
        -------

        Parameters:
        Mandatory fields in json format.

        Returns:
        json: success message.

        """
        response = post_details(self,request)
        return response 