# from sys import argv
# print(type(argv))
# print("The number of command line arguments: ",len(argv))
# print("The List of command line arguments: ", argv)
# print("Command line arguments one by one:")
# for x in argv:
#     print(x)
#     #sys and argv
#     #why?-->when we want to control cla from outside
#     #addition of 2 no.s using cla
# from sys import argv
# print(argv[1]+argv[2])
# print(int(argv[1])+int(argv[2]))

# # #OOPs features
# # #classes
# # #objects
# # #abstraction
# # #encapsulation
# # #inheritance
# # #polymorphism
# # #exception handling
# # #message passing
# # #dynamic binding
# #class creation
# class Student:
#     def show1(self):
#         self.a=20
#         print("I am in a show1",self.a)
#     def show2(self):
#         #a=30
#         print("I am in a show2",self.a)

# s=Student()
# s.show1()
# s.show2()
# #Constructors.
# class Student:
#     def __init__(self):
#         self.name="Atharva"
#         self.age=22
#         self.percentage=88
#     def showInfo(self):
#         print(self.name)
#         print(self.age)
#         print(self.percentage)
        
# # s=Student()
# # s.showInfo()
# constructors class with parameters.
# class Student:
#     def __init__(self,n,a,p):
#         self.name=n
#         self.age=a
#         self.percentage=p
#     def showInfo(self):
#         print(self.name)
#         print(self.age)
#         print(self.percentage)
# name=input("Enter name: ")
# age=int(input("Enter age: "))
# per=int(input("Enter percentage: "))
# s=Student(name,age,per)
# s.showInfo()
# #constructor overloading
# class MyPython:
#     def __init__(self):
#         print("First Constructor")
#     def __init__(self):
#         print("Second Constructor")
# #delete instance variable :
# class MyPython:
#     def __init__(self):
#         self.a=10
#         self.b=20
#         self.c=30
#         self.d=40
#     def func(self):
#         del self.d
# m=MyPython()
# print(m.__dict__)
# m.func()
# print()
# #Static variable and instance variable.
# class MyPython:
#     x=20
#     def __init__(self):
#         self.y=10
# m1=MyPython()
# m2=MyPython()
# print("m1 is: ",m1,x,m1.y)#20,10
# print("m2 is : ",m2.x,m2.y)#20,10
# MyPython.x=111
# m1.y=222
# print("m1 is: ",m1,x,m1.y)#111,222
# print("m2 is : ",m2.x,m2.y)#111,10
# class Employee:
#     def __init__(self,no,name,sal):
#         self.eno=no
#         self.ename=name
#         self.esal=sal
#     def showDetails(self):
#         print("Employee no : ",self.eno)
#         print("Employee ename : ",self.ename)
#         print("Employee salary : ",self.esal)
# class Test:
#     def updates(Employee):
#         Employee.esal=Employee.esal+8000
#         Employee.showDetails()
# e=Employee(101,"Atharva",100000)
# e.showDetails()
# Test.updates(e)
# #Inner Class
# class RAIT:
#     def __init__(self):
#         print("RAIT constructor")
#     class CSE:
#         def __init__(self):
#             print("CSE constructor")
#         def techfest(self):
#             print("RAIT - CSE techfest")
# r=RAIT()
# c=r.CSE()
# #----------
# c1=RAIT().CSE()
# c1.techfest()
# #----------------------
# RAIT().CSE().techfest()
# #Electricity bill program..

# class ElectricityBill:

#     def __init__(self):

#         self.c_name = ""
#         self.c_id = ""
#         self.unit = 0
#         self.bill_amount = 0.0

#     def inputData(self):

#         self.c_name = input("Enter customer name: ")
#         self.c_id = input("Enter customer ID: ")

#         while True:

#             try:
#                 self.unit = int(input("Enter number of units consumed: "))

#                 if self.unit < 0:
#                     raise ValueError("Units cannot be negative. Please enter again.")
#                 break

