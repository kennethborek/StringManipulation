# The following command introduces a specific module into the program being drafted.
import sys
#
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
        # This statement establishes that the punctuation marks, indicated in the statement, are to be acknowledged by the program to conclude a sentence.
        # This action will increment by 1 each iteration.
        if essay[a]=='.'or essay[a]==','or essay[a]=='!'or essay[a]==';':
            conclusionofsentence+=1
    # This command breaks down the string into an array.
    words=essay.split()
    # This command will display the result in the Run portion of the PyCharm Screen.
    print(words)
    # This establishes a legitimate or valid word as an object.
    legitimatewords=0
    # This establishes a sample or test word as an object.
    sampleword=0
    # This establishes the variable 'b' as an object.
    b=0
    # This statement establishes a loop in which to iterate the scan of the essay.
    for a in words:
        sampleword=words[b]
        sampleword=len(sampleword)
        if sampleword >=3:
           legitimatewords+=1
        b+=1
    numberwords=len(words)
    # These commands will display the respective text and the values indicated outside of the double quotes within the Run portion of the PyCharm Screen with the appropriate text .
    print("The precise amount of words is equivalent to",len(words), "")
    print("")
    print("The complete amount of legitimate words is equivalent to", legitimatewords)
    print("")
    print("The calculated average value of words comprised within each sentence is equivalent to",legitimatewords/conclusionofsentence)



main()

