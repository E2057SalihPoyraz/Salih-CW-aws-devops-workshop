fibonacci = [1, 1]

a = int(input("How many fibonacci numbers would you like to generate? "))

while fibonacci[-1] < a:

    fibo_next = fibonacci[-2] + fibonacci[-1]

    fibonacci.append(fibo_next)

print(fibonacci)