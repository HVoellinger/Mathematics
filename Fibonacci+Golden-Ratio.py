#!/usr/bin/env python
# coding: utf-8

# # Python Progarm to Calcualte Fibonacci Numbers' & "Golden Ratio'
# 
# Powered by: Dr. Hermann Völlinger, DHBW Stuttgart(Germany); August 2020
#     
# See Wikipedia: https://en.wikipedia.org/wiki/Fibonacci_number:
#  
# ## The Fibonacci Numbers 
# 
# Fibonacci numbers are named after Italian mathematician Leonardo of Pisa, later known as Fibonacci. In his 1202 book 
# Liber Abaci, Fibonacci introduced the sequence to Western European mathematics,[5] although the sequence had been described 
# earlier in Indian mathematics,[6][7][8] as early as 200 BC in work by Pingala on enumerating possible patterns 
# of Sanskrit poetry formed from syllables of two lengths.
# 
# Fibonacci numbers appear unexpectedly often in mathematics, so much so that there is an entire journal dedicated to their 
# study, the Fibonacci Quarterly. Applications of Fibonacci numbers include computer algorithms such as the Fibonacci search
# technique and the Fibonacci heap data structure, and graphs called Fibonacci cubes used for interconnecting parallel and 
# distributed systems.
# They also appear in biological settings, such as branching in trees, the arrangement of leaves on a stem, the fruit sprouts 
# of a pineapple, the flowering of an artichoke, an uncurling fern, and the arrangement of a pine cone's bracts.
# 
# ## 'Fibonacci Spiral'
#     
# An approximation of the golden spiral created by drawing circular arcs connecting the opposite corners of squares in 
# the Fibonacci tiling; (see preceding image) Fibonacci numbers are strongly related to the golden ratio: Binet's 
# formula expresses the nth Fibonacci number in terms of n and the golden ratio, and implies that the ratio of two 
# consecutive Fibonacci numbers tends to the golden ratio as n increases.
# 
# A tiling with squares whose side lengths are successive Fibonacci numbers: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144....

# In[1]:


print ("********************************************************************") 
print ("***'Fibonacci Numbers' are shown as squares whose side lengths *****") 
print ("*** are successive Fibonacci numbers: 1, 1, 2, 3, 5, 8, 13, 21.. ***")
print ("********************************************************************") 

from IPython.display import Image

Image('fibonacci-nb.png')


# In[2]:


print ("****************************************************************") 
print ("**'Fibonacci Spiral'= drawing a Spiral into the above squares:**") 
print ("****************************************************************") 

from IPython.display import Image

Image('fibonacci-sp.png')


# In[3]:


# First Part: 'Fibonacci Numbers'
print ("*********************************************************************")
print ("****The program calculates the Fibonacci Numbers & Golden Ratio******")
print ("*********************************************************************")
print (" ********** First Part: 'Fibonacci Numbers'**************************")
print ("*********************************************************************")


# In[4]:


# Start calculation of Fibo

def recur_fibo(n):  
   if n <= 1:  
       return n  
   else:  
       return(recur_fibo(n-1) + recur_fibo(n-2))

# End calulation of Fibo


# In[5]:


# Take the input from the user + print the Fibo numbers

nterms = int(input("Hello Hermann. How many terms you want? "))

# Check if the number of terms is valid  

if nterms <= 0:  
   print("Plese enter a positive integer")  
else:  
   print("The Fibonacci numbers until",nterms, "are:")  
   for i in range(nterms):  
       print(recur_fibo(i))
    
# End calculation and print of Fibonacci numbers
  
print ("****end of list of Fibo Numbers****")


# # End of First Part
# 
# 
# 
# # Second Part: 'Golden Ration'

# In[6]:


# second part: 'Golden Ratio'
print("Hello Hermann. Do you want to see the the 'Golden Ratio' numbers until this term? ")
go = int(input("Then type '1'"))
if go == 1: 
   print ("******************************************************************") 
   print ("*** The program calculates 'Golden Ratio'= (Fibo(i+1)/Fibo(i)) ***")
   # Start printing 'Golden Ratio'
   print ("******************************************************************")
   print ("Please check the values for: 'Golden-Ratio'~1.61803398875")
# Start printing 'Golden Ratio'
   for i in range(nterms):  
       print(recur_fibo(i+2)/recur_fibo(i+1))
else:
   print ("no 'Golden Ratio' numbers are calculated")

## End of Second Part


# In[7]:


# print current date and time
import time
print("date",time.strftime("%d.%m.%Y %H:%M:%S"))
print ("end")

