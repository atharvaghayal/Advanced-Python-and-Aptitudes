#Problem No:01
"""WAP to take number input from user
and yake input character from user and print that character for input number of times."""
a=input("Enter a character you want to print: ")
b=int(input("How many number of times to print your character: "))
for i in range(1,b+1):
  print(a)

#Problem No:02
'''Takes two integer inputs from the user.
Performs and displays the results of addition, subtraction, multiplication, division, modulus, exponentiation, and floor division between these two integers.
Display the results in a well-formatted manner.'''
i=0
for i in range(0,6):
  a=int(input("Enter first number for operation: "))
  b=int(input("Enter second number for operation: "))
  c=input("Enter operation: ")
  if c=="Addition":
    print(a+b)
  elif c=="Substraction":
    print(a-b)
  elif c=="Multiplication":
    print(a*b)
  elif c=="Division":
    print(a/b)
  else:
    print("Enter valid number: ")

#Problem No:03
"""Problem:
Write a Python program that displays a multiplication table (from 1 to 10) for a number entered by the user.
"""
a=int(input("Enter a number: "))
i=0
for i in range(1,11):
  print(a*i)
  i=i+1

#Problem No:04
"""Problem:
Write a Python program to determine the grade of a student based on marks entered by the user.
If the marks are 90 or above, print "Grade: A".
If the marks are 80-89, print "Grade: B".
If the marks are 70-79, print "Grade: C".
If the marks are 60-69, print "Grade: D".
Otherwise, print "Grade: F"."""
a=input("Enter student Name: ")
English=int(input("Enter marks scored in English: "))
Maths=int(input("Enter marks scored in Maths: "))
Science=int(input("Enter marks scored in Science: "))
Social_Science=int(input("Enter marks scored in Social Science: "))
if (English+Maths+Science+Social_Science)//400*100:
  print(a,"You get a grade: A")
  