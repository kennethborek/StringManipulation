import sys

def main():
    # The following commands under the 'def readfile():' command will read the test.txt file.
    # The 'def readfile' function is defining what exactly will be executing in the proceeding commands.
    def readfile():
        # This command retrieves the file.
        file=sys.argv[1]
    # This command will open the "test.txt" file.
    f=open("test.txt","r")
    # This command will scan and read the "test.txt" file.
    essay=f.read()
    # This command will confirm if the "test.txt" file is empty and/or cannot be located.
    checkfile(essay)
    # This command will close the "test.txt" file.
    f.close()
    # The following commands under the 'def checkfile():' command will scan the test.txt file and count words and sentences accordingly.
def checkfile(essay):
    # This establishes the variable 'a' to be an object.
    a=0
    # This establishes the conclusion of a sentence counter belonging to the 'for in range' statement.
    conclusionofsentence=0
    # This statement saves the count and adds it to a list.
    count=len(essay)
    # This statement establishes a range in which to iterate starting at zero and continuing to the conclusion.
    for a in range(0,count):
        # This statement establishes the punctuation marks indicated in the statement is to be acknowledged by the program to conclude a sentence.
        # This action will increment by 1 each iteration.
        if essay[a]=='.'or essay[a]==','or essay[a]=='!'or essay[a]==';':
            conclusionofsentence+=1
    # This command splits
    words=essay.split()
    print(words)

    legitimatewords=0
    sampleword=0
    b=0
    for a in words:
        sampleword=words[b]
        sampleword=len(sampleword)
        if sampleword >=3:
           legitimatewords+=1
        b+=1


    numberwords=len(words)
    print("The precise amount of words is equivalent to",len(words), "")
    print("")
    print("The complete amount of legitimate words is equivalent to", legitimatewords)
    print("")
    print("The calculated average value of words comprised within each sentence is equivalent to",legitimatewords/conclusionofsentence)



main()

