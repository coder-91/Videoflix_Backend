# TODO Script schreiben, mit der man mit einem Befehl alle Dateien importieren / exportieren kann.

# Ausführen mit python manage.py my_script
from video.admin import VideoResource

dataset = VideoResource().export()
# dataset.json > Datei.txt