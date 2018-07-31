# Declare variables
mylist = [2,3,1,3,5]   # Our inputs to the program
has_duplicates = False # initialize as false (why?)

mylist.sort()
# : Loop through 'mylist' with a for-Loop
for index in range(len(mylist) - 1): # range(5)
    print(mylist) # index is the index of the element
    print(mylist[index], mylist[index + 1])

    # : Check if adjacent elements of 'mylist' are the same
    if mylist[index] == mylist[index + 1]:
        has_duplicates = True
        break
        #  if they are the same, set has_duplicates to True
        # Exit out of the for-loop (no need to check rest of list)

print(has_duplicates) # Our outputs of the program
