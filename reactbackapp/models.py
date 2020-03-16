from django.db import models
from uuid import uuid4
from datetime import datetime
# Create your models here.
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

TYPES = (
       (1, _('Input')),
       (2, _('Output')),
   )


class MyUser(User):
    avatar = models.ImageField(null=True, blank=True, upload_to='staticfiles/upload/users')
    token = models.CharField(default=uuid4().hex, max_length=255, blank=True, null=True)


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='staticfiles/upload/products')
    created_at = models.DateTimeField(default=datetime.now, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.title)


class Operation(models.Model):
    quantity = models.SmallIntegerField(default=1)
    operation_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    operation_user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, null=True, blank=True)
    type = models.SmallIntegerField(choices=TYPES,null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{} of {} by {}".format(self.type, self.operation_product.title, self.operation_user.username )
