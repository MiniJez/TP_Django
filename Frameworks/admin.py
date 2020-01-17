from django.contrib import admin
from .models import Frameworks

# Register your models here.
class FrameworksAdmin(admin.ModelAdmin):
    list_display = ("name","language", "using_percentage")
admin.site.register(Frameworks, FrameworksAdmin)
