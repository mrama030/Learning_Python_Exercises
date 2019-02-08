from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't wan't that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file (in write mode)..."
# second parameter indicated open in write mode.
# the 'w' character for write. There's also 'r' for read, 'a' for append, and modifiers on these.
# you can also use 'w+', 'r+', and 'a+', to open in read/write mode.
print "Note: The default mode for open(filename) is READ mode"


target = open(filename, 'w')

print "Truncating the file!. Goodbye!"
target.truncate()

print "Now I'm going to ask for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# Study Drill: There's too much repetition in this file. Use strings, formats, and escapes to print out
# line1, line2, and line3 with just one target.write() command instead of six.

print "Study drill: We will write the same lines a second time, but using a single write command..."
print "writing again..."
target.write("%s\n%s\n%s\n" % (line1, line2, line3))
print "Study drill complete."

print "And finally, we close the file."
target.close()