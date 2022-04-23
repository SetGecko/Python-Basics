import os
path = r'C:\GDrive\GB\Learn\homework_7\sproject'
projectname = 'my_project'
folders = \
['settings',
 'mainapp',
 'adminapp',
 'authapp']

fullpath = os.path.join(path, projectname)
if not os.path.exists(fullpath):
    os.mkdir(fullpath)
for f in folders:
    folder = os.path.join(fullpath, f)
    if not os.path.exists(folder):
        os.mkdir(folder)
