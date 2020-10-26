products = ["Pride and Prejudice", "To Kill a Mockingbird", "The Great Gatsby",
            "One Hundred Years of Solitude", "Pride and Prejudice", "In Cold Blood", "Wide Sargasso Sea",
            "One Hundred Years of Solitude", "Brave New World",  "The Great Gatsby", "Brave New World",
            "I Capture The Castle", "Brave New World", "The Great Gatsby", "The Great Gatsby",
            "One Hundred Years of Solitude", "Pride and Prejudice"]



def find_non_repeated(value):
    return [i for i in value if value.count(i)==1]

print(find_non_repeated(products))

