def firstNonRepeating(arr, n): 
  
    for i in range(n): 
        j = 0
        while(j < n): 
            if (i != j and arr[i] == arr[j]): 
                break
            j += 1
        if (j == n): 
            return arr[i] 
      
    return -1

# Driver code 
arr = ["Pride and Prejudice", "To Kill a Mockingbird", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice", "In Cold Blood", "Wide Sargasso Sea",\
"One Hundred Years of Solitude", "Brave New World",  "The Great Gatsby", "Brave New World",\
"I Capture The Castle", "Brave New World", "The Great Gatsby", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice"] 
n = len(arr)
print(n) 
print(firstNonRepeating(arr, n)) 