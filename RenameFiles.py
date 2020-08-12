# -*-coding:utf-8 -*

import os
import sys

# Initialize for another try
retry = True

# List of all files in the folder selected
def file_list(fpath):
    file_names = []
    file_names = os.listdir(fpath) 
    for f in file_names:
        if os.path.isfile(os.path.join(fpath, f)):
            yield f

def rename_prefix(fpath):
    pre = input("What is the prefix to add? ")
    pre = str(pre).lstrip()
    for f in file_list(fpath):
        src = fpath + "/" + f
        dst = fpath + "/" + pre + f
        os.rename(src, dst)

def rename_suffix(fpath):
    suf = input("What is the suffix to add? ")
    suf = str(suf)
    for f in file_list(fpath):
        f_name, f_extension = os.path.splitext(f)
        src = fpath + "/" + f
        dst = fpath + "/" + f_name + suf + f_extension
        os.rename(src, dst)

# While retry = True
while retry:
    # Selection of the folder
    folder_path = input("Folder path: ")
    # print(folder_path)

    test_folder = True
    i = 0
    while test_folder:
        try:
            folder = os.listdir(folder_path)
            test_folder = False
        except FileNotFoundError:
            print("We cannot find the folder in the path specified.")
            folder_path = input("Folder path: ")
            i += 1
            if i == 2:
                sys.exit()
        

    # Print the list of all the files in the folder selected
    print("Here the list of all the files in the folder selected: ")
    for x in file_list(folder_path):
        print(x)

    question = input("Do you want to add a prefix (p), a suffix (s), or both (b)? - Select Q to quit.\nChoose between p, s or b: ")
    question = str(question)
    question = question.lower()
    question_bool = True

    i = 0
    while question_bool:
        if question == "p" or question == "s" or question == "b" or question == "q":
            if question == "p":
                print("You want to add a prefix.")
                question_bool = False
                rename_prefix(folder_path)
                print("Successfully rename!")
            if question == "s":
                print("You want to add a suffix.")
                question_bool = False
                rename_suffix(folder_path)
                print("Successfully rename!")
            if question == "b":
                print("You want to add a prefix and a suffix.")
                question_bool = False
                rename_prefix(folder_path)
                rename_suffix(folder_path)
                print("Successfully rename!")
            if question == "q":
                sys.exit()
        else:
            question = input("Please select between p, s, b or Q to quit: ")
            i += 1
            if i == 2:
                question_bool = False

    # Ask for another try to rename in another folder
    another = input("Do you want to rename another files? (y/n) ")
    another = str(another)
    another = another.lower()
    another_bool = True

    i = 0
    while another_bool:
        if another == "y" or another == "n":
            if another == "y":
                another_bool = False
                retry = True
            if another == "n":
                another_bool = False
                retry = False
        else:
            another = input("Select y for yes or n for no: ")
            i += 1
            if i == 2:
                sys.exit()

os.system("pause")
