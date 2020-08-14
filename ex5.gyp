name = 'Mikey D'
age = 28 #. !(╯°□°）╯︵ ┻━┻
height_imp = 5 * 12 + 10 # inches
height_met = height_imp * 2.54
weight_imp = 165 # lbs
weight_met = round(weight_imp / 2.205)
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height_imp} inches tall, which is {height_met} centimeters.")
print(f"He's {weight_imp} pounds heavy, which just so happens to be {weight_met} kg.")
print("Well, not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height_imp + weight_imp
print(f"If I add {age}, {height_imp}, and {weight_imp} I get {total}")
