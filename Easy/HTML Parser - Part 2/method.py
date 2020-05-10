from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if "\n" in data:
            print(">>> Multi-line Comment\n"+str(data))
        else:
            print(">>> Single-line Comment\n"+str(data))
    
    def handle_data(self, data):
        if data != "\n":
            print(">>> Data\n"+str(data))
  
#obtaining inputs
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

#calling object
parser = MyHTMLParser()
parser.feed(html)
parser.close()