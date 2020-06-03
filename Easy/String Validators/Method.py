#!/bin/python3
if __name__ == '__main__':
    s = input()
    #Bolean Variables
    isalphanumeric = False
    isalphabetical = False
    isdigit = False
    lowercase = False
    uppercase = False
    #Convert to list of chars
    a = list(s)
    #Validator loop
    for i in a:
        if i.isalnum():
            isalphanumeric = True
        
        if i.isalpha():
            isalphabetical = True
        
        if i.isdigit():
            isdigit = True

        if i.islower():
            lowercase = True

        if i.isupper():
            uppercase = True
    #Print Bolean Variables
    print( str(isalphanumeric) + "\n" + str(isalphabetical) + "\n" + str(isdigit) + "\n" + str(lowercase) + "\n" + str(uppercase))
