#!/usr/bin/env python
# coding: utf-8

# In[1]:


y = '5'
x = '10'
x = '12'
one = y > x
two = y < x
tri = y == x
four = y != x
five = y>x>y
print(one)
print(two)
print(tri)
print(four)
print(five)


# In[ ]:


name = input('place ur name: ')
surname = input(f"hi {name}, what is ur surname?: ")
dads = input(f"{name}  {surname} яке у вас по батькові?: ")
date = input(f"{name} {surname} {dads} enter ur born date: ")
print(f"name = {name}")
print(f"surname = {surname}")
print(f"dads = {dads}")
print(f"born date = {date}")
print(f"pip = {name[:1]}{surname[:1]}{dads[:1]}")      


# In[ ]:


given_string = '   i am gonna have my super power tomorrow morning so i am heading to bed now. Bye everyone   '
case = given_string.upper()
lower = case.casefold()
digit = given_string.isalpha()
nospace = given_string.strip()
count = given_string.count('a')
replace = given_string.replace('i', '1')
replace2 = given_string.replace(' ', '-')
replace3 = given_string.replace('super power', 'tasty breakfast')
print(digit)
print(case)
print(lower)
print(nospace)
print(count)
print(replace)
print(replace2)
print(replace3)


# In[ ]:




