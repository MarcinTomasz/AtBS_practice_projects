#Program to delete unwanted files.

import os

del_folder = input('What folder do you want to search for files to delete? ')
file_size = input('What size files do you want to delete (in MB)? ')


def del_large_files(del_folder, file_size):
    print('\nThese files will be deleted: ')
    for root, folders, files in os.walk(del_folder):
        for file in files:
            size = os.path.getsize(os.path.join(root, file)) * 10 ** 1 
            if int(file_size) > size:
                print(file, '| Path =', os.path.join(root, file))

del_large_files(del_folder, file_size)
