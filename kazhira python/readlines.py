#readlines.py
#a module for transforming XML to HTML
#by Treyton Opocensky and 

#Starter Code:

def main():
    infile = open("Test.xml","r",encoding="utf8")
    outfile = open("DemoWT.html","w",encoding="utf8")

    print("<html>\n<head>\n<title>Winter's Tale Demo</title>",file=outfile)
    print("<link rel='stylesheet' type='text/css' href='Shakespeare.css'>\n</head>\n<body>",file=outfile)
    alltext = infile.readlines()
    text = infile.readline()

    for line in range(len(alltext)):
        line = line.split(" ")
        if line[0][1] == "t":
            theTitle = words[1:-1]
            theTitle = " ".join(theTitle)
            print("<h1>" + theTitle + "</h1>",file=outfile)
            
