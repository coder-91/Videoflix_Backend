from django.contrib import admin

from video.models import Video


# Register your models here.
class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    search_fields = ['id', 'title', 'description']


# Register your models here.
admin.site.register(Video, VideoAdmin)