from django.db import models
from django.contrib.auth.models import User

import uuid


class TimeStampModel(models.Model):
    """
    Timestamp Model which will be inherited by all the models.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Customer(TimeStampModel):
    CUSTOMER_ACTIVE_STATUS = 'active'
    CUSTOMER_INACTIVE_STATUS = 'inactive'

    CUSTOMER_STATUS_CHOICES = (
        (CUSTOMER_ACTIVE_STATUS, 'Active'),
        (CUSTOMER_INACTIVE_STATUS, 'Inactive'),
    )

    customer_id = models.UUIDField(
        default=uuid.uuid4, editable=False, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64, default='')
    phone_number = models.CharField(max_length=16)
    email = models.CharField(max_length=1024)

    status = models.CharField(
        max_length=16, default=CUSTOMER_ACTIVE_STATUS, choices=CUSTOMER_STATUS_CHOICES)

    def __str__(self):
        return self.user.username + " : " + self.phone_number

    @property
    def full_name(self):
        return ' '.join([self.first_name, self.last_name])

    @classmethod
    def create(cls, **kwargs):
        user_data = {key: kwargs[key] for key in ('first_name', 'last_name', 'email')}
        user_data["username"] = kwargs.pop('username')
        user, status = User.objects.get_or_create(**user_data)
        password = kwargs.pop('password')
        user.set_password(password)
        user.save()

        kwargs.update({"user": user})
        customer = cls(**kwargs)
        customer.user = user
        customer.save()

        return customer
