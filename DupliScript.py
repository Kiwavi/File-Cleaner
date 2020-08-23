#!/usr/bin/python3

import sys
import os
import re
import string

""" This script will pass through the /Muziki/roots folder and delete duplicate files. Tired of songs repeating themselves. It is supposed to rename files beginning with digits removing the digits, remove one if two files have the same size in terms of kilobytes, remove files ending with .part(means they were partially downloaded), remove files with (1). or any other number since it means they are just copies of others,"""

files = os.listdir(os.getcwd())

def FindIfSameName(the_file):
    """ This function finds if there's another name that's similar to the file that's been passed """
    all_files_lower = []
    same_name = 0
    for file in files:
        all_files_lower.append(file.lower())
    for file in all_files_lower:
        if file == the_file.lower():
            same_name = same_name + 1
    if same_name == 2:
        return True
    else:
        return False

def FindIfSameSize(the_file):
    """ This function finds if there's another file with the same size as the one passed to it """
    size_of_file = str(os.stat(the_file).st_size)
    sizes = []
    for file in files:
        size_of_one = str(os.stat(file).st_size)
        sizes.append(size_of_one)
    number_of_same = 0
    for size in sizes:
        if size == size_of_file:
            number_of_same = number_of_same + 1
    if number_of_same == 2:
        return True
    else:
        return False

def RemoveUnfinishedDownloads():
    """ Removes unfinished downloads which end with .part  """
    try:
        for file in files:
            if file.endswith('.part'):
                os.unlink(file)
    except FileNotFoundError:
        pass
    
def RemoveSameSized():
    """ Remove files with the same sizes. A major indicator of replication  """
    try:
        listsizes = []
        for file in files:
            listsizes.append(os.stat(file).st_size)
        length = len(listsizes)
        song_index = 0
        while song_index >= length:
            for file in files:
                if FindIfSameSize(file) is True:
                    os.unlink(file)
        song_index = song_index + 1
    except FileNotFoundError:
        pass

def RemoveDuplicateDownloads():
    """ Removes Duplicate downloads. A download done more than once """
    try:
        SignOfDuplicateDownload = re.compile(r'\([0-9]\)\.')
        for file in files:
            if SignOfDuplicateDownload.search(file) is not None and FindIfSameSize(file) is True:
                os.unlink(file)
    except FileNotFoundError:
        pass

def RemoveTrailingDigits():
    """Go through every file. In each, if you find anything other than a letter at the beginning, remove it till you get to a letter, stop. Then rename it using os.rename function"""
    try:
        namelist = []
        for file in files:
            namelist.append(file)
        for file in files:
            found = re.findall(r'^[A-Za-z][a-zA-Z\.\-\(\)\,0-9\[\]\{\}\;\:@\s\'\"\&\%\~\_]+',file)
            natha = re.compile(r'[A-Za-z][a-zA-Z\.\-\(\)\,0-9\[\]\{\}\;\:@\s\'\"\&\%\_\~]+')
            if len(found) == 0:
                newname = natha.search(file).group(0)
                os.rename(file,newname)
    except FileNotFoundError:
        pass
            
def RemoveDuplicatesDifferentNames():
    """ Removes files which have same names although cases might be different eg Yellow river.pm8 and yellow River.PM8  """
    try:
        for file in files:
            if FindIfSameName(file):
                os.unlink(file)
            else:
                break
    except FileNotFoundError:
        pass

            
to_clean = input('You are about to clean the folder ' + str(os.getcwd()) + ' Are you sure? Y/N ')

if to_clean == 'Y':
    RemoveUnfinishedDownloads()
    files = os.listdir(os.getcwd())
    RemoveDuplicateDownloads()
    files = os.listdir(os.getcwd())
    RemoveTrailingDigits()
    files = os.listdir(os.getcwd())
    RemoveSameSized()
    files = os.listdir(os.getcwd())
    RemoveDuplicatesDifferentNames()
    files = os.listdir(os.getcwd())
elif to_clean == 'N':
    sys.exit()
else:
    sys.exit()



  
