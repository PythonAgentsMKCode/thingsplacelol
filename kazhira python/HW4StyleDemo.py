#HW4Transform.py
#a module for transforming XML to HTML
#by Treyton Opocensky and 

#Starter Code:

def main():
    infile = open("WTExcerpt.xml","r",encoding="utf8")
    outfile = open("DemoWT.html","w",encoding="utf8")

    print("<html>\n<head>\n<title>Winter's Tale Demo</title>",file=outfile)
    print("<link rel='stylesheet' type='text/css' href='Shakespeare.css'>\n</head>\n<body>\n",file=outfile)
#test
    '''
    print("<h1>This is H1 formatting.</h1>\n",file=outfile)
    print("<h2>This is H2 formatting.</h2>\n",file=outfile)
    print("<h3>This is H3 formatting.</h3>\n",file=outfile)
    print("<h4>This is H4 formatting.</h4>\n",file=outfile)
    print("<p>This is p formatting.</p>\n",file=outfile)
    '''
#start
    '''
    text = infile.readline()
    while text !=" ":
        print(text)
        text = infile.readline()
    '''
#end

    print("</body>\n</html>",file=outfile)
    outfile.close

main()

'''
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
'''
