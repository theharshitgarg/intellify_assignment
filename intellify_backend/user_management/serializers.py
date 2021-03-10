from rest_framework import serializers

from user_management.models import Customer
from user_management.validators import name_validator, phone_validator, password_validator
from user_management.exceptions import UsernameAlreadyExistsException


class CustomerSignUpSerialaizer(serializers.Serializer):

    first_name = serializers.CharField(
        max_length=64, validators=[name_validator])
    last_name = serializers.CharField(
        max_length=64, validators=[name_validator])
    phone_number = serializers.CharField(
        max_length=16, validators=[phone_validator])
    email = serializers.EmailField()
    username = serializers.CharField(max_length=64)
    password = serializers.CharField(
        max_length=64, validators=[password_validator])

    def validate_username(self, value):
        user = Customer.objects.filter(user__username=value)

        if user.exists():
            raise UsernameAlreadyExistsException(value)

        return value


class CustomerLogInSerialaizer(serializers.Serializer):
    username = serializers.CharField(max_length=64)
    password = serializers.CharField(max_length=64)


class CustomerDetailsSerialaizer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        exclude = ('user',)
