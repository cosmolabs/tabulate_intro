#!usr/bin/python
"""
This Python script tabulates the intro and attaches to your script.
You can customize fields that you want to add to your script.
"""

"""
+---------------+---+---------------------------------------------------------------------------+
| Author        | : | Ganesh Kuramsetti                                                         |
+---------------+---+---------------------------------------------------------------------------+
| Script Name   | : | Script Intro                                                              |
+---------------+---+---------------------------------------------------------------------------+
| Date Created  | : | May 6th, 2021                                                             |
+---------------+---+---------------------------------------------------------------------------+
| Description   | : | A script that can frame and add intro's to any scripts in a table format. |
+---------------+---+---------------------------------------------------------------------------+
| Language      | : | python                                                                    |
+---------------+---+---------------------------------------------------------------------------+
| Prerequisites | : | python, tabulate module, and os module.                                   |
+---------------+---+---------------------------------------------------------------------------+
| Instructions  | : | Execute the script from terminal or from your preferred IDE.              |
+---------------+---+---------------------------------------------------------------------------+
| Date Modified | : | September 1st, 2021                                                       |
+---------------+---+---------------------------------------------------------------------------+
"""

# imports

from os import path as io
# importing tabulate module from lib folder
from lib.tabulate import tabulate  



def tabulate_intro_details(intro_details):
    """
    This function return the tabulated details of the list provided in grid format.

    Args:
        intro_details (list): Contains a list of key value pairs.

    Returns:
        string: returns a tabulated string with the input key value pairs.
    """    
    # ? More information on tabulate: https://pypi.org/project/tabulate/
    return tabulate(intro_details, tablefmt="grid", colalign=("left",))


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


# ! The start function
# ToDo: Fix the length of the column using line breaks
# ToDo: Store the entered details and ask for user verification.
def get_intro():
    print("\nEnter the below details: \n")
    # * Defining labels that has to be shown  into a list
    intro_labels = ["Author: ", "Script Name: ", "Date Created: ", "Description: ",
                    "Language: ", "Prerequisites: ", "Instructions: ", "Date Updated: "]
    # * using list comprehension
    intro_details = [input(label) for label in intro_labels]
    # * making use of zip function available. zip returns an iterator with tuples in it
    # * type casting the iterator to list 
    intro_details_ordered = list(zip(intro_labels, intro_details))
    script_intro = tabulate_intro_details(intro_details_ordered)
    save_to_file = input("\nDo you want to save the intro to a file? (Y or N): ")
    # Asking user to output into standard output or to a file.
    if save_to_file.upper() == "Y":
        file_path = input("\nEnter the path (including the file name): ")
        add_contents_to_a_file(script_intro, file_path)
    elif save_to_file.upper() == "N":
        print(script_intro)
    else:
        print("\nSelect Y or N, when asked for. No Intro !!!")

# Execute the below code block if this file run as a primary file.
if __name__ == '__main__':
    get_intro()