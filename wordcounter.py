# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 01:16:44 2021

@author: Anna Christiane
"""

# This file contains the WordCount class which takes a filepath.
# The get_result() method will call the other methods and print the ten most frequent words 
# mentioning the number of occurrences.

import processtext
import os


class WordCount():
    '''This class will call the processtext.py methods and print the result.
    '''

    def __init__(self, filepath=None):
        self.filepath = filepath
        self.file_content = None
        self.word_process = None
        self.word_dictionary = {}

    def validate_filepath(self, filepath=None):
        if filepath is not None and os.path.exists(filepath):
            self.filepath = filepath
            return
        if self.filepath is None or not os.path.exists(self.filepath):
            self.filepath = str(input("Enter proper file path: "))
            self.validate_filepath()
        else:
            return

    def get_file_content(self):
        '''This method will split the whole content of the text file by empty spaces and 
        return it as a list of strings.
        '''
        fobj = open(self.filepath).read()
        self.file_content = fobj.split()
        return self.file_content

    def call_processtext(self):
        '''Initializes the filetype specific class object, calls processtext method
        and returns a dictionary containing individual word counts.
        '''

        self.word_process = processtext.ProcessPlainTxt(self.file_content)
        return self.word_process.get_dict()

    def print_result(self):
        '''This method will sort the words in descending order of their number of 
        occurrences and print them on the screen.
        '''
        
        word_count_list = sorted(self.word_dictionary, key=self.word_dictionary.get, 
                                 reverse=True)
        for word in word_count_list[:10]:
            print(str(word)+" (" +str(self.word_dictionary[word])+")")
        

    def get_result(self, filepath=None):
        '''The primary method that does the work of calling the required
        methods of the class in the correct order to get the final required dictionary.
        If a filepath is passed with this method, it overwrites the content of
        self.filepath.
        '''
        
        self.validate_filepath(filepath)
        self.file_content = self.get_file_content()
        self.word_dictionary = self.call_processtext()
        self.print_result()
