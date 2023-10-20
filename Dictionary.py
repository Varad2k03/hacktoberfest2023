D = {} 
 
L = [['a', 1], ['b', 2], ['a', 3], ['c', 4]]
 
# Loop to add key-value pair
# to dictionary
for i in range(len(L)):
    # If the key is already 
    # present in dictionary
    # then append the value 
    # to the list of values
    if L[i][0] in D:
        D[L[i][0]].append(L[i][1])
     
    # If the key is not present
    # in the dictionary then add
    # the key-value pair
    else:
        D[L[i][0]]= []
        D[L[i][0]].append(L[i][1])
         
print(D)
