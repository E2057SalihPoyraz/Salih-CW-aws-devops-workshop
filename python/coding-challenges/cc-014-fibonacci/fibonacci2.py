fibonacci = [1, 1]

a = int(input("How many fibonacci numbers would you like to generate? "))

if a ==1:
    fibonacci = [1]
else:
    while len(fibonacci) < a:
        
        fibo_next = fibonacci[-2] + fibonacci[-1]

        fibonacci.append(fibo_next)

print(fibonacci)