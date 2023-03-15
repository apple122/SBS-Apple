from django.db import models
from apps.prize.models import Prize
from apps.period_type.models import PeriodType
# from .models import Period


class Period(models.Model):
    period = models.CharField(max_length=255)
    period_type = models.ForeignKey(
        PeriodType, on_delete=models.CASCADE, related_name='period')
    prize = models.ForeignKey(
        Prize, on_delete=models.CASCADE, related_name='period')
    open_date = models.DateTimeField(blank=True, null=True)
    is_special = models.BooleanField(default=False)
    close_date = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.period


class Meta:
    ordering = ['-created_on']
    verbose_name = ("Period")
    verbose_name_plural = ("Periods")
