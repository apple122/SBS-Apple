from django.contrib import admin
from .models import Period


class PeriodAdmin(admin.ModelAdmin):
    list_display = ['open_date', 'close_date',
                    'prize', 'period', 'is_special']
    fieldsets = (
        (None, {
            'fields': ['open_date', 'close_date', 'prize', 'period', 'is_special']
        }),
    )


admin.site.register(Period, PeriodAdmin)
