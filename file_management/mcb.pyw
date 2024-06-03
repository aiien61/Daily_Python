#! /usr/bin/env python3
# mcb.pyw - Saves and loads pieces of text to the clipboard
# Usage: python3 mcb.pyw save <keyword> - Saves clipboard to keyword
#        python3 mcb.pyw <keyword> - Loads keyword to clipboard
#        python3 mcb.pyw list - Loads all keywords to clipboard
#        python3 mcb.pyw delete <keyword> - Deletes keyword
#        python3 mcb.pyw delete - Deletes all keywords

import shelve, pyperclip, sys

mcb_shelf = shelve.open('mcb')

if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcb_shelf[sys.argv[1]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete' and sys.argv[2] in mcb_shelf.keys():
        del mcb_shelf[sys.argv[2]]
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        mcb_shelf.clear()
    elif sys.argv[1] in mcb_shelf.keys():
        pyperclip.copu(str(mcb_shelf[sys.argv[1]]))

mcb_shelf.close()