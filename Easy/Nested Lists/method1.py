#!/usr/bin/python3
if __name__ == '__main__':
    #defining some temp list variables
    lis = []
    l = []
    f = []
    t = []

    #obtaining and sorting inputs
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lis.append([name, score])

    #extracting and sorting grades
    for i in lis:
        l.append(i[1])
    l.sort()

    #determining the second lowest grade
    for i in l:
        if i> l[0]:
            t.append(i)
            if i != t[0]:
                t.pop()
                break

    #obtaining names of the second lowest grade and sorting them alphabetically
    for i in lis:
        if i[1] in t:
            f.append(i[0])
    f.sort()

    #printing names each in a line 
    for i in f:
        print(i)
    
"""
This method is based on grouping both name and corresponding grade in a nested list
then extracting the grades and determining the second lowest grade and saving the value in t
then searching in the list for the names whose index(1)/grade is in the list t
then printing the names alphabetically each in a newline

the benefit of this is that the method depends on fetching the name according to the value of the second lowest grade

i was thinking about making each names and grades in a seperate list but i will be forced to fetch for names according to the indexes of the the second lowest grade values, so i need to extract the indexes from the grades list and then extract each name using the extracted index and resort them (search using multiple values)

After re-evaluating, i think this method is more effiecent as i will compare a one value not a list of values/indexs to extract the names
"""
