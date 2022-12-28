from django.contrib import admin
from .models import Category,Product

# Register your models here.

class CategoryAdmin(admin.ModelAdmin): #ha class yasathi kela ki aplyala automated frontend sobt je disyla pahije te
    list_display = ('id', 'Category_name')# ya list_display mdhe lihale

class ProductAdmin(admin.ModelAdmin):
    list_display =('id','pname','price','description','size','qty','image','cat')


admin.site.register(Category,CategoryAdmin) #category table la categoryadmin sobt connect kele
admin.site.register(Product,ProductAdmin)#product table la productadmin sobt connect kele
