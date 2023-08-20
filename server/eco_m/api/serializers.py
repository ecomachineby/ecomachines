from django.contrib.auth import authenticate, login
from django.core.validators import RegexValidator
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

from service.models import Service


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs,):
        username = self.context['request'].data.get('username')
        password = self.context['request'].data.get('password')

        user = authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed('Invalid login credentials.')

        login(self.context['request'], user)
        return user


class RecoverPasswordSerializer(serializers.Serializer):
    message = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    phone = serializers.CharField(
        required=True,
        validators=[
            RegexValidator(
                regex=r"^\+\d{3}[\s\S]*\d{2}[\s\S]*\d{3}[\s\S]*\d{2}[\s\S]*\d{2}$",
                message="Phone number must be in the format: '+999999999999'.",
            )
        ],
    )
    organization = serializers.CharField(required=True)


class SenderSerializer(serializers.Serializer):
    message = serializers.CharField(required=True)
    email = serializers.EmailField(required=False)
    phone = serializers.CharField(
        required=False,
        validators=[
            RegexValidator(
                regex=r"^\+\d{3}[\s\S]*\d{2}[\s\S]*\d{3}[\s\S]*\d{2}[\s\S]*\d{2}$",
                message="Phone number must be in the format: '+999999999999'.",
            )
        ],
    )
    service = serializers.PrimaryKeyRelatedField(
        required=False,
        queryset=Service.objects.all(),
        error_messages={
            "does_not_exist": "Service with the given ID does not exist.",
            "incorrect_type": "Incorrect type. Expected a valid Service ID.",
        },
    )

    class Meta:
        fields = [
            "email",
            "phone",
            "service",
            "service_title",
            "message",
        ]



