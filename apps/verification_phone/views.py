from django.conf import settings
from django.http import HttpResponseBadRequest

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from twilio.rest import Client

from .serializer import PhoneNumberSerializer, VerifyPhoneNumberSerializer


class SendSMSView(APIView):
    @swagger_auto_schema(
        request_body=PhoneNumberSerializer,
        responses={
            status.HTTP_200_OK: openapi.Response("Success"),
            status.HTTP_400_BAD_REQUEST: openapi.Response("Bad request"),
        }
    )


    def post(self, requeest):
        phone_number = requeest.data.get('phone_number')
        if not phone_number:
            return Response({"message": "Phone number is required"},
                            status.HTTP_400_BAD_REQUEST)
        try:
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            client.verify.v2.services(settings.TWILIO_VERIFY_SERVICE_SID) \
                .verifications \
                .create(to=phone_number, channel="sms")
        except Exception as e:
            return Response({"message": e},
                            status.HTTP_400_BAD_REQUEST)
        return Response({"message": "SMS sent successfully"}, status.HTTP_200_OK)


class VerifyPhoneNumberView(APIView):
    @swagger_auto_schema(
        request_body=VerifyPhoneNumberSerializer,
        responses={
            status.HTTP_200_OK: openapi.Response("Success"),
            status.HTTP_400_BAD_REQUEST: openapi.Response("Bad request"),
        }
    )

    def post(self, request):
        phone_number = request.data.get('phone_number')
        verification_code = request.data.get('verification_code')
        if not phone_number or not verification_code:
            return Response(
                {"message": "phone_number or verification_code are required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            verification_check = client.verify \
                .services(settings.TWILIO_VERIFY_SERVICE_SID) \
                .verification_checks \
                .create(to=phone_number, code=verification_code)
            if verification_check.status == 'approved':
                return Response({'message': 'Phone number verified'},
                    status=status.HTTP_200_OK)

        except Exception:
                return Response({'message': "Invalid verification code"},
                        status=status.HTTP_400_BAD_REQUEST)