# assigns var (people) to int 30
people = 30
# assigns var (cars) to int 40
cars = 40
# assigns var (trucks) to int 15
trucks = 15

# evaluate (cars > people) and execute following block if true
if cars > people:
    # displays the str "We should take the cars."
    print("We should take the cars.")
# evaluate (cars < people) and execute following block if true
elif cars < people:
    # displays the str "We should not take the cars."
    print("We should not take the cars.")
# execute following block if all previous if statements are False
else:
    # displays the str "We can;t decide."
    print("We can't decide.")

# evaluate (trucks < cars) and execute following block if true
if trucks > cars:
    # displays the str "That's too many trucks."
    print("That's too many trucks.")
# evaluate (trucks < cars) and execute following block if true
elif trucks < cars:
    # displays the str "Maybe we could take the trucks."
    print("Maybe we could take the trucks.")
# execute following block if all previous if statements are False
else:
    # displays the str "We still can't decide."
    print("We still can't decide.")

# evaluate (people < trucks) and execute following block if true
if people > trucks:
    # displays the str "Alright, let's just take the trucks."
    print("Alright, let's just take the trucks.")
# execute following block if all previous if statements are False
else:
    # displays the str "Fine, let's stay home them."
    print("Fine, let's stay home them.")
