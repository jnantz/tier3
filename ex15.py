from sys import argv
# For now just understand that sys is a package, and this phrase just says to get the argv feature from that package. You'll learn more about these later.
script, filename = argv

txt = open(filename)

# Prints the file you enter when you first typed out your command
print "Here's your file %r:" % filename
# print the other file you named
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

