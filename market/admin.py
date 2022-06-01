from django.contrib import admin
from market.models import Contact2
from market.models import Category, Product
# Register your models here.
class ContactAdmin2(admin.ModelAdmin):
    list_display = ['email','name','address','message','sent_at']

    list_filter = ['sent_at']

    search_fields =  ['email','name','address','message','sent_at']

    # list_editable = ['address']

class CategoryAdmin(admin.ModelAdmin):
    list_displey = ['name']
class ProductAdmin(admin.ModelAdmin):
    list_displey = ['name','price','category','description','image']

admin.site.register(Contact2, ContactAdmin2)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)