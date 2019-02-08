from sys import argv
from os.path import exists

# Script takes two parameters: 
script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two lines with one line, how?
#in_file = open(from_file)
#indata = in_file.read()

# my solution:
indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue or CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()

# not needed when using single-line solution
#in_file.close()

# file.close() acts as a save as well, so it is required for the output file
# but not the input file, since it was not modified, only read.