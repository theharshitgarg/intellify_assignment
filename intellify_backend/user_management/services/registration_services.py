from user_management.serializers import (
    CustomerSignUpSerialaizer, CustomerLogInSerialaizer,
    CustomerDetailsSerialaizer,
)
from user_management.models import Customer
from user_management.exceptions import CustomException
from rest_framework.exceptions import ValidationError as RestValidationError

class SignUpService():

    def validated_data(self, data):
        serializer = CustomerSignUpSerialaizer(data=data)
        serializer.is_valid(raise_exception=True)

        return serializer.validated_data

    def reigster_customer(self, data):
        validated_data = self.validated_data(data)

        try:
            validated_data = self.validated_data(data)

            auth_details = {
                "username": validated_data["username"],
                "password": validated_data["password"],
            }
            customer = Customer.create(**validated_data)
        
        except RestValidationError as err:
            raise CustomException("data", message="Invalid data")

        except KeyError as err:
            raise CustomException("data", message="Invalid request")
         
        return customer


class LogInService():

    def validate_data(self, data):
        serializer = CustomerLogInSerialaizer(data=data)
        serializer.is_valid(raise_exception=True)

        return serializer.validated_data

    def login_customer(self, data):
        

        try:
            validated_data = self.validate_data(data)
            customer = Customer.objects.get(user__username=validated_data["username"])
            
            is_valid = customer.user.check_password(validated_data["password"])
            
            if is_valid:
                return CustomerDetailsSerialaizer(customer).data
        
        except KeyError as err:
            raise CustomException("data", message="Invalid request")

        except RestValidationError as err:
            raise CustomException("data", message="Invalid data")

        return False

