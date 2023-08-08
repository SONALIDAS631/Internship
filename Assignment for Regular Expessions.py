#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Question 1- Write a Python program to replace all occurrences of a space, comma, or dot with a colon.


# In[2]:


import re

text = ('Ring-a-ring o roses, A pocket full of posies, A-tishoo, a-tishoo! We all fall down.111609')
print(re.sub("[,.]",":",text))    


# In[ ]:


Question 2-  Write a Python program to find all words starting with 'a' or 'e' in a given string.


# In[3]:


import re
# Input.
text = ('Ring-a-ring o roses, A pocket full of posies, A-tishoo, a-tishoo! We all fall down.111609')
#find all the worlds starting with 'a' 'e' 
list = re.findall("[ae]\w+",text)
# print result.
print(list)


# In[ ]:


Question 3- Create a function in python to find all words that are at least 4 characters long in a string. The use of the re.compile() method is mandatory.


# In[8]:


import re
text = 'Ring-a-ring o roses, A pocket full of posies, A-tishoo, a-tishoo! We all fall down.111609.'
print(re.findall(r"\b\w{4,}\b", text))


# In[ ]:


Question 4- Create a function in python to find all three, four, and five character words in a string. The use of the re.compile() method is mandatory.


# In[1]:


import re

text = ('Ring-a-ring o roses, A pocket full of posies, A-tishoo, a-tishoo! We all fall down.111609')
print(re.findall(r"\b\w{3,5}\b",text))    


# In[ ]:


Question 5- Create a function in Python to remove the parenthesis in a list of strings. The use of the re.compile() method is mandatory.


# In[11]:


import re
re.findall('[A-Z][^A-Z]*', 'Ring-a-ring o roses, A pocket full of posies, A-tishoo, a-tishoo! We all fall down.111609')


# In[ ]:


Question 6- Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression.


# In[13]:


import re 
x = "Ring-a-ring o roses (A pocket full of posies) [A-tishoo],"
re.sub("[\(\[].*?[\)\]]", "", x)


# In[ ]:


Question 7- Write a regular expression in Python to split a string into uppercase letters.


# In[15]:


import re
re.findall('[A-Z][a-z]*', 'Ring-a-ring o roses, A Pocket full of Posies, A-tishoo, a-tishoo! We all fall down.111609')


# In[ ]:


Question 8- Create a function in python to insert spaces between words starting with numbers.


# In[22]:


s = "RegularExpression1IsAn2ImportantTopic3InPython"
re.sub( r"([0-9])", r" \1", s).split()


# In[ ]:


Question 9- Create a function in python to insert spaces between words starting with capital letters or with numbers.


# In[25]:


import re
string='RegularExpression1IsAn2ImportantTopic3InPython'
words = re.findall('[A-Z][0-9]*', string)
print(' '.join((words)))


# In[ ]:


Question 10- Write a python program to extract email address from the text stored in the text file using Regular Expression.


# In[30]:


import re
text = "Please contact us at contact@tutorialspoint.com for further information."
      
emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
print(emails)


# In[ ]:


Question 11- Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.


# In[44]:


import re
def text_match(text):
        patterns = '^[a-zA-Z0-9_]*$'
        if re.search(patterns, text):
                return 'Found a match!'
        else:
                return('Not matched!')
            
print(text_match("The quick brown fox_jumps over the lazy dog_."))


# In[ ]:


Question 12- Write a Python program where a string will start with a specific number. 


# In[45]:


import re
def match_num(string):
    text = re.compile(r"^5")
    if text.match(string):
        return True
    else:
        return False
print(match_num('5-2345861'))
print(match_num('6-2345861'))


# In[ ]:


Question 13- Write a Python program to remove leading zeros from an IP address


# In[9]:


import re

ip = ('Ring-a-ring o roses, A pocket full of posies, A-tishoo, a-tishoo! We all fall down.111609')
string = re.sub('\.[0]*', '.', ip)

print(string)

    


# In[ ]:


Question 14- Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file.


# In[46]:





# In[ ]:


Question 15- Write a Python program to search some literals strings in a string. 


# In[17]:


import re

