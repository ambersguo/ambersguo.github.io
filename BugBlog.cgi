#!/usr/bin/env python3

import cgi   # NEW

def main(): 
    form = cgi.FieldStorage()      

    age = form.getfirst("age", "0")
    fur = form.getfirst("fur", "")
    bones = form.getfirst("Bones", "")
    rice = form.getfirst("Rice", "")
    chicken = form.getfirst("Chicken", "")
    garlic = form.getfirst("Garlic", "")
    leek = form.getfirst("Leek", "")

    contents = processInput(age,fur,bones,rice,chicken,garlic,leek)   
    print(contents)
    
def processInput(age,fur,bones,rice,chicken,garlic,leek):  
    '''Process input parameters and return the final page as a string.'''
    result = ""
    age = int(age)
    if age == 2 and fur == "v2" and bones == "1" and rice == "1" and chicken == "1" and garlic != "1" and leek != "1":
        result = 'Congratulations! You know Bug very well!'
    else:
        result = 'Sorry! Please try again!'

    return fileToStr('BugBlog2.html').format(result)

# standard code for future cgi scripts from here on
def fileToStr(fileName): 
    """Return a string containing the contents of the named file."""
    fin = open(fileName); 
    contents = fin.read();  
    fin.close() 
    return contents

try:   # NEW
    print("Content-type: text/html\n\n")   # say generating html
    main() 
except:
    cgi.print_exception()                 # catch and print errors


