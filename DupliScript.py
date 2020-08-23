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


    """length = len(the_folder)
    mwanzo = 0
    same_name = 2
    while mwanzo <= length:
        for file in the_folder:
            if file == the_file:
                same_name = same_name + 1
        mwanzo = mwanzo + 1
        if same_name:
            return True
        else:
            return False """

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
        
    """ Searches through the folder to find if there's a file of the same size to the one passed """
    """sizes = []
    for file in files:
        sizes.append(os.stat(file).st_size)
    length = len(sizes)
    number_of_same = 0
    index = 0
    while index <= length:
        for file in files:
            if os.stat(file).st_size == sizes[index]:
                number_of_same = number_of_same + 1
        index = index + 1
    if number_of_same == 2:
        return True
    else:
        return False"""
                

def RemoveUnfinishedDownloads():
    """ Removes unfinished downloads which end with .part  """
    for file in files:
        if file.endswith('.part'):
            os.unlink(file)

files = os.listdir(os.getcwd())
            
def RemoveSameSized():
    """ Remove files with the same sizes. A major indicator of replication  """
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

files = os.listdir(os.getcwd())

def RemoveDuplicateDownloads():
    """ Removes Duplicate downloads. A download done more than once """
    SignOfDuplicateDownload = re.compile(r'\([0-9]\)\.')
    for file in files:
        if SignOfDuplicateDownload.search(file) is not None and FindIfSameSize(file) is True:
            os.unlink(file)


def RemoveTrailingDigits():
    """Go through every file. In each, if you find anything other than a letter at the beginning, remove it till you get to a letter, stop. Then rename it using os.rename function"""
    namelist = []
    for file in files:
        namelist.append(file)
    for file in files:
        found = re.findall(r'^[A-Za-z][a-zA-Z\.\-\(\)\,0-9\[\]\{\}\;\:@\s]+',file)
        natha = re.compile(r'[A-Za-z][a-zA-Z\.\-\(\)\,0-9\[\]\{\}\;\:@\s]+')
        if len(found) == 0:
            newname = natha.search(file).group(0)
            os.rename(file,newname)
files =  os.listdir(os.getcwd())


def RemoveDuplicatesDifferentNames():
    """ Removes files which have same names although cases might be different eg Yellow river.pm8 and yellow River.PM8  """
    for file in files:
        if FindIfSameName(file):
            os.unlink(file)

files = os.listdir(os.getcwd())
            
to_clean = input('You are about to clean the folder ' + str(os.getcwd()) + ' Are you sure? Y/N ')

if to_clean == 'Y':
    RemoveUnfinishedDownloads()
    RemoveDuplicateDownloads()
    RemoveTrailingDigits()
    RemoveSameSized()
    RemoveDuplicatesDifferentNames()
elif to_clean == 'N':
    sys.exit()
else:
    sys.exit()


files = os.listdir(os.getcwd())

  
