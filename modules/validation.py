#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

def check_isbn(string):
    """
    Return true if string passed is valid isbn.
    
    :param string: string to be checked
    :return: True if checked string is valid isbn
    """
    # Drop dashes from string and convert to lowercase in case of 10 being represented as X
    string = string.replace("-", "").lower()
    
    if len(string) == 10:
        # sum of all ten digits, each multiplied by its weight in ascending order from 1 to 10, is a multiple of 11.    
        w, p = 10, 0 # weight, product
        for char in string:
            if char is not "x":
                p += int(char)*w
                w -= 1
            if char is "x":
                p += 10*w
                w -= 1

        if p % 11 == 0: # multiple of 11 --> valid isbn-10
            return True
        else:
            return False
    
    if len(string) == 13:
        # the sum of all digits, each multiplied by its weight, alternating between 1 and 3, is a multiple of 10
        w, p = 1, 0 # weight, product
        for char in string:
            for char in string:
                if char is not "x":
                    p += int(char)*w
                    w = 4-w # subtraction from their total switches between 1 and 3        
                if char is "x":
                    p += 10*w
                    w = 4-w

        if p % 10 == 0: # multiple of 10 --> valid isbn-13
            return True 
        else:
            return False
        
def check_issn(string):
    """
    Return true if string passed is valid issn.
    
    :param string: string to be checked
    :return: True if checked string is valid issn
    """
    # Drop dashes from string and convert to lowercase in case of 10 being represented as X
    string = string.replace("-", "").lower()

    if len(string) == 8:
        # Sum of all ten digits, each multiplied by its weight in ascending order from 1 to 8, is a multiple of 11.
        w, p = 8, 0  # weight, product
        for char in string:
            if char is not "x":
                p += int(char)*w
                w -= 1
            if char is "x":
                p += 10*w
                w -= 1

        if p % 11 == 0: # product divisble by 11 --> valid issn
            return True
        else:
            return False

def check_sysno(string):
    """
    Return true if string passed is valid NTL system number.
    In case of this workflow it always begins with SIGLA + 9 numbers    
    
    :param string: string to be checked
    :return: True if checked string is valid system number
    """
    # TODO validate if such system number exists in library catalogue as well
    # String must conform to pattern
    repattern = '^ABA013-\d\d\d\d\d\d\d\d\d$'
    return re.match(repattern,  string)


def check_cnb(string):
    """
    Return true if string passed is valid CNB identifier    
    
    :param string: string to be checked
    :return: True if checked string is valid CNB
    """
    # TODO validate if such system number exists in library catalogue as well
    # String must conform to pattern
    repattern = '^cnb\d\d\d\d\d\d\d\d\d$'
    return re.match(repattern,  string)
