import os, shutil

root = os.path.dirname(__file__)
project_folder = 'my_project'
template_new_folder = os.path.join(root,project_folder,'templates')

for root, dirs, files in os.walk(project_folder):
    if root.find('templates') > 0:
        if len(dirs) != 0 and not os.path.exists(os.path.join(template_new_folder,dirs[0])):
            os.makedirs(os.path.join(template_new_folder,dirs[0]))
        if dirs == []:
            for file in files:
                src_file = os.path.join(root,file)
                dst_file = os.path.join(template_new_folder,os.path.split(root)[1],file)
                if not os.path.exists(os.path.join(template_new_folder,os.path.split(root)[1],file)):
                    shutil.copy2(src_file,dst_file)
