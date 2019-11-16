import shutil
import os
import send2trash

# To copy one file to another
full_path_source = os.path.join(os.getcwd(), 'names_file.txt')
full_path_dest = os.path.join(os.getcwd(), 'names_file_2.txt')
dest_file = shutil.copy(full_path_source, full_path_dest)
print(dest_file)

# to copy an entire folder and every folder and file contained in it.
new_folder_dest = '/Users/vedhoos/hobby_python_proj/aaa'
new_folder_source = '/Users/vedhoos/hobby_python_proj/automateboringstuff'
shutil.copytree(new_folder_source, new_folder_dest)

# Moving and renaming a file from one folder to another
green_egg_n_ham = '/Users/vedhoos/hobby_python_proj/aa/green_eggs_and_ham.txt'
shutil.move(dest_file, green_egg_n_ham)

# Making and deleting a folder and file
temp_dir = '/Users/vedhoos/hobby_python_proj/temp_dir'
os.mkdir(temp_dir)
os.rmdir(temp_dir)
shutil.rmtree(new_folder_dest, ignore_errors=True)
os.unlink(green_egg_n_ham)

# This function will send the fill to recycle bin, which can be recovered later.
with open('test_for_send2trash.txt', 'w') as test_file:
    test_file.write('I am creating this file to test to delete it afterwards...')
send2trash.send2trash('test_for_send2trash.txt')

