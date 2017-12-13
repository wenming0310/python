'''
print("There are %5d %s available" % (17, "donuts"))
print("%7d" % (11232/3))
print("%s %e" % ("Value is", 16.0 ** 0.5))
print("%x" % 127)
print("%20s\n" % "Banana swirl")
print("%s is $%4.2f" % ("Popsicle", 1.754))
print("%s %f" % ("Value is", 16.0 ** 0.5))
print("%07d" % (11232/3))
'''
'''
def save_transaction(price, credit_card, description):
    file = open("transactions.txt", "a")
    file.write("%s%07d%s\n" % (credit_card, price * 100, description))
    file.close()
items = ["DONUT", "LATTE", "FILTER", "MUFFIN"]
prices = [1.50, 2.0, 1.80, 1.20]
running = True

while running:
    option = 1
    for choice in items:
        print(str(option) + ". " + choice)
        option = option + 1
    print(str(option) + ". Quit")
    choice = int(input("Choose an option: "))
    if choice == option:
        running = False
    else:
        credit_card = input("Credit card number: ")
        save_transaction(prices[choice - 1], credit_card, items[choice - 1])
'''

def save_transaction(price, credit_card, description):
    file = open("transactions.txt", "a")
    file.write("%s%07d%s\n" % (credit_card, price * 100, description))
    file.close()
items = ["DONUT", "LATTE", "FILTER", "MUFFIN"]
prices = [1.50, 2.0, 1.80, 1.20]
running = True

while running:
    option = 1
    for choice in items:
        print(str(option) + ". " + choice)
        option = option + 1
    print(str(option) + ". Quit")
    choice = int(input("Choose an option: "))
    if choice == option:
        running = False
    else:
        credit_card = input("Credit card number: ")
        save_transaction(prices[choice - 1], credit_card, items[choice - 1])
