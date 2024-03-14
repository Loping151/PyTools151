# --------------------------------------------------------------------------------
# Author: Loping151
# GitHub: https://github.com/Loping151/pytools151
# Description: This repository contains a collection of Python tools designed to
#              enhance productivity and simplify various tasks. The code is open
#              for use and can be freely used, modified, and distributed.
# License: MIT License - Feel free to use and modify the code as you wish.
# --------------------------------------------------------------------------------
import os
import zipfile


def add_to_zip(zipfile_path, target_directory, condition_function=None, extension=None):
    """
    Add files to a zip archive based on a condition function.
    
    Args:
        zipfile_path (str): The path to the zip archive.
        target_directory (str): The directory containing the files to be added to the zip archive.
        condition_function (function): A function that takes a file name as input and returns a boolean.
        
    Example:
        >>> add_to_zip('test.zip', 'test', lambda x: x.endswith('.png'))
    """
    assert condition_function is not None or extension is not None, 'Either condition_function or extension must be provided'
    assert not (condition_function is not None and extension is not None), 'Only one of condition_function or extension can be provided'
    if extension is not None:
        condition_function = lambda x: x.endswith(extension)
    with zipfile.ZipFile(zipfile_path, 'w') as zipf:
        for foldername, _, filenames in os.walk(target_directory):
            for filename in filenames:
                if condition_function(filename):
                    file_path = os.path.join(foldername, filename)
                    zipf.write(file_path, os.path.relpath(file_path, target_directory))
                    

def walk_folder(root, extension=None, sort=False):
    """
    Walk through a folder and its subfolders to find files with a specific extension.
    If no extension is provided, all files will be listed.
    
    Args:
        root (str): The root directory to start the search.
        extension (str): The file extension to filter by.
        sort (bool): Whether to sort the list of files.
        
    Returns:
        list: A list of file paths.
    """
    matched_files = []

    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            if extension is None or filename.endswith(extension):
                matched_files.append(os.path.join(dirpath, filename))

    if sort:
        matched_files.sort()

    return matched_files
