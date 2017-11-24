from django.contrib import admin

# Register your models here.
from .models import Info, Register

admin.site.register(Info)
admin.site.register(Register)
