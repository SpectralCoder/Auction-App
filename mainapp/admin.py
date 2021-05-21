from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *
from django.urls import path

admin.site.site_header =" Taka School Auction Admin"
# Register your models here.
class adminview(admin.ModelAdmin):
    list_display =('proname','minbid', 'total_auction')
    list_filter = ('date',)
    def total_auction(self, obj):
        q=Item.objects.count()
        return q

    
    # def get_urls(self):
    #     urls= super().get_urls()
    #     custom_urls = [
    #         path('', self.adminhomeview),
    #     ]
    # def adminhomeview(self, request):
    #     print("okay")
admin.site.register(Item, adminview)


