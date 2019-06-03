from django.contrib import admin

# Register your models here.
from pigpig.models import Taste, Cooking, Recipe

admin.site.register(Taste)
admin.site.register(Cooking)
admin.site.register(Recipe)