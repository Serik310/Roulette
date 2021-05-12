from django.contrib import admin
from .models import BetHistory

class BetHistoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(BetHistory, BetHistoryAdmin)
