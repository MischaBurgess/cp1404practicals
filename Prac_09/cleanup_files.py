"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import os


def main():
    """Fix inconsistent file naming."""
    os.chdir('Lyrics')

    for directory_name, subdirectories, filenames in os.walk('.'):
        for file_name in filenames:
            new_name = clean_file_name(file_name)

            old_name = os.path.join(directory_name, file_name)
            new_name = os.path.join(directory_name, clean_file_name(file_name))
            os.rename(old_name, new_name)
            if new_name != old_name:
                print("Renaming {} to {}.".format(old_name, new_name))


def clean_file_name(file_name):
    """Return a correctly formatted filename."""
    new_name = ''

    for position, character in enumerate(file_name):
        if position == 0:
            new_name += file_name[position].upper()
        elif file_name[position].isupper() and file_name[position-1].islower():
            new_name += " " + character
        else:
            new_name += character
    new_name = new_name.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


main()
