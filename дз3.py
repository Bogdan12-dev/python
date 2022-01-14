#!/usr/bin/env python
# coding: utf-8

# In[8]:


print('hi, welcome to calculator')
operation = input("we have *, +, -, /, choose what u like to do :")
print("choose what u need to do")
if operation == '+':
    x = input('Enter first number: ')
    if x.isdigit():
        y = input('enter second number: ')
    else:
        print('thats not a number: ')
    if y.isdigit():
            print(f"{x} + {y} = {int(x) + int(y)}")
if operation == '-':
    x = input("Enter first value: ")
    if x.isdigit():
        y = input("enter second number: ")
    else: 
        print('thats not a number: ')
    if y.isdigit(): 
            print(f"{x} - {y} = {int(x) - int(y)}") 
if operation == '*':
    x = input("Enter first value: ")
    if x.isdigit():
        y = input("enter second number: ")
    else: 
        print('thats not a number: ')
    if y.isdigit(): 
            print(f"{x} * {y} = {int(x) * int(y)}") 
if operation == '/':
    x = input("Enter first value: ")
    if x.isdigit():
        y = input("enter second number: ")
    else: 
        print('thats not a number: ')
    if y.isdigit(): 
            print(f"{x} / {y} = {int(x) / int(y)}")             
print('Thank you for using my calculator! ')            


# In[ ]:




