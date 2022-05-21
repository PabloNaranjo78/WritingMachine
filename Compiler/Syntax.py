import sys

# run with "python3 Syntax.py file.japi" 
fileToWork = open(sys.argv[1])

print(fileToWork.read())

fileToWork.close()
