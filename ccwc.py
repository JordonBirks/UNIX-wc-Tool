import sys

# A class to carry out the functionality of the project

# A class to implement comand line tool functionality
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

        # Set f and data as class attrbutes
        self.f = f 
        self.data = data

        # run each function based on condition
        if f == '-c': 
            self.c(self.data)
        if f == '-l': 
            self.l(self.data)
        if f == '-w': 
            self.w(self.data)
        if f == '-m': 
            self.m(self.data)
        if f == "" : 
            self.default(self.data)

    # Count bytes in file
    def c(self, data):
        print(len(data.encode('utf-8')))
    # Count line in file
    def l(self, data):
        print(data.count('\n'))
    # Count words in file
    def w(self, data):
        print(len(data.split()))
    # Count character in file 
    def m(self, data):
        print(len(data) - data.count(' '))

    # If no method specified do all
    def default(self, data):
        self.c(self.data) 
        self.l(self.data)
        self.w(self.data)
        self.m(self.data)

if __name__ == '__main__':
    # cat test.txt | python ccwc.py
    # python ccwc.py -c test.txt
    # conda activate /Users/jordonbirks/opt/anaconda3/envs/Standard

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


    
