name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# Study Drills
height_cm = round(height * 2.54,2)
weight_kg = round(weight / 2.205,2)

print(f"Let's talk about {name}.")
print(f"He's {height} inches, or {height_cm} centimeters, tall.")
print(f"He's {weight} pounds, or {weight_kg} Kilograms, heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
