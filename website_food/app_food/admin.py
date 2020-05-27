from django.contrib import admin
from .models import Food, Recipes, User

admin.site.register(Food)
admin.site.register(User)
admin.site.register(Recipes)