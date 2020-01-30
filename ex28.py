# this is a worksheet that will grade itself on Boolean statements

def check(statement, guess):
    if eval(statement) != guess:
        print(f"Incorrect, \"{statement}\" is:", eval(statement))

check("True and True", True)
check("False and True", False)
check("1 == 1 and 2 == 1", False)
check("'test' == 'test'", True)
check("1 == 1 or 2 != 1", True)
check("True and 1 == 1", True)
check("False and 0 != 0", False)
check("True or 1 == 1", True)
check("'test' == 'testing'", False)
check("1 != 0 and 2 == 1", False)
check("'test' != 'testing'", True)
check("'test' == 1", False)
check("not (True and False)", True)
check("not (1 == 1 and 0 != 1)", False)
check("not (10 == 1 or 1000 == 1000)", False)
check("not (1 != 10 or 3 == 4)", False)
check("not ('testing' == 'testing' and 'Zed' == 'Cool Guy')", True)
check("1 == 1 and (not ('testing' == 1 or 1 == 0))", True)
check("'chunky' == 'bacon' and (not (3 == 4 or 3 == 3))", False)
check("3 == 3 and (not ('testing' == 'testing' or 'Python' == 'Fun'))", False)
print("All done!")
