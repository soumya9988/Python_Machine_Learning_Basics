import os
import shutil

cur_work_dir = os.getcwd()
print(cur_work_dir)
destination_folder_name = '/Users/vedhoos/hobby_python_proj/aa'

for folderNames, subfolder, filenames in os.walk(cur_work_dir):
    for file in filenames:
        if file.endswith('.jpg'):
            source_file = os.path.join(cur_work_dir, file)
            print('Moving %s to %s....\n' % (source_file, destination_folder_name))
            shutil.move(source_file, destination_folder_name)

