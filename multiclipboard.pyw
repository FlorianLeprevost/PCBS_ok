# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 07:50:34 2019

@author: install
"""

#import shelve
#shelfFile = shelve.open('mydata')
#cats = ['Zophie', 'Pooka', 'Simon']
#shelfFile['cats'] = cats
#shelfFile.close()

    
#! python3
   # mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
   #        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
   #        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys
mcbShelf = shelve.open('mcb')

   # TODO: Save clipboard content.
 # Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
   # TODO: List keywords and load content.
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    if sys.argv[2] in mcbShelf:
        mcbShelf[sys.argv[2]] = []
    elif sys.argv[2] =="all":
        mcbShelf =[]

mcbShelf.close()