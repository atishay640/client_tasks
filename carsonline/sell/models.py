from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


class Car(models.Model):
    STATUS_CHOICES = [
        ('A', 'Available'),
        ('S', 'Sold'),
    ]

    YEAR_CHOICES = [(y, y) for y in range(1970, datetime.date.today().year+1)]

    make = models.CharField(max_length=50, blank=False, null=True)
    model = models.CharField(max_length=50, blank=False, null=True)
    year = models. PositiveSmallIntegerField(choices=YEAR_CHOICES)
    price = models.PositiveIntegerField(
        validators=[MinValueValidator(1000), MaxValueValidator(100000)])
    seller_name = models.CharField(max_length=30, blank=False, null=False)
    seller_mobile = models.CharField(max_length=13, blank=False, null=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A')
    currency = models.CharField(default="USD", max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.make} - {self.model}" 


class PurchaseOrder(models.Model):
    STATUS_CHOICES = [
        ('S', 'Success'),
        ('F', 'Failed'),
    ]
    car = models.ForeignKey(to=Car, on_delete=models.SET_NULL,
                            null=True, related_name='purchase_orders')
    buyer_name = models.CharField(max_length=30, blank=False, null=False)
    buyer_mobile = models.CharField(max_length=13, blank=False, null=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='S')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.buyer_name} - {self.car}" 