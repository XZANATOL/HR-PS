# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser


class pArser(HTMLParser):
    #this to obtain tags starts and it's attributes
    def handle_starttag(self, tag, attrs):
        print("Start : "+str(tag))
        for i in attrs:
            print("->",i[0],">",i[1])
                
    #this to obtain tags ends
    def handle_endtag(self, tag):
        print("End   : "+str(tag))
    
    #this to obtain empty tags (such as: br)
    def handle_startendtag(self, tag, attrs):
        print("Empty : "+str(tag))
        for i in attrs:
            print ('->',i[0],'>',i[1])
    
#creating object
parser = pArser()

#obtaining inputs
for i in range(int(input())):
    parser.feed(input())
