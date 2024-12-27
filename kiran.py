b="thor"
for i in b:
    print(i)


for i in range (1,10):
    print(i)


thor=[1,2,5,6,4]
for i in thor:
    if i==2:
        print("2 is my fav num")
        break
    else:
        print("non")
s=(2,55,26,75,12)
print(sorted(s))
g={1,5,1,6,23,45}
print(g.update([26,56]))
print(g)
h={"name":"thor"}
print(h["name"])

print(h)


import numpy as np
a=np.array([2,6,4,8])
print(a)
b=np.array([1,2,3,4])
print(b)

print(a.ndim)
print(b.shape)
k=np.random.rand(4,4)
print(np.vstack((a,b)))
print(np.sum([a,b],axis=1))

s=np.full((3,3),16)
print(s)





num=int(input("enter tne number:"))
if num%2==0:
    print("{0} is even".format(num))
else:
    print("iam not 2")

num=int(input("enter the required table no:"))
for i in range (1,12):

    print(num,"x",i,"=",num*i)
num =int(input("enter the number:"))
if num<0:
    print("{0} is negitive".format(num))
else:
    print("{0} is postive".format(num))



l=12
p=5
u=87
if(l>p)and(l>u):
    print("l is largest number")
elif(p>l)and(p>u):
    print("p is largest")
else:
    print("u is largest")
