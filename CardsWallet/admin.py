from django.contrib import admin
from CardsWallet.models import *
# Register your models here.
class CardsAdmin(admin.ModelAdmin):
    list_display = ['name_on_the_card','expiry_date','type','cvv','card_number','user']
    class Meta:
        model = Cards

admin.site.register(Cards,CardsAdmin)