# code scanner for detecting error inducing bugs from student submissions
# to run this application, in your terminal, run "python codescan.py studentsubmission.py"
# note that your file to be scanned must be in the same directory

import sys

total = len(sys.argv)
counter = 0

def found_print(line):
	if "print" in line and "#" not in line:
		print ("Print statement found at " + str(counter) + " |||| Note: Print statements may cause errors in Gradescope.")


#def filename_error(line):

#def web_server(line):
	#if encoding error 
		#print ("encoding error at " + str(counter))

#def smtp_error(line):
	#if smtp error
		#print ("smtp command error at " + str(counter))

#if no argument return error
if total < 2:
    print ("Error! - No File Specified!")
else:    
    filename = str(sys.argv[1])
    try:

    	f = open(filename, "r")

    	for line in f:
    		counter += 1
    		found_print(line)

    except Exception as e:
        print ("Error! - File Not Found!")