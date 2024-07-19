from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from video.models import Video


# Register your models here.
class VideoResource(resources.ModelResource):
    list_display = ['id', 'title', 'description']
    search_fields = ['id', 'title', 'description']

    class Meta:
        model = Video


@admin.register(Video)
class VideoAdmin(ImportExportModelAdmin):
    pass



