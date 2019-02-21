import os


def print_directory_content(path):
    """
    This function takes the name of a directory and prints out the paths files within that directory as well as any
    files contained in contained directories.
    (str) --> None

    """
    print(path)
    for child in os.listdir(path):
        child_path = os.path.join(path, child)
        if os.path.isdir(child_path):
            print_directory_content(child_path)
        else:
            print(child)


print_directory_content(os.getcwd())