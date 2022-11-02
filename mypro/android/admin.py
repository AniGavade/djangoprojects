from django.contrib import admin

# Register your models here
from .models import BwksStudents
@admin.register(BwksStudents)
class Classadmin(admin.ModelAdmin):
    class Meta:
        model=BwksStudents
        fields="__all__"
        