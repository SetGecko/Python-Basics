import os
import shutil

ROOT_DIR = r"C:\GDrive\GB\Learn\homework_7\sproject"
TEMPLATE_DIR = r"C:\GDrive\GB\Learn\homework_7\sproject\template"


def move_template(filename):
    rel_filename = os.path.relpath(filename, os.path.dirname(os.path.dirname(filename)))
    rel_dirname = os.path.join(TEMPLATE_DIR, os.path.dirname(rel_filename))
    os.makedirs(rel_dirname, exist_ok=True)
    shutil.copy2(filename, os.path.join(rel_dirname, os.path.basename(filename)))


for root, dirs, files in os.walk(ROOT_DIR):
    if os.path.relpath(root, ROOT_DIR).startswith(r"template"):
        continue

    for file in files:
        if file.lower().endswith('.html'):
            move_template(os.path.join(root, file))
