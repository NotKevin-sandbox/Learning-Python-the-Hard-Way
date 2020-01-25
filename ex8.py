# assigns varable (formatter) as string "{} {} {} {}"
formatter = "{} {} {} {}"

# formats (formatter) with int arguments (1), (2), (3), (4),
# then displays result
print(formatter.format(1, 2, 3, 4))

# formats (formatter) with sting arguments "one", "two", "three", "four",
# then displays result
print(formatter.format("one", "two", "three", "four"))

# formats (formatter) with bool arguments (True), (False), (False), (True),
# then displays result
print(formatter.format(True, False, False, True))

# formats (formatter) with string arguments (formatter), (formatter),
# (formatter), (formatter), then displays result
print(formatter.format(formatter, formatter, formatter, formatter))

# formats (formatter) with string arguments "Try your", "Own text here",
# "Maybe a poem", "Or a song about fear", then displays result
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
