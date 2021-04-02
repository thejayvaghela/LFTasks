import random

def optimized_random(mylist):
    length=len(mylist)
    while length>0:
        at=random.randrange(length) # Random Number From List (DEPENDS ON 0 - LENGTH).
        number=mylist[at]           # Print the number present at the randomly picked index.
        print(number)
        mylist[at]=mylist[length-1] # Replace the number with the number at index LENGTH-1.
        length=length-1             # DECREMENT the length by 1.
                                    # Next Random will only pick numbers which are less than now LENGTH.
    print("LENGTH : ",len(mylist))  # Length of List is intact.


i=100
mylist=[] # I TOOK THIS LIST JUST FOR EXAMPLE
for x in range(0,i):
    mylist.append(x)

# mylist = [1, 2, 3, 4, 5, 6, 7 ,8,9,10]
print(mylist)
optimized_random(mylist)



