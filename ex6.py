# defines variable (types_of_people) as int (10)
types_of_people = 10

# defines variable (x) as a formated string using variable (types_of_people)
x = f"There are {types_of_people} types of people."

# defines variable (binary) as string "binary"
binary = "binary"

# defines variable (do_not) as string "don't"
do_not = "don't"

# defines variable (y) as a formated string using variables
# (binary) and (do_not)
y = f"Those who know {binary} and those who {do_not}."

# displays variable (x)
print(x)

# displays variable (y)
print(y)

# displays formated string "I said: {x}" using variable (x)
print(f"I said: {x}")

# displays formated string "I also said: {y}" using variable (y)
print(f"I also said: '{y}'")

# defines variable (hilarious) as bool (False)
hilarious = False

# defines variable (joke_evaluation) as
# string "Isn't that joke so funny?! {}"
joke_evaluation = "Isn't that joke so funny?! {}"

#formats varable (joke_evaluation) with (hilarious) then displays it
print(joke_evaluation.format(hilarious))

# defines variable (w) as string "This is the left side of..."
w = "This is the left side of..."

# defines variable (e) as string "a string with a right side."
e = "a string with a right side."

# concatenates strings string varables (w) and (e) then displays the result 
print(w + e)
