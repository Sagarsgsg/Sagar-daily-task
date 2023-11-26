# How to works with directories and files in python#

import os  #used to intercat with operating sys#
os.mkdir('folder1)

#folder got created#
================================================================================================================
# How to read folders in c/n dir in python#

import os  #used to intercat with operating sys#
a = os.listdir('.')
print(a)

#0/p::-
#['folder1', 'Python Notes.txt', 'python.py', 'python.py.bak', 'sagu.txt', 'test.py']

===================================================================================================================
# Intract using path#

import os.path
x = os.path.exists('sagu.txt)
print(a)

#o/p::-
#True
===================================================================================================================                   
#delete the folder#

os.rmdir('folder1')
a = os.listdir('.')
print(a)

#o/p::-
['Python Notes.txt', 'python.py', 'python.py.bak', 'sagu.txt', 'test.py']
====================================================================================================================
#Remove the file from the directory#

a = os.remove('sagu.txt')
#Remove the  directory which contain file#
import shutil
shutil.rmtree('sam')
