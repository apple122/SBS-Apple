from django.contrib import admin
from .models import LotteryBill
# from apps.period.models import Period


class LotteryBillAdmin(admin.ModelAdmin):

    list_display = ['is_draw', 'total_cost',
                    'seller_number', 'bill_number', 'candidate', "image", 'prize', ]
    fieldsets = (
        (None, {
            'fields': ['period', 'is_draw', 'total_cost',
                       'seller_number', 'bill_number', 'candidate', "image", 'prize',]
        }),
    )

    # def show_period(self, obj):
    #     return "\n".join([a.Period for a in obj.Period.all()])


admin.site.register(LotteryBill, LotteryBillAdmin)
