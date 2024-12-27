''' def functions'''
def thor(a,b):
    print(a,b)
thor(1,2)
def uday(name,age):
    print(name,age)
uday("thor",1500)
def kiran(c,k):
    print(c+k)
g=kiran(5,2)
def hulk(a):
    for i in a:
        print(i)
hulk("revender")

def put(*a):
    print(a)
put(1,5,8,8)
'''inheritance'''
class parent:
    def home(self):
        print("my home")
class child(parent):
    def home1(self):
        print("this is my home")
class grandchild(child):
    def home2(self):
        print("iam the final owner of this house")
obj=grandchild()
obj.home()
obj.home1()
obj.home2()
'''polymorphism'''
'''method over riding'''
class a:
    def journey(self):
        print("goa")
class v(a):
    def journey(self):
        print("usa")
obj=v()
obj.journey()

'''method over loading'''
class a:
    def sum(self,a,b):
       
       return a+b
    def sum(self,a,b,c=1):
       
       return(a+b+c)
obj=a()
obj.sum(1,2,3)
'''slicing'''
r=[1,8,6,9,5,7] 
print(r[1:5])