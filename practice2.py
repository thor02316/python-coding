print("hello world")

word="hello"
revesed_woord=word[::-1]
print(revesed_woord)

num=(4,5,5,6,6,1,7)
number=list(set(num))
print(number)

a=4
b=6
a,b=b,a
print(a,b)

 

list1=[4,5,4]
list2=[8,7,3]
concatenated_list=list1+list2
print(concatenated_list)

nk=4
if nk%2==0:
    print("even")
else:
    print("odd")


my_list=[]
if_empty=len(my_list)==0
print(if_empty)



numv=[54,78,56,98]
larg=max(numv)
print(larg)


numbers = [12, 25, 39, 52, 65, 78, 91]
for i in numbers:
    if i % 13 == 0:
        print(i)
        
    else:
        print("non")

string = "Hello"
for char in string:
    print(char)


my_tuple = (1, 2, 3)
print(type(my_tuple))
string = "HELLO"
string=string.lower()
print(string)




sum_1_to_10 = sum(range(1, 11))
print(sum_1_to_10)


 
rows = 5
for i in range(1, rows + 1):
    print('*' * i)
#50,49,48,47,46,45,44,42,40,39,38,37,35,33,32,28,27.26,25,24,23,22,21,20,
    

numl=13
is_prime= True
if numl>1:
    for i in range(2, numl):
        if numl%i==0:
            is_prime=False
            break
else:
    is_prime=False
print(is_prime)


a, b = 10, 20
for i in range(10):
    print(a, end=" ")
    a, b = b, a + b

a, b = 10, 20
for i in range(10):
    print(a, end=" ")
    a, b = b, a + b






kum=153
kum_str=str(kum)
kum_len=len(kum_str)
sum_ofcbe=0
for i in kum_str:
    sum_ofcbe += int(i)**kum_len
if kum==sum_ofcbe:

    print(True)
else:
    print(False)

num1 = 7
num2 = 13
average = (num1 + num2) / 2
print(average)

numbers = [12, 5, 7, 19, 23, 1, 15, 8, 21, 13]
print(max(numbers))


sq=[4,5,2,7]
sqq=[x**2 for x in sq] #3 cube
print(set(sqq))

# Decimal to binary
decimal = 42
binary = bin(decimal)[2:]
print(binary)

# Binary to decimal
binary_str = "101010"
decimal = int(binary_str, 2)
print(decimal)


number = 5
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("The factorial of number is ",factorial)


year = 2004  # You can change this to any year

if (year % 4 == 0 and year % 100 != 0) :
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

positive_numbers = filter(lambda x: x < 0, range(-10 , 0))
print(list(positive_numbers))
