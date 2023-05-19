from rest_framework import serializers

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'},
                                     write_only=True)

    class Meta:
        model = CustomUser
        fields = ('id',
                  'first_name',
                  'last_name',
                  'username',
                  'email',
                  'address',
                  'phone_number',
                  'password',
                  'qr_code')
        extra_kwargs ={

            'qr_code': {'read_only': True},
        }