#!/usr/bin/env python
# coding: utf-8

# # Tuple

# In[17]:


#immutable
#One create it , cannot change it, including items's orde and value etc...
#run faster
my_first_tuple = (1,2,3,4,5,5)
#my_first_tuple .sort() # tuple' object has no attribute 'sort'


# In[18]:


print(1 in my_first_tuple) 


# In[19]:


#dictionary key can be a tuple
dictionary_1 = {
  (1,2): [1,2,3],
  'b': 'Hello',
  'age': 'appear'
} 

print(dictionary_1[(1,2)])


# In[20]:


x,y,z,*other = (1,2,3,4,5,5)
print(x)
print(y)                                                                                        
print(other)


# In[24]:


#Most Important two function: (count, index, len()) in tuple
#my_first_tuple = (1,2,3,4,5,5)
print(my_first_tuple.count(5))
print(my_first_tuple.index(5)) #return the first's value index it finds
print(len(my_first_tuple))  


# # SET
# 1.SET is an unorder(unorder means the value's memory is not next to each other)
# 2.Every value is gonna be unique
# 3.value in set can only be grabbed as an item

# In[25]:


my_set = {1,2,3,4,5,5,5,}
print(my_set)


# In[26]:


my_set.add(100)
my_set.add(2) #repetitive value will not be added
print(my_set)


# In[28]:


#Small Exercise
my_list = [1,2,3,4,5,5]
set(my_list)
print(my_list)
print(set(my_list))


# In[30]:


my_set = {1,2,3,4,5,5}
#print(my_set[0])


# In[31]:


new_my_set =  my_set.copy()
print(new_my_set)
my_set.clear()
print(my_set)


# In[32]:


print(list(new_my_set))
print(new_my_set)


# # Set2

# In[5]:


#my_set = {1,2,3,4,5}
my_set = {4,5}
your_set = {4,5,6,7,8,9,10}
#print(my_set.difference(your_set))
#print(my_set.discard(5)) #remove item
#print(my_set)
#print(my_set.difference_update(your_set)) #Remove the items that exist in both sets:, difference dosen't return its value
#print(my_set.intersection(your_set))
#my_set.isdisjoint(your_set) #Return True if no items in set x is present in set y
#print(my_set.union(your_set)) #remove other duplicates
#print(my_set|your_set ) another way to union sets
#print(my_set & your_set ) another way to find intersection in set
my_set.issubset(your_set)


# # Conditional Logic

# In[7]:


is_old = False
is_licenced =True

if is_old and is_licenced:
    print('you are old enough to drive, and you have a licence!')
    
else:
    print('you are not of age')
    
print('okok')


# # Truthy and Falthy
# Help to keep python code simple and clear
# https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-how-is-it-different-from-true-and-false

# In[13]:


#print(bool(''))
#print(bool(5))
#print(bool(None))
password = '123'
username = 'Johnny'
print(bool(password))
print(bool(username))

if password and username: #Truthy and Falthy Helps to keey python code simple and clear
    print('your password and username is great')


# # Short Circuiting

# In[17]:


is_friend = False
is_User = True

if False and is_User:
    print('best friend forever')
    
else:
    print('We are not friend')


# # Logical Operators

# In[18]:


print('a'>'b') #why? Each character has a value according to the ASCII table:


# In[22]:


print('a'<'b'<'c' >'e') #
print(not(True))


# # Exercise

# In[25]:


is_magician = True
is_expert = False

if is_magician and is_expert:
    print("You are a magician: ")

elif is_magician and not is_expert:
    print("At least you are getting there")
elif not is_magician:
    print("You need magic powers")


# # is v.s. ==
# is: checking the location in memery where the values store is the same
# ==: check quality in values

# In[33]:


print(True == 1) 
print('1' == 1) # == comparing two types
print([] == 1 )
print(10 == 10.0)
print([] == [])


# In[37]:


print(bool('1'))
print('1' == 1)


# In[41]:


print(True is 1) #
print(1 is 1) # == comparing two types
print([] is 1 )
print(10 is 10.0)
print([1,2,3] is [1,2,3]) #create two new data types


# # Loop 
# works for list,set,tuple, dictionary (collection of items)

# In[43]:


for item in [1,2,3,4,5]: 
    print(item)


# #  Iterables

# In[73]:


User = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

#for item in User:
   # print(item)

# item in User.items():
#    print(item)

#for item in User.values():
#    print(item)
    
#for item in User.keys():
#    print(item)
    
#for Key, Value in User.items():
#    print(Key, Value)
    
for item in 50: #only collection item is iterable
    print(item)


# # Exercise Tricky Counter

# In[74]:


my_list = [1,2,3,4,5,6,7,8,9,10]
count = 0
for item in my_list:
    count = count+item
    
print(count)


# # Range
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

# In[75]:


print(range(100))


# In[82]:


for i in range(0,10,2): #run 100 times
    print(i)
    # Video72


# In[85]:


for i in range(10,0,-2): #convert
    print(i)


# In[88]:


for _ in range(2):
    print(list(range(10)))
    


# # Enumerate

# In[1]:


for i,char in enumerate ('Helloooo'):
    print(i,char)


# In[2]:


for i,char in enumerate ([1,2,3]):
    print(i,char)


# In[3]:


for i,char in enumerate (list(range(100))):
    print(i,char)


# # WhileLoop

# In[4]:


i = 0
while i<50:
    print(i)
    break
    


# In[ ]:


i = 0
while i <50:
    print(i)
    i=i+1
    break
else:  #while i condition is not working 
    print('done with all the work ')
    


# In[5]:


while True:
    response = input('say something: ')
    if (response =='bye'):
        break
        


# In[7]:


my_list = [1,2,3]
for item in my_list:
    print(item)

    
print(len(my_list))
i = 0
while i< len(my_list):
    print(my_list[i])
    i=i+1
    


# In[8]:


my_list = [1,2,3]
for item in my_list:
    continue    #Never a loop
    print(item)


# Video 77 exercise

# In[22]:


picture = [
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
]

print(picture[0][0])

i = 0
k = 0

while i < 6:
    while k < len(picture[i]):
        if picture[i][k] == 0:
            print(' ', end ='')
        else:
            print('*')
        k = k + 1
    print(/n)
    i = i+1
    




# # avoiding repetition

# In[4]:


def showtree():
    print("Tree")

showtree()
print(showtree) #print out its memory


# # Parameters and Argument

# In[12]:


#Parameters:A parameter is a variable in a function definition
#def say_hello(name, emoji): #Parameters
#    print(f'hellllooooo{name}{emoji}')
    
#Arguments: is a value passed during function invocation.
#positional arguments(position matter)
#say_hello('Luna',':)')

#Default Parameters #Parameters

def say_hello(name = 'Luna', emoji = '<3'):
    print(f'hellllooooo{name}{emoji}') 

#Keywords arguments
say_hello(name = 'Zelin' , emoji = '<3')

say_hello() #run the default result


# 
