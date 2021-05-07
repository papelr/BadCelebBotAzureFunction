#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 17:02:23 2021

@author: robertpapel
"""

import os

# Function to delete all .jpg files from project directory
def remove_jpg():

    # script_dir = os.path.dirname(__file__)
    # rel_path = "/Users/robertpapel/Documents/bad_celeb_names_bot/"
    # abs_file_path = os.path.join(script_dir, rel_path)
    path = "./"
    for file in os.scandir(path):
        if file.name.endswith(".jpg"):
            os.unlink(file.path)

# Main function ----
if __name__ == '__main__':
    remove_jpg()