import random

def passwdgen(name):

    name2 = name.replace(" ", "").lower()

    firstchar = random.choice(name2)
    secondchar = random.choice(name2)
    thirdchar = random.choice(name2)

    num = random.randint(1000, 9999)

    password = f"{firstchar}{secondchar}{thirdchar}{num}"

    return password


name = input("Please enter your first and surname: ")
print("The password is:", passwdgen(name))