#             except ValueError as e:
#                 print(e)

#     def calculateBill(self):

#         if self.unit > 0 and self.unit <= 100:
#             self.bill_amount = self.unit * 3

#         elif self.unit > 100 and self.unit <= 200:
#             self.bill_amount = (100 * 3) + (self.unit - 100) * 4.5

#         elif self.unit > 200 and self.unit <= 300:
#             self.bill_amount = (100 * 3) + (100 * 4.5) + (self.unit - 200) * 5

#         elif self.unit > 300:
#             self.bill_amount = (100 * 3) + (100 * 4.5) + (100 * 5) + (self.unit - 300) * 7

#     def checkSubsidy(self):
#         is_subsidy = input("Are you under subsidy? (yes/no): ").strip().lower()

#         if is_subsidy == "yes":

#             if self.unit <= 200:
#                 self.bill_amount = 0

#             else:
#                 if self.bill_amount > 700:
#                     self.bill_amount += self.bill_amount * 0.15

#     def showBill(self):
#         print("\nCustomer Name:", self.c_name)
#         print("Customer ID:", self.c_id)
#         print("Units Consumed:", self.unit)
#         print("Total Bill Amount: Rs.", round(self.bill_amount, 2))

# # Example usage

# if __name__ == "__main__":
#     customer = ElectricityBill()
#     customer.inputData()
#     customer.calculateBill()
#     customer.checkSubsidy()
#     customer.showBill()
# embiguity issue in python/java
# class A:
#     def showA(self):
        
#         print("Class A")
        
# class B(A):
    
#     def showB(self):
        
#         print("Class B")

# class C(B):
    
#     def showC(self):
#         print("Class C")

# obj=C()
# obj.showC()
# obj.show()
#single inheritance
class A:
    def Dog(self):
        print("bhow")
class B(A):
    def Cat(self):
        print("meow")
obj = B()
obj.Dog()
obj.Cat()

#Multiple Inheritance.
class A:
    def Dog(self):
        print("bhow")
class B:
    def Cat(self):
        print("meow")
class C(A, B):
    def AnimalSounds(self):
        print("Animal sounds include:")
        self.Dog()  # Accessing method from class A
        self.Cat()  # Accessing method from class B
# Create an instance of C
obj = C()
obj.AnimalSounds()  # Calls methods from both parent classes.

#Multilevel inheritance.
class A:
    def Parent(self):
        print("bhow")
class B:
    def Cat(self):
        print("meow")
#Hybrid Inheritance.

class A:
    def Parent(self):
        print("bhow")
class B:
    def Cat(self):
        print("meow")
        
#constructor calling hierarchy
#super function
class Parent1:
    def show1(self,n):
        print(n)
class Parent2(Parent1):
    def show2(self):
        super().show1("Atharva")
        print("Parent2 method")
c=Parent2()
c.show2()
#2nd exg
class Parent1:
    def __init__(self,p):
        print(p)
class show1(self,n):
    def show2(self):
        super().show1("Atharva")
        print("Parent2 method")
        super().__init__()
c=Parent2()
c.show2()
#PolyMorphism(Overloading and overiding)
class Test:
    def __init__(self):
        print("No argument method")
    def __init__(self,a):
        print("One argument method: ",a)
    def __init__(self,a,b):
        print("Two argument method: ",(a+b))
#t=Test()
#t=Test(10)
t=Test(10,22)
#Constructor Overloading with variable number of arguments.
class Test:
    def __init__(self,*n):
        total=0
        for x in n:
            total=total+x
        print(total)

t=Test()
t=Test(10)
t=Test(10,22)
t=Test(10,22,33)
#Constructor overloading with default arguments.
class Test :
    def __init__(self,a=None,b=None,c=None):
        print(a,b,c)
t=Test()
t=Test(10)
t=Test(10,22)
t=Test(10,22,33)