from sys import argv

script_name, text_file_name = argv

text = open(text_file_name)

print "Here's your file %r:" % text_file_name
print text.read()

print "Type the filename again:"
file_again = raw_input('> ')

text_again = open(file_again)

print text_again.read()