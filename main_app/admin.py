from django.contrib import admin

from .models import Cat, Feeding

# Register your models here.
admin.site.register(Cat) # This will give us CRUD functionality for our Cat table in the admin app
admin.site.register(Feeding)