#XMLtoHTML.py
#converts an XML document into an HTML document
#by Treyton Opocensky

def main():
    XML = open("WTExcerpt.xml","r")
    for line in XML.readlines():
        


    """
    read in XML document (by the line)
    print(out) <html>
    print(out) <link rel="stylesheet" href="Shakespeare.css">
    print(out) <body>
    if line[1] is t
        line.split[0] = <h1>
        line.split[1] is the h1 title
        line.split[2] = </h1>
    if line is <head>
        print(out) <h3>
    if line is </head>
        print(out) </h3>
    if line[1] is w
        line.split[1] is the word
    if line[1] is 'punctuation'
        line[4] is the mark
    """

main()
