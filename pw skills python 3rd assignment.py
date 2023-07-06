#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Q1. Which keyword is used to create a function? Create a function to return a list of odd numbers in the range of 1 to 25.

#Ans=def keyword is used to create a function.
l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
list(filter(lambda x: x%2 != 0, l))


# In[4]:


#2nd

l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

def test(n):
    l1 = []
    for i in l:
        if i%2 != 0:
            l1. append(i)
        return l1


# In[7]:


test(l)


# In[15]:


#3rd

l1 = []
for i in l:
    if i%2 != 0:
        l1. append(i)


# In[16]:


l1


# In[24]:


#Q2. Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs to demonstrate their use.

#ans=In *args we can write multiple inputs.ex

def test1(*args): #we change name also of args and put any name like Raja,Mama etc because its not a function
    return args

#But in **kwargs we can input values in key and values format like as dictionary input.ex

def test2(**kwargs): #for kwargs use double *.
    return kwargs


# In[25]:


test1(1,25,14,11)
test2(a=[25,2,5,66],b='sssss',c=[30.6,6+1j])


# In[36]:


#Q3. What is an iterator in python? Name the method used to initialise the iterator object and the method used for iteration. 
#Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14,16, 18, 20].

#ans=Iterator is a process where data can process internally.next() used for initialisation the object and the mathod used for iteration.
#string is not a iterato,to convert into iterator use iter() function.
#ex
l=[2, 4, 6, 8, 10, 12, 14,16, 18, 20]
s=iter(l)


# In[37]:


next(s)


# In[38]:


next(s)


# In[39]:


next(s)


# In[40]:


next(s)


# In[41]:


next(s)


# In[86]:


#Q4. What is a generator function in python? Why yield keyword is used? Give an example of a generator function.

#generator function is used for a generation of functon for which we can use that again and agin after generation.
#yield is used for generator a function.ex

def test(n):
    a,b=0,1
    for i in range(n):
        yield a
        a,b=b,b+a
        


# In[87]:


for i in test(5):
    print(i)


# In[11]:


#Q5. Create a generator function for prime numbers less than 1000. Use the next() method to print the first 20 prime numbers.

def test_prime(n):
    a=1
    while a <= n:
        yield a
        if a % 2 == 0:
            return i
        a=a+1


# In[12]:


p=test_prime(5)


# In[13]:


for i in p:
    print(i)


# In[70]:


#Q7. Write a List Comprehension to iterate through the given string: ‘pwskills’.Expected output: ['p', 'w', 's', 'k', 'i', 'l', 'l', 's']

s='pwskills'

list(filter(lambda x : len(s),s))


# In[76]:


#Q9. Write a code to print odd numbers from 1 to 100 using list comprehension.
number=[i for i in range (1,100)]
list(filter(lambda x : x%2!=0,number))


# In[83]:


#Q6. Write a python program to print the first 10 Fibonacci numbers using a while loop.

def test2():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
    
    


# In[84]:


fib=test2()


# In[85]:


for i in range(10):
    print(next(fib))


# In[ ]:


#Q8. Write a python program to check whether a given number is Palindrome or not using a while loop.

number = int(insert('enter number'))
a=number
b=0
while number>0:
    c=number%10
    b=c

