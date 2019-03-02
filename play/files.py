import sys
sys.path.append('../') #this has been added so can be found in cmd window
print ("hi")

class Fourth_lesson:
    ''' Read a file and count how many words are from each word.
    Uppercase/downcase is not important.
    write it into a dictionary where words are listed with their quantity'''
    def __init__(self):
        pass
    def readfile(self):
        with open (file1.txt,'r') as infile:
            for line in infile:
                print (line)

d = Fourth_lesson()
d.readfile()