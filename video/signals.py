import os

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from video.models import Video
from video.tasks import convert_480p


@receiver(post_save, sender=Video)
def video_post_save(sender, instance, created, **kwargs):
    print("video post saved")
    if created:
        print("New video created")
        convert_480p(instance.video_file.path)


@receiver(post_delete, sender=Video)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding Video object is deleted.
    """
    if instance.video_file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)