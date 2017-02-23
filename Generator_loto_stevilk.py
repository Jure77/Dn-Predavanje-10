import random
print("Welcome to the Lottery numbers generator.")

def lottery():
    loto = []
    vpr = int(raw_input("Please enter how many random numbers would you like to have: "))
    print("User: %s" %vpr)
    loto = random.sample(xrange(1, 20 + 1), vpr)
    return loto

print lottery()