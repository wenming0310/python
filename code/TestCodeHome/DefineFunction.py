<<<<<<< HEAD
def make_smoothie():
    juice = input("What juice would you like? ")
    fruit = input("OK - and how about the fruit? ")
    print("Thanks. Let's go!")
    print("Crushing the ice...")
    print("Blending the " + fruit)
    print("Now adding in the " + juice + " juice")
    print("Finished! There's your " + fruit + " and " + juice + " smoothie!")
def shout_out(the_name):
    return("Congratulations " + the_name + "!")

print(shout_out('z'))
msg = shout_out('Graham, Jhon, Michael, Eric, and Terry by 2')
print(msg)
print(shout_out('Nonty'))

print("Welcome to smoothie-matic 2.0")
another = "Y"
while another == "Y":
    make_smoothie()
=======
def make_smoothie():
    juice = input("What juice would you like? ")
    fruit = input("OK - and how about the fruit? ")
    print("Thanks. Let's go!")
    print("Crushing the ice...")
    print("Blending the " + fruit)
    print("Now adding in the " + juice + " juice")
    print("Finished! There's your " + fruit + " and " + juice + " smoothie!")
def shout_out(the_name):
    return("Congratulations " + the_name + "!")

print(shout_out('z'))
msg = shout_out('Graham, Jhon, Michael, Eric, and Terry by 2')
print(msg)
print(shout_out('Nonty'))

print("Welcome to smoothie-matic 2.0")
another = "Y"
while another == "Y":
    make_smoothie()
>>>>>>> 228d57760e22242bd39aba4b7829a3e0c41dd95d
    another = input("How about another(Y/N)? ")