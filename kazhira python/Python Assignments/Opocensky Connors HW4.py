#HW4Transform.py
#a module for transforming XML to HTML
#by Treyton Opocensky and Jimmy Connors

def main():
    infile = open("WTExcerpt.xml","r",encoding="utf8")
    outfile = open("DemoWT.html","w",encoding="utf8")

    print("<html>\n<head>\n<title>Winter's Tale Demo</title>",file=outfile)
    print("<link rel='stylesheet' type='text/css' href='Shakespeare.css'>\n</head>\n<body>",file=outfile)
    text = infile.readline()
    text = infile.readline()
    words = text.split(" ")
    if words[0][1] == "t":
        theTitle = words[1:-1]
        theTitle = " ".join(theTitle)
        print("<h1>" + theTitle + "</h1>",file=outfile)
    while text != "":
        text = infile.readline()
        words = text.split(" ")
        if "<head>" in text and "</head>" not in text:
            print("<h3>",file=outfile)
        if "</head>" in text:
            print("</h3>",file=outfile)
        if "<stage>" in text and "</stage>" not in text:
            print("<h4>",file=outfile)
        if "</stage>" in text:
            print("</h4>",file=outfile)
        if "<sp>" in text and "</sp>" not in text:
            print("<p>",file=outfile)
        if "</sp>" in text:
            print("</p>",file=outfile)   
        if "<speaker>" in text and "</speaker>" not in text:
            print("<h2>",file=outfile)
        if "</speaker>" in text:
            print("</h2>",file=outfile)
        if words[0] == "<w>":
            if "</w>" in words[1]:
                print(words[1][0:int(len(words[1])-5)],file=outfile)
            else:
                print(words[1],file=outfile)
        if "<pc>" in text:
            print(text[4],file=outfile)
    print("</body>\n</html>",file=outfile)
    outfile.close

main()

