#!/bin/python3

import os

# Set the filename for parsing
filename = "NAMES.txt"

# Functions
def read_line_by_line(filename):
    # Reads a file line by line and to parse large files
    if os.path.exists(filename):
        file1 = open(filename, "r")
        while file1:
            # Some functions can be added on this step
            line1 = file1.readline()
            if line1 == "":
                break
            else:
                print(line1)
    else:
        print(f"file {filename} does not exists")

read_line_by_line(filename)
