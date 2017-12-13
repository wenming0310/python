
def save_transaction_cardfirst(price, credit_card, description):
    file = open("transactions.txt", "a")
    file.write("%16s%07d%16s\n" % (credit_card, price * 100, description))
    file.close()

def save_transaction_pricefirst(price, credit_card, description):
    file = open("transactions.txt", "a")
    file.write("%07d%16s%16s\n" % (price * 100, credit_card, description))
    file.close()