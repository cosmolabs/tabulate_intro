#!usr/bin/python
"""
    
+----------------+-------------------------------------------------+
| Author:        | Ganesh Kuramsetti                               |
+----------------+-------------------------------------------------+
| Script Name:   | helper.py                                       |
+----------------+-------------------------------------------------+
| Date Created:  | Nov 28, 2021                                    |
+----------------+-------------------------------------------------+
| Description:   | An helper module for the tabulate intro script. |
+----------------+-------------------------------------------------+
| Language:      | Python                                          |
+----------------+-------------------------------------------------+
| Prerequisites: | None                                            |
+----------------+-------------------------------------------------+
| Instructions:  | None                                            |
+----------------+-------------------------------------------------+
| Date Updated:  | Nov 28, 2021                                    |
+----------------+-------------------------------------------------+

"""


def add_line_breaks(line: str, char_length: int):
    if type(line) is str:
        a_new_line = ""
        length_of_line = len(line)
        line_break_chars = char_length
        while line_break_chars < length_of_line:
            line = line[:line_break_chars].strip()  + "-\n-" + line[line_break_chars:].strip()
            line_break_chars = line_break_chars + char_length
        return line


def add_contents_to_a_file(contents_to_be_added, file_path):
    """
    This function adds contents to a file. It's so smart, that it can identity if
    the file exists or not before adding and prompts user to create if it doesn't.

    Args:
        contents_to_be_added (string): The tabulated intro that has to be added to the file.
        file_path (string): The path to the file including file name to add the intro.
    """
    # Verifying whether a file exists or not and if it's valid file or not.
    if io.exists(file_path) and io.isfile(file_path):
        # * prepending the contents to the file by reading
        # * and joining the new content and the old content
        with open(file_path, "r") as file:
            existing_file_content = file.readlines()
            existing_file_content.insert(0, contents_to_be_added)
        with open(file_path, "w") as intro_file:
            intro_file_content = "".join(existing_file_content)
            intro_file.write(intro_file_content)
        print("\nAdded intro to the file!!")
    # To check if path entered is a directory.
    elif io.isdir(file_path):
        print("\nEntered path is not a valid file. No intro !!")
    else:
        create_file = input("\nFile doesn't exists. Do you want to create a new file (Y or N)?: ")
        if create_file.upper() == "Y":
            with open(file_path, "w+") as intro_file:
                intro_file.write(contents_to_be_added)
            print("\nAdded intro to the file!!")
        else:
            print("\nNo intro!!")