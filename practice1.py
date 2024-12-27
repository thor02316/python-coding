string="uday"
reverse_string=string[::-1]
print(reverse_string)
 

num=4
is_prime=True
if num>1:
 for i in range(2,num):
  if num % i ==0:
   is_prime=False
   break
else:
  
  is_prime=False
print(is_prime)


#factorial


number=15
factorial=1
for i in range (1, number+1):
 factorial*=i
print(factorial)

 
list=[1,5,3,9]
list.append(56)
list.pop(3)
print(list)
#fibonacci serises
a,b=0,1
for i in range(10):
 print(a,end="  ")
 a,b=b,a+b
  
pass

year=2016

if year%4==0 and year%100!=0 or year%400==0:
  print("leapyear")
else:
 print("not a leep year")



 #amstrong
num=157
num_str=str(num)
num_len=len(num_str)
sumof_power=0
for i in num_str:
 sumof_power+= int(i)**num_len
if num==sumof_power:
 print(True)
else:
 print(False)





input_str = "This is a string with spaces"
output_str = input_str.replace(" ","")
print(output_str)  # Output: "Thisisastringwithspaces"

input_str = "This is a string with spaces"
output_str = ''.join(input_str.split())
print(output_str)  # Output: "Thisisastringwithspaces"

for i in range(10):
    if i == 5:
       break
    print(i)


# Print positive numbers from 1 to 10
num = 1  # Start with the first positive number

print("Positive numbers:")
while num <= 10:  # Continue the loop until num is less than or equal to 10
    print(num)
    num += 1  # Increment the number by 1 for the next iteration

# Print negative numbers from -1 to -10
num = -1  # Start with the first negative number

print("Negative numbers:")
while num >= -10:  # Continue the loop until num is greater than or equal to -10
    print(num)
    num -= 1  # Decrement the number by 1 for the next iteration






keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = dict(zip(keys, values))
print(dictionary)

from array import array

# Creating an array of integers
arr = array('i', [1, 2, 3, 4, 5])

# Accessing elements
print(arr[0])  # 1
print(arr[2])  # 3

# Modifying elements
arr[2] = 10
print(arr)  # array('i', [1, 2, 10, 4, 5])

# Length of the array
print(len(arr))  # 5

class cal:
  def add(n):
    return(n+2)
obj=cal()
print(obj.add(3))