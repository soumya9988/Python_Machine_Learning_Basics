import os

# return a string with a file path using the correct path separators.
full_path = os.path.join('Users', 'vedhoos', 'hobby_python_proj', 'automateboringstuff')
print(full_path)
print(full_path.split(os.path.sep))

# To get the path of current working directory
print(os.getcwd())

# To create a new directory
os.makedirs('/Users/vedhoos/hobby_python_proj/aa', exist_ok=True )

# Absolute file path & relative file path
print(os.path.abspath('basic_regex_2.py'))
print(os.path.isabs('/Users/vedhoos/hobby_python_proj/automateboringstuff/basic_regex_2.py'))
print(os.path.isabs('basic_regex_2.py'))
print(os.path.relpath('/Users/vedhoos/hobby_python_proj/automateboringstuff/basic_regex_2.py'))
print(os.path.abspath('.'))
print(os.path.abspath('../project_euler'))

# Returns the directory name and the basename
print(os.path.split('/Users/vedhoos/hobby_python_proj/automateboringstuff/basic_regex_2.py'))
print(os.path.dirname('/Users/vedhoos/hobby_python_proj/automateboringstuff/basic_regex_2.py'))
print(os.path.basename('/Users/vedhoos/hobby_python_proj/automateboringstuff/basic_regex_2.py'))
print('/Users/vedhoos/hobby_python_proj/automateboringstuff'.split(os.path.sep))

# Finding File Sizes and Folder Contents
print(os.listdir('/Users/vedhoos/hobby_python_proj/automateboringstuff'))
print(os.path.getsize('/Users/vedhoos/hobby_python_proj/automateboringstuff'))


