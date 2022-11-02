from django.contrib import admin

# Register your models here.
from .models import Song,Singer

@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display=["name","gender"]

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display=["song_title","singer","relation"]