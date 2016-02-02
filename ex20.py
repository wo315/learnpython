from sys import argv
script, input_file = argv

# print the file's all things 
def print_all(f):
    print f.read()

# position
def rewind(f):
	f.seek(0)

# read a line
def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(input_file)
# the first sentence printed 
print "First let's print the whole file:\n"
# call the function print_all
print_all(current_file)


print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines."

# print the first line
current_line = 1
print_a_line(current_line, current_file)
# print the second line

current_line += + 1
print_a_line(current_line, current_file)
# print the third line

current_line += + 1
print_a_line(current_line,current_file)

