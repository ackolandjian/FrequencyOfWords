# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 15:05:01 2021

@author: Anna Christiane
"""

# This contains the class ProcessText and the subclass that is created
# for textfile type (currently only for txt).
# It performs the task of taking the content of the file passed and producing a dictionary
# containing the individual word count.
# This dictionary is returned to the caller.

# General patterns needed for removing the punctuations
st = "!#$%&()*+.,/:;<=>?@[\]^_`{|}~"
# maketrans is used to remove all of the punctutations that exist in String st 
# from a String word
translator = str.maketrans('', '', st)


class ProcessText:
    '''This is the base class inherited by the subclass for filetype txt.
    '''

    def __init__(self, filecontent):
        self.file_content = filecontent
        self.word_dictionary = {}
        self.word = None
        
    def split_word_to_list(self):
        '''This method will find punctuations inside a String word.
        It will remove punctuations and other symbols "@|!&*,”“:?.;\\[\]~`() 
        except hyphens and apostrophes between alpha characters from each word 
        (of type String, held by self.file_content). It will split each word at removed 
        punctuations into two or more words, depending on the number of punctuations.
        It returns the partitions of a word as a list called wordlist.
        '''
        
        wordlist = "".join((char if (char.isalpha() or char=="'" or char=='-') else " ") 
                                                for char in self.word).split()
        return wordlist
    
    def add_list_to_file_content(self,wordlist):
        '''This method will take the list of words returned by split_word_to_list(), 
        and add them, if they exist, to the original file_content.
        '''
        
        lengthoflist = len(wordlist)
        while (lengthoflist > 1):
            if (wordlist[1] != ""):
                lengthoflist = lengthoflist - 1
                self.word=wordlist[0]
                self.file_content.append(wordlist[1])

    
    def remove_punctuation(self):
        '''This method will remove punctuations and other symbols "@|!&*,”“:?.;\\[\]~`()
        except hyphens and apostrophes from each word that ends or starts with a 
        punctuation.
        '''
        
        self.word = self.word.translate(translator).lower()
    
    
    def counting_word(self):
        '''This method will find the count of a word in the word_dictionary
        and increment it.
        In case it's the first occurrence of the word, it returns 1.
        '''

        count = self.word_dictionary.get(self.word, 0)   #if not found returns 0, 
                                                    #else returns the saved value of count
        count += 1
        return count

    def get_dict(self):
        '''This method will call the methods in the proper order, remove punctuations 
        and other symbols from each word of the file (held by self.file_content).
        The symbols to be removed are defined in strip_parse_word().
        It returns a dictionary with the word counts of each unique word in the
        file.
        '''
        
        for self.word in self.file_content:
            wordlist = self.split_word_to_list()
            self.add_list_to_file_content(wordlist)
            self.remove_punctuation()
            #print(self.word)

            count = self.counting_word()
            self.word_dictionary[self.word] = count
        return self.word_dictionary
            


class ProcessPlainTxt(ProcessText):
    '''This class inherits from the ProcessText class and basically uses only
    the methods defined in that class
    '''

    def __init__(self, filecontent):
        super().__init__(filecontent)
