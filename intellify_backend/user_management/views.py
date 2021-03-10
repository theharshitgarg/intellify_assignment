from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK , HTTP_400_BAD_REQUEST
from rest_framework import permissions

from user_management.services import registration_services
from user_management.helpers import view_helpers
from user_management.exceptions import CustomException


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, requset):
        response = view_helpers.APIViewErrorResponse()
        http_code = HTTP_400_BAD_REQUEST

        try:
            service = registration_services.LogInService()
            data = service.login_customer(self.request.data)

            response = view_helpers.APIViewSuccessResponse()
            response.message = "User successfully logged in."
            response.data = data
            http_code = HTTP_200_OK

        except CustomException as err:
            http_code = HTTP_400_BAD_REQUEST
            response.update(**{"message": err.message,})

        return Response(response.json(), http_code)


class SignUpView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, requset):
        response = view_helpers.APIViewErrorResponse()
        http_code = HTTP_400_BAD_REQUEST

        try:
            service = registration_services.SignUpService()
            data = service.reigster_customer(self.request.data)

            response = view_helpers.APIViewSuccessResponse()
            response.message = "User registered successfully."
            http_code = HTTP_200_OK

        except CustomException as err:
            http_code = HTTP_400_BAD_REQUEST
            response.update(**{"message": err.message})

        return Response(response.json(), http_code)