from django.db import models
from apps.period.models import Period
from apps.candidate.models import Candidate
from sorl.thumbnail import ImageField
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete


class LotteryBill(models.Model):
    candidate = models.ForeignKey(
        Candidate, on_delete=models.CASCADE, related_name='lottery_bill')
    period = models.ManyToManyField(Period)
    bill_number = models.CharField(max_length=30)
    total_cost = models.IntegerField()
    image = ImageField(verbose_name='Image', upload_to='uploads/', blank=True)
    prize = models.CharField(max_length=19, blank=True,  null=True)
    is_draw = models.BooleanField(default=False)
    seller_number = models.IntegerField()


class Meta:
    verbose_name = ("Lottery_bill")
    verbose_name_plural = ("Lottery_bill")


def sorl_delete(**kwargs):
    delete(kwargs['file'])


cleanup_pre_delete.connect(sorl_delete)
