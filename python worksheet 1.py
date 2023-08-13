#!/usr/bin/env python
# coding: utf-8

# In[ ]:


11.	Write a python program to find the factorial of a number.


# In[16]:


num = int(input("Enter a number: "))
factorial = 1
# check if the number is negative, positive or zero
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num + 1):
        factorial=factorial*i
    print("The factorial of",num,"is",factorial)


# In[ ]:


12.	Write a python program to find whether a number is prime or composite.


# In[14]:


num = int(input("Enter any number : "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is NOT a prime number")
            break
    else:
        print(num, "is a PRIME number")
elif num == 0 or 1:
    print(num, "is a neither prime NOR composite number")
else:
    print(num, "is NOT a prime number it is a COMPOSITE number")


# In[ ]:


13.	Write a python program to check whether a given string is palindrome or not.


# In[17]:


# function to check string is
# palindrome or not
def isPalindrome(str):
 
    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
 
# main function
s = "malayalam"
ans = isPalindrome(s)
 
if (ans):
    print("Yes")
else:
    print("No")


# In[ ]:


14.	Write a Python program to get the third side of right-angled triangle from two given sides.


# In[ ]:


from math import sqrt
print("Input lengths of shorter triangle sides:")
a = float(input("a: "))
b = float(input("b: "))
c = sqrt(a**2 + b**2)
print("The length of the hypotenuse is:", c )


# In[ ]:


15.	Write a python program to print the frequency of each of the characters present in a given string.


# In[19]:


# Python3 code to demonstrate
# each occurrence frequency using
# naive method
 
# initializing string
test_str = "GeeksforGeeks"
 
# using naive method to get count
# of each element in string
all_freq = {}
 
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
 
# printing result
print("Count of all characters in GeeksforGeeks is :\n "
      + str(all_freq))


# In[ ]:




