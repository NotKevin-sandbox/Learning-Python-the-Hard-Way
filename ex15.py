# load argv modual form the sys database.
#from sys import argv

# unpack argv to str varables (script) and (filename)
#script, filename = argv

filename = input("Please type the name and extention of the file you wish to read: ")

# opens file named (filename) and assigns the crated file object to (txt)
txt = open(filename)

# formats and displays the str "Here's your file {filename}"
# with variable filename
print(f"Here's your file {filename}:")

# calls the function read without parameters on (txt) then displays results
print(txt.read())
txt.close()
# diplays the str "Type the filename again:"
#print("Type the filename again:")

# assigns str (file_again) to user input with prompt "> " 
#file_again = input("> ")

# opens file named (file_again) and assigns the crated
# file object to (txt_again)
#txt_again = open(file_again)

# calls the function read without parameters on (txt_again)then
# displays results
#print(txt_again.read())
#txt_again.close()
