from django.db import models
from apps.prize_type.models import PrizeType


class Prize(models.Model):

    prize_type = models.ForeignKey(
        PrizeType,  on_delete=models.CASCADE, related_name='Prize_type')
    prize = models.CharField(max_length=255)
    detail = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)


class Meta:
    ordering = ['-created_on']
    verbose_name = ("Prize")
    verbose_name_plural = ("Prizes")
