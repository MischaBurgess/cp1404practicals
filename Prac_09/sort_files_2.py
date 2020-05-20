"""sort files in FilesToSort, version 2"""

import os
import shutil
FOLDER_TO_SORT = 'FilesToSort'


def main():
    os.chdir(FOLDER_TO_SORT)
    files_to_sort = get_files_to_sort()
    extensions = get_extensions(files_to_sort)
    get_categories(extensions, files_to_sort)


def get_files_to_sort():
    """Gets a list of the files in the current directory."""
    try:
        files_to_sort = [f for f in os.listdir('.') if os.path.isfile(f)] # ignores folders
    except IsADirectoryError:
        print("Directory error - Could not find {} in directory".format(FOLDER_TO_SORT))
    return files_to_sort


def get_extensions(files_to_sort):
    """Gets extensions from list of unsorted files."""
    extensions = []
    for file in files_to_sort:
        extension = file.split('.')[-1]
        if extension not in extensions:
            extensions.append(extension)
        else:
            pass
    return extensions


def get_categories(extensions, files_to_sort):
    """Asks the user how to organise files."""
    for extension in extensions:
        category = input('What category would you like to sort {} files into? '.format(extension))
        try:
            os.mkdir(category)
        except FileExistsError:
            pass
        rearrange_files(files_to_sort, category, extension)


def rearrange_files(files_to_sort, category, extension):
    """Uses shutil module to rearrange files into their corresponding folder."""
    for file in files_to_sort:
        current_extension = file.split('.')[-1]
        if current_extension == extension:
            shutil.move(file, category)


main()
