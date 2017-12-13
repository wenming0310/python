from random import randint
secret = randint(1,10)
print("Welcome!")
#guess = 0
g = "yes"
#while guess != 250:
while g != "no":
    g = input("Guess the number: ")
    isnumber = g.isdigit()
    if isnumber == True:
        guess = int(g)
        if guess == secret:
            print("You win!")
            secret = randint(1,10)
            print("Next round!")
        else:
            if guess > secret:
                print("Too high!")
                print("You lose!")
            else:
                print("Too low!")
                print("You lose!")
    else:
        if g == "answer":
            print(secret)
        else:
            print("Please input number!")
print("Game over!")
