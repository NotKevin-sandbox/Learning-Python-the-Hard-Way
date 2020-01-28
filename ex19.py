# creates function cheese_and_crackers that takes 2 arguments:
# cheese_count and boxes of crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # formats and displays the string "You have {cheese_count} cheeses!"
    print(f"You have {cheese_count} cheeses!")
    # formats and displays the string "You have {boxes_of_crackers}
    # boxes of crackers!"
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # displays "Man that's enough for a party!"
    print("Man that's enough for a party!")
    # displays "Get a blanket (newline)"
    print("Get a blanket.\n")

# displays "We can just give the function numbers directly:"
print("We can just give the function numbers directly:")
# calls function cheese_and_crackers with arguments int 20, and 30
cheese_and_crackers(20, 30)

# displays "OR, we can use variables from our script:"
print("OR, we can use variables from our script:")
# sets variable (amount_of_cheese) to int 10
amount_of_cheese = 10
# sets variable (amount_of_crackers) to int 50
amount_of_crackers = 50

# calls function cheese_and_crackers with arguments:
# amount_of_cheese and amount_of_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# displays "We can even do math inside too:"
print("We can even do math inside too:")
# calls function cheese_and_crackers with arguments:
# 10 + 20, 5 + 6 evaluated
cheese_and_crackers(10 + 20, 5 + 6)

# displays "and we can combine the two, variables and math:"
print("And we can combine the two, variables and math:")
# calls function cheese_and_crackers with arguments:
# (amount_of_cheese) + 100, (amount_of_crackers) + 1000 evaluated
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
