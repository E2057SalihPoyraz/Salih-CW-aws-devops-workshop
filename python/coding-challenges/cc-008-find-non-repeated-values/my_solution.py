def my_function(book_list):
    for i in book_list:
        if book_list.count(i) == 1:
            print(i)


products = ["Pride and Prejudice", "To Kill a Mockingbird", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice", "In Cold Blood", "Wide Sargasso Sea",\
"One Hundred Years of Solitude", "Brave New World",  "The Great Gatsby", "Brave New World",\
"I Capture The Castle", "Brave New World", "The Great Gatsby", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice"]

  
my_function(products)