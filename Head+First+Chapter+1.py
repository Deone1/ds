
# coding: utf-8

# In[2]:

import sys
sys.platform
print sys.version


# In[5]:

import os
os.getcwd()


# In[8]:

import time
time.sleep(5)


# In[3]:

vowels = ['a','e','i','o','u']
word = raw_input("Write a word: ")
found = []
for letter in word :
    if letter in vowels :
        if letter not in found:
            found.append(letter)
for vowels in found :
    print vowels
print found



# ## Using [] as a subset operator for iterations etc ..Printing in Reverse

# In[36]:

jaffa = ['j','a','f','f','a']
jaffa[ : :-1]



# In[39]:

found = {}
found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0
found


# In[10]:

vowels = ['a','e','i','o','u']
word = raw_input("Write a word: ")
found = {}
for letter in word :
        if letter in vowels :
            if letter in found :
                found[letter] = found[letter] + 1
            else :
                found[letter]= 1

for letter,count in found.items():
    print "This %s occured %d times" %(letter,count)


# In[15]:

float(100.0/12) - 9.0


# Found.items method is preferable in Python while using a loop
# Also if letter in found :
#                 found[letter] = found[letter] + 1
#             else :
#                 found[letter]= 1
#                 can be replaced with found.setdefault(letter,0)
#                                      found[letter]=+1

# Dictionary of dictionaries

# In[49]:

people = {}
people['Ford'] = { 'Name': 'Ford Prefect',
'Gender': 'Male',
'Occupation': 'Researcher',
'Home Planet': 'Betelgeuse Seven' }
people['Arthur'] = { 'Name': 'Arthur Dent',
'Gender': 'Male',
'Occupation': 'Sandwich-Maker',
'Home Planet': 'Earth' }
people['Trillian'] = { 'Name': 'Tricia McMillan',
'Gender': 'Female',
'Occupation': 'Mathematician',
'Home Planet': 'Earth' }
people['Robot'] = { 'Name': 'Marvin',
'Gender': 'Unknown',
'Occupation': 'Paranoid Android',
'Home Planet': 'Unknown' }


# In[50]:

import pprint
pprint.pprint(people)


# In[60]:

set1= ['[','{','(']
def next_bracket(s) :
    if s == '[' :
        return ']'
    elif s =='{' :
        return '}'
    elif s =='(' :
        return ')'

wordlist= ['jaffa']
def delpattern(word):
    j = 0
    for i in range(len(word)-2) :
        if word[i] not in set1 :
            i = i+1
        else :
            if next_bracket(word[i]) == word[i+1]:
                word[i] = 0
                word[i+1] = 0
                j = j+2

    for x in range(j):
        word.remove(0)
    print(word)
    if len(word) == 2 :
        print (word)
        if next_bracket(word[0])==word[1]:
            print("can be solved")
        else:
            print("Can't be solved")

    else :
        if wordlist[-1] == ''.join(word) :
            print("Cant be saalved")

        else :
            wordlist.append(''.join(word))
            delpattern(word)














# In[67]:

word1 = raw_input("give a set of paranthesis")
word=list(word1)
delpattern(list(word))



# ## Working with Booleans in Python
# Something is False if it evaluates to 0 ; it has an empty data structure or is None

# In[71]:

print bool(0)
print bool({})
print bool(None)


# In[81]:

def search_for_letters(phrase,letters):
    letters=set(letters)
    found = letters.intersection(set(phrase))
    return bool(found),found
search_for_letters("hticcbkcbw","hijklm")


# Empty Lists,sets,tuples,dictionaries

# In[80]:

d = dict()
print "empty dictionary %r"%d
l = list()
print "empty list %r"%l
t = tuple()
print t
s = set()
print s


# ## Objects and Classes in Python

# In[17]:

states = {
'Oregon': 'OR',
'Florida': 'FL',
'California': 'CA',
'New York': 'NY',
'Michigan': 'MI'
 }


# In[27]:

state=states.get('Oregon',None)
print state


# In[92]:

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday =Song(["Happy birthday to you","I dont want to get sued","So Ill stop right there"])

bulls_on_parade = Song(["They rally around the family","With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()


# ## Inheritance

# In[94]:

class Vehicle(object) :
    def general_usage(self):
        print ("general use: transportation")
class Car(Vehicle):
    def __init__(ass):
        print "I'm a car"
        ass.general_usage()
        ass.wheels= 4
        ass.has_roof = True

    def specific_usage(ass):
        print "Car has",ass.wheels,"wheels"

class Bike(Vehicle):
    def __init__(self):
        print "I'm a Bike"
        self.wheels= 2
        self.has_roof = False

    def specific_usage(self):
        print "time Pass"

c = Car()
c.specific_usage()

b= Bike()
b.specific_usage()



# ## Exception Handling

# In[89]:

From = raw_input("From Number: ")
To = raw_input('To Number: ')
Step = raw_input('Step size: ')
try :
    lista = range(int(From),int(To),Step)

##except Exception as e:
##    print "Exception occured : ",e
##    lista=None
##print lista

## How to findout the type of Exception


except TypeError as e:
    print "Exception occured : ",type(e).__name__
    lista=None


except ValueError as e:
    print "Value Error"
    lista=None
print lista





# ## Generator Functions

# In[ ]:




# In[101]:

from urllib import urlopen
WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []
for word in urlopen(WORD_URL).readlines() :
    WORDS.append(word.strip())
WORD[]

# In[105]:



# In[ ]:
