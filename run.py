# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 14:58:55 2021

@author: Anna Christiane
"""

# This program counts unique words from an English text file, treating hyphen and apostrophe 
# as part of the word. It prints the ten most frequent words and mentions the number of 
# occurrences.

# Run this program from the commmand line as
# $ python3 run.py <input_file>

import wordcounter
import sys


def writetofile(filename):
    wordcount_obj = wordcounter.WordCount(filename)
    wordcount_obj.get_result()


if __name__ == '__main__':
    try:
        input_file = sys.argv[1]
    except:
        input_file = str(input("Enter input file path: "))

    writetofile(input_file)
