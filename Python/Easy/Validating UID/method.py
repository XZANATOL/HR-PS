#!/bin/python3
def check(UUID):
    #count variables
    countrepeat=0
    countupper=0
    countdigit=0
    #check length
    if len(UUID) == 10:
        #check if alphanumeric
        if UUID.isalnum():
            #split into list to test each character
            UUID1 = list(UUID)
            for i in UUID1:
                #check if repeated (Invalid if repeated)
                if UUID.count(i) > 1:
                    countrepeat +=1
                #check if upper (for at least 2 upper char to be valid)
                if str(i).isupper():
                    countupper +=1
                #check if number (for at least 3 digits to be valid)
                if str(i).isnumeric():
                    countdigit +=1
            
            #check count variables values
            if countrepeat >1:
                return "Invalid"
            else:
                if countupper >= 2 and countdigit >= 3:
                    return "Valid"
                else:
                    return "Invalid"
        else:
            return "Invalid"
    else:
        return "Invalid"

#start of program
#get inputs
for i in range(int(input())):
    UUID = input()
    #validate UUID
    validation = check(UUID)
    #print validation boolean
    print(validation)
