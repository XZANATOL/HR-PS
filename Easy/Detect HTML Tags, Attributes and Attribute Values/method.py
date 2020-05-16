#!/usr/bin/python3
from html.parser import HTMLParser

class HTMLParse(HTMLParser):
    def handle_starttag(self, tag, attr):
        print(tag)
        if attr:
            for i in attr:
                string="-> "
                t=1
                for n in i:
                    string += str(n) + (" > "*t)
                    t-=1
                print(string)


parse = HTMLParse()
for i in range(int(input())):
    parse.feed(input())
