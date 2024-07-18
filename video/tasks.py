import os
import subprocess


def convert_480p(source):
    base, ext = os.path.splitext(source)
    target = f"{base}_480px{ext}"
    cmd = ['ffmpeg', '-i', source, '-s', 'hd480', '-c:v', 'libx264', '-crf', '23', '-c:a', 'aac', '-strict', '-2', target]
    subprocess.run(cmd)