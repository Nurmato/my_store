from django.contrib import admin
from market.models import Contact2
# Register your models here.
class ContactAdmin2(admin.ModelAdmin):
    list_display = ['email','name','address','message','sent_at']

    list_filter = ['sent_at']

    search_fields =  ['email','name','address','message','sent_at']

    # list_editable = ['address']
admin.site.register(Contact2, ContactAdmin2)
