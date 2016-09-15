from sys import argv
#inports the argv module
script, filename = argv
#defines the arguments
text = open(filename)
#defines a variable called text that opens the file asigend to the file name variable
print "Here's your file %r:" % filename
print text.read()
# first a message, then a raw input of file name. then it reads the text variable which is to read the actual file
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
