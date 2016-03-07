# __author__ = 'admin'
# -*- coding: utf-8 -*-
from sys import argv
from os.path import exists


script, from_file, to_file = argv
"""
print "Copying from %s to %s." % (from_file, to_file)

# We could do this on one line too, how?
file_data = open(from_file)
data = file_data.read()

# data = open(from_file).read()

print "The input file is %d bytes long." % len(data)
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_put = open(to_file, 'w')
out_put.write(data)

print "Alright, all done."

out_put.close()
file_data.close()
"""
with open(from_file) as data1, open(to_file, 'w') as data2:
    data = data1.read()
    data2.write(data)