patterns = [ 'ring', 'gold', 'a-tishoo' ]
text = 'Ring-a-ring o roses, A pocket full of posies, A-tishoo, a-tishoo! We all fall down.111609'
for pattern in patterns:
    print('Searching for "%s" in "%s" ->' % (pattern, text),)
    if re.search(pattern,  text):
        print('Matched!')
        




    


# In[ ]:


Question 16- Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs


# In[15]:


import re

patterns =  'posies'
text = 'Ring-a-ring o roses, A pocket full of posies, A-tishoo, a-tishoo! We all fall down.111609'
match = re.search(pattern, text)
s = match.start()
e = match.end()
print('Found "%s" in "%s" from %d to %d ' %     (match.re.pattern, match.string, s, e))

    



    


# In[ ]:


Question 17- Write a Python program to find the substrings within a string.


# In[21]:


import re

text = 'Ring-a-ring o roses, A pocket full of posies, A-tishoo, a-tishoo! We all fall down.111609'
pattern = 'ring'
for match in re.findall(pattern, text):
    print('Found "%s"' % match)



# In[ ]:


Question 18- Write a Python program to find the occurrence and position of the substrings within a string.


# In[2]:


import re

text = 'Ring-a-ring o roses, A pocket full of posies, A-tishoo, a-tishoo! We all fall down.111609'
pattern = 'ring'
for match in re.finditer(pattern, text):


        s = match.start()
        
    print('Found "%s" at %d:%d' % (text[s:e], s, e))






# In[3]:


Question 19- Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.


# In[ ]:





# In[ ]:


Question 20- Create a function in python to find all decimal numbers with a precision of 1 or 2 in a string. The use of the re.compile() method is mandatory.


# In[ ]:


Question 21- Write a Python program to separate and print the numbers and their position of a given string.


# In[ ]:


Question 22- Write a regular expression in python program to extract maximum/largest numeric value from a string.


# In[ ]:


Question 23- Create a function in python to insert spaces between words starting with capital letters.


# In[2]:


import re

def capital_words_spaces(str1):

 taxt ='Ring-a-ring o roses, A pocket full of posies, A-tishoo, a-tishoo! We all fall down.111609'
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)
print(capital_words_spaces("Python"))

print(capital_words_spaces("PythonExercises"))

print(capital_words_spaces("PythonExercisesPracticeSolution"))







# In[ ]:


Question 23- Create a function in python to insert spaces between words starting with capital letters.


# In[6]:


import re
def “Regular_Expression_Is_An_Important_Topic_In_Python" (str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2",(str1): 
                
                
                
            
print(Regular_Expression_Is_An_Important_Topic_In_Python("Python"))
print(Regular_Expression_Is_An_Important_Topic_In_Python("PythonExercises"))
print(Regular_Expression_Is_An_Important_Topic_In_Python("PythonExercisesPracticeSolution"))


# In[ ]:





# In[ ]:


Question 24- Python regex to find sequences of one upper case letter followed by lower case letters


# In[1]:


import re
def text_match(text):
        patterns = '[A-Z]+[a-z]+$'
        if re.search(patterns, text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(text_match("AaBbGg"))
print(text_match("Python"))
print(text_match("python"))
print(text_match("PYTHON"))
print(text_match("aA"))
print(text_match("Aa"))


# In[ ]:


Question 25- Write a Python program to remove continuous duplicate words from Sentence using Regular Expression.


# In[2]:


def unique_list(text_str):
    l = text_str.split()
    temp = []
    for x in l:
        if x not in temp:
            temp.append(x)
    return ' '.join(temp)

text_str = "Python Exercises Practice Solution Exercises"
print("Original String:")
print(text_str)
print("\nAfter removing duplicate words from the said string:")
print(unique_list(text_str))


# In[ ]:


Question 26-  Write a python program using RegEx to accept string ending with alphanumeric character.


# In[ ]:


Question 27-Write a python program using RegEx to extract the hashtags.


# In[ ]:


Question 28- Write a python program using RegEx to remove <U+..> like symbols
Check the below sample text, there are strange symbols something of the sort <U+..> all over the place. You need to come up with a general Regex expression that will cover all such symbols.


# In[ ]:


Question 29- Write a python program to extract dates from the text stored in the text file.


# In[ ]:


Question 30- Create a function in python to remove all words from a string of length between 2 and 4.
The use of the re.compile() method is mandatory.


# In[ ]:





# In[ ]:




