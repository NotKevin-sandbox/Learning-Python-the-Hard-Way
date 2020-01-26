from sys import argv

system, filename = argv

txt = open(filename)

print("Here is the body of that file:")
print(txt.read())

txt.close()
