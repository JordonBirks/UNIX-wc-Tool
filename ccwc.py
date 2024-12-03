import sys

# A class to carry out the functionality of the project
# big change
class ccwc:
    def __init__(self, f = "", file = ""):

        # If it is a text file then read it in, else it is already read in and set file to data
        if file[-4:] == '.txt':
            with open(file, 'r') as temp_file:
                data = temp_file.read()
        else: 
            data = file

        # Check the method called is valid
        if (f in ('-c', '-l', '-w', '-m', "")) == False:
            sys.exit('Invalid first argument, should be -c, -l, -w, -m or nan')

        # Set f and file as class attrbutes
        self.f = f 
        self.data = data
        # run each function 
        self.c(self.data)


    def c(self, data):
        #print(len(data.encode('utf-8')))
        print(len(data))
    def l(self, data):
        pass

    def w(self, data):
        pass

    def m(self, data):
        pass

    def default(self, data):
        pass  

if __name__ == '__main__':
    #  cat test.txt | python ccwc.py
    #  python ccwc.py -c test.txt

    # If more than two arguments added, return error
    if len(sys.argv) > 3:
        sys.exit('Wrong number of arguments entered, this function requires 2 arguments or less')

    # If no arguments added read file out of standard input
    if len(sys.argv) == 1:
        f = ""
        file = sys.stdin.read()

    # If only one argument is providied it is the file name
    if len(sys.argv) == 2:
        f = ""
        file = sys.argv[1]
    
    # If two arguments provided, set the method to f and the file name to file
    if len(sys.argv) == 3:
        f = sys.argv[1]
        file = sys.argv[2]

    # Initialise the class, running all the functionality of the script
    inst = ccwc(f, file)


    