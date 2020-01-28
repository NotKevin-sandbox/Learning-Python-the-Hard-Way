# imports module from sys
from sys import argv

# unpacks argv to str variables (script) and (input_file)
script, input_file = argv

# defines fucntion print_all with argument f
def print_all(f):
    # reads the file f and displays the output.
    print(f.read())
# defines function rewind with argument f
def rewind(f):
    # takes file f and sets index to beginning of file
    f.seek(0)

#defines fucntion print_a_line with arguments line_count and f
def print_a_line(line_count, f):
    # diplays line_count and then reads the next line in f then diplays it
    # without appending a newline to the end
    print(line_count, f.readline(), end='')

# sets variable current_file to open('r') input_file
current_file = open(input_file)

# displays the str "First let's print the whole file:\n"
print("First let's print the whole file:\n")

# calls the function print_all with argument current_file
print_all(current_file)

# displays the str "Now let's rewind, kind of like a tape."
print("Now let's rewind, kind of like a tape.")

# calls funtion rewind with argument current_file
rewind(current_file)

# displays the str "Let's print three lines:"
print("Let's print three lines:")

# sets variable current_line to int 1
current_line = 1
# calls function print_a_line with arguments current_line and current_line
print_a_line(current_line, current_file)

# sets variable current_line to itself + 1 (increment by 1)
#current_line = current_line + 1
current_line += 1
# calls function print_a_line with arguments current_line and current_line
print_a_line(current_line, current_file)

# sets variable current_line to itself + 1 (increment by 1)
#current_line = current_line + 1
current_line += 1
# calls function print_a_line with arguments current_line and current_line
print_a_line(current_line, current_file)
