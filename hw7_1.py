import os, shutil

root = os.path.dirname(__file__)
high_folder = 'my_project'
folders = {'settings', 'mainapp', 'adminapp', 'authapp'}

try:
    exist_folders = set(os.listdir(os.path.join(root, high_folder)))
    folders_to_delete = exist_folders.difference(folders)
    if len(folders_to_delete) > 0:
        for folder in folders_to_delete:
            shutil.rmtree(os.path.join(root, high_folder, folder))
except FileNotFoundError as e:
    print('Директория создана.')

for folder in folders:
    if not os.path.exists(os.path.join(root, high_folder, folder)):
        os.makedirs(os.path.join(root, high_folder, folder))