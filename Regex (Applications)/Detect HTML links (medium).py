#!/usr/bin/python3
import re

pattern_link = r'<a href="(.*?)".*?>(\s|<.*?>)?(.*?)<'
for i in range(int(input())):
    s = input()
    result = re.findall(pattern_link, s)
    if result is not None:
        for i in result:
            print(i[0] + "," + i[2])


"""
                So Let's break this jumble down :p
#Just a note that i don't know some of the HTML tags combinations so i had to unlock some test cases in order to understand

so the search pattern begins with (<a href=") to detect the beginning of the link tag Then appending the first group of .* to get whatever links of different chars in between the quotes and shoud stop at the first quote it meets ( ?)" ) then for the other attributes i just skipped it with .* which should stop at the fist > symbol it
meets using ( ?> ) then read whatever internal tags and spaces in between the <a> (<b>) name </a> tags like the <b> (as its existance will be optional using
( \s|<.*?>)? ) (the reson of <.*?> is there are tags that are more length of 1 char like <span> so the right solution is to look for all and stop at the first >)
and appending it to a second group just to avoid wrong translations then appending the third which contains the name and stop at the first open tag it meets
(.*?)<

#A small note: you should not end with the </a> as there might be internal attributes such as an internal close tag like </span> or even more annoying a <br> xd so just leave it as (a stop when meeting an open tag)

Using the classic checking for number of cases and importing the string in s variable, i used the findall function to find all links in one string as the cases may contain one or more links (or none but in this case it won't print a thing), so appending them in a list of tuples which then is imported to a for loop and extracting the important groups and get seperated by a ",". important groups are:
    i[0]: link
    i[2]: name

and bingo :D.
"""
