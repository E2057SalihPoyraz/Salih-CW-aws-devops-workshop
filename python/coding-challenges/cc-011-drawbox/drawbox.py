num = int(input("Please enter the side length: "))
for i in range(num):
    if i==0 or i==(num-1):
        print("#"*num)
    else:
        print("#"+" "*(num-2)+"#")