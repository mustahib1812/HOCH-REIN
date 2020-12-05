# creating an empty list 
lst_1 = [] 
lst_2 = []


# number of elements as input 
n_1 = int(input("Enter number of elements to be inserted into LIST 1: ")) 

# iterating till the range 
for i in range(0, n_1): 
    ele = int(input()) 
  
    lst_1.append(ele) # adding the element 


n_2 = int(input("Enter number of elements to be inserted into LIST 2: ")) 
for i in range(0, n_2): 
    ele = int(input()) 
  
    lst_2.append(ele) # adding the element 



# If any of the list's lenght is shorter than the other one, 
# append 1 in the shorter list equal to the length of the bigger list
if (len(lst_1) < len(lst_2)):
    difference = len(lst_2) - len(lst_1)
    for i in range(difference):
        lst_1.append("1")

elif(len(lst_2) < len(lst_1)):
    difference = len(lst_1) - len(lst_2)
    for i in range(difference):
        lst_2.append("1")



for i in lst_1:
    for j in lst_2:
        continue
    # Print both the values
    print("Both values are : "+str(i)+" and "+str(j))

    sum_of_num = int(i)+int(j)
    # Print the sum of both the values
    print("Sum of both the values is : ", sum_of_num)

    if(sum_of_num % 3 == 0):
        print("Fizz")
    elif(sum_of_num % 7 == 0):
        print("Buzz")
    elif(sum_of_num%3==0 and sum_of_num%7==0):
        print("Fizz Buzz")