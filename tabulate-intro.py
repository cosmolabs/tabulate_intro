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
from .helper import add_contents_to_a_file
from .helper import add_line_breaks



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


# ! The start function
# ToDo: Store the entered details and ask for user verification.
def get_intro():
    print("\nEnter the details: \n")
    # * Defining labels that has to be shown  into a list
    intro_labels = ["Author: ", "Script Name: ", "Date Created: ", "Description: ",
                    "Language: ", "Prerequisites: ", "Instructions: ", "Date Updated: "]
    # * using list comprehension
    intro_details = [input(label) for label in intro_labels]
    # * making use of zip function available. zip returns an iterator with tuples in it
    # * type casting the iterator to list 
    intro_details_formatted = []
    for a_detail in intro_details:
        intro_details_formatted.append(add_line_breaks(a_detail, 80))
    intro_details_ordered = list(zip(intro_labels, intro_details_formatted))
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