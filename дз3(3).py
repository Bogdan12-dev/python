#!/usr/bin/env python
# coding: utf-8

# In[13]:


print('hi, welcome to calculator')
operation = input("we have *, +, -, /, choose what u like to do: ")
if operation == '+':
    x = input("Enter first number: ")
    if x.isdigit():
        y = input("enter second number: ")
        if y.isdigit():
            print(f"{x} + {y} = {int(x) + int(y)}")
        else:
            print(f"{y} is not digit")
    elif x.isalpha():
        y = input("Second value: ")
        print(f"{x} + {y} = {x + y}")
    else:
        print(f"{x} is not digit or letter")
if operation == '-':
    x = input("Enter first number: ")
    if x.isdigit():
        y = input("enter second number: ")
        if y.isdigit():
            print(f"{x} - {y} = {int(x) - int(y)}")
        else:
            print(f"{y} is not digit")
    elif x.isalpha():
        y = input("Second value: ")
        print(f"{x} + {y} = {x + y}")
    else:
        print(f"{x} is not digit or letter")
if operation == '*':
    x = input("Enter first number: ")
    if x.isdigit():
        y = input("enter second number: ")
        if y.isdigit():
            print(f"{x} * {y} = {int(x) * int(y)}")
        else:
            print(f"{y} is not digit")
    elif x.isalpha():
        y = input("Second value: ")
        print(f"{x} + {y} = {x + y}")
    else:
        print(f"{x} is not digit or letter")   
if operation == '/':
    x = input("Enter first number: ")
    if x.isdigit():
        y = input("enter second number: ")
        if y == "0":
            print('divisoin by zero')
        if y.isdigit():
            print(f"{x} / {y} = {int(x) / int(y)}")
        else:
            print(f"{y} is not digit")
    elif x.isalpha():
        y = input("Second value: ")
        print(f"{x} + {y} = {x + y}")
    else:
        print(f"{x} is not digit or letter")   
if operation == "=":
    print('incorecct operation')


# In[ ]:




