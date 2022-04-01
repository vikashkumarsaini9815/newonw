from django.db import models

# Create your models here.

from django.db import models
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _
from .constants import PaymentStatus


class User(models.Model):
    name = models.CharField(max_length=255, null = True, blank = True)
    contact = models.CharField(max_length=12, unique=True)
    email = models.EmailField(null = True, blank = True)
    address = models.TextField(null = True, blank = True)
    join_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.contact

# class Amount_info(models.Model):
#     user = models.ForeignKey(User,on_delete = models.CASCADE, related_name="user")
#     amount = models.DecimalField(max_digits=20, decimal_places=2)
#     join_date = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return self.amount







class Order(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE, related_name="user")
    amount = models.FloatField(_("Amount"), null=False, blank=False)
    status = CharField(
        _("Payment Status"),
        default=PaymentStatus.PENDING,
        max_length=254,
        blank=False,
        null=False,
    )
    provider_order_id = models.CharField(
        _("Order ID"), max_length=40, null=False, blank=False
    )
    payment_id = models.CharField(
        _("Payment ID"), max_length=36, null=False, blank=False
    )
    signature_id = models.CharField(
        _("Signature ID"), max_length=128, null=False, blank=False
    )
    join_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.id}-{self.amount}-{self.status}"