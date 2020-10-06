x = "{[()}]"
for i in range(len(x)//2):
    x = x.replace("()","")
    x = x.replace("[]","")
    x = x.replace("{}","")
print(not bool(x))