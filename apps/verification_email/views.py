from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import ValidationError


from .models import VerificationEmail
from .serializers import VerificationEmailSerializer, CodeVerificationEmailSerializer

class VerificationEmailModelViewSet(ModelViewSet):
    queryset = VerificationEmail.objects.all()
    serializer_class = VerificationEmailSerializer
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = VerificationEmailSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Code sent successfully!'},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors)


class CodeVerificationModelViewSet(ModelViewSet):
    queryset = VerificationEmail.objects.all()
    serializer_class = CodeVerificationEmailSerializer

    def create(self, request, *args, **kwargs):
        serializer = CodeVerificationEmailSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            print(serializer)
            email = serializer.data.get('email')
            code = serializer.data.get('code')
            obj = VerificationEmail.objects.filter(code=code, email=email)
            if obj.exists():
                return Response({'message': 'Code exists!'},
                            status=status.HTTP_200_OK)
            return Response({'message': 'Code does not exist!'},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors)