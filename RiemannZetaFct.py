#!/usr/bin/env python
# coding: utf-8

# # # Python Program to check values of Riemann's Zeta-Function
#  
#  Powered by: Dr. Hermann Völlinger, DHBW Stuttgart(Germany); September 2020
#      
#  See https://en.wikipedia.org/wiki/Riemann_zeta_function
#     
#  YouTube Video:  https://www.youtube.com/watch?v=sZhl6PyTflw&vl=en  
# 
# The Riemann zeta function or Euler–Riemann zeta function, ζ(s), is a function of a complex variable s that analytically 
# continues the sum of the Dirichlet serie which converges when the real part of s is greater than 1. 
# 
# More general representations of ζ(s) for all s are given below. The Riemann zeta function plays a pivotal role in 
# analytic number theory and has applications in physics, probability theory, and applied statistics.
# As a function of a real variable, Leonhard Euler first introduced and studied it in the first half of the eighteenth century 
# without using complex analysis, which was not available at the time. Bernhard Riemann's 1859 article "On the Number of 
# Primes Less Than a Given Magnitude" extended the Euler definition to a complex variable, proved its meromorphic continuation 
# and functional equation, and established a relation between its zeros and the distribution of prime numbers.[2]
# 
# The values of the Riemann zeta function at even positive integers were computed by Euler. The first of them, ζ(2), provides 
# a solution to the Basel problem. In 1979 Roger Apéry proved the irrationality of ζ(3). The values at negative integer 
# points, also found by Euler, are rational numbers and play an important role in the theory of modular forms. 
# Many generalizations of the Riemann zeta function, such as Dirichlet series, Dirichlet L-functions and L-functions, are known.
#   
#     
#     

# In[1]:


print("***LATEX syntax of zeta-fct for re(z)>1: '$ displaystyle \\zeta(s)=\sum_{n=1}^\infty 1/n^s $'***")


# In[2]:


print ("************************************************************************")
print ("****** The bridge between zeta-fct in 'Complex Analysis' and prim- *****") 
print ("****** numbers in 'Number Theory' is given by EulerProduct formula *****")
print ("************************************************************************")

from IPython.display import Image

Image('EulerProduct.jpg')


# In[3]:


print ("***** Here is the example of a plot of the zeta function ******") 
print ("*** See the non-trival zeros at 'critical' line real(z)=0.5 ***")
print ("***************************************************************")

from IPython.display import Image

Image('riemann-zeta1.jpg')


# In[4]:


print ("*** Here is the example of a plot of the zeta function in more detail***") 
print ("*** See two zeros at at the points z=0.5 + 14,12...z=0.5-14,12...***")
print ("*********************************************************************")

from IPython.display import Image

Image('riemann-zeta2.jpg')


# In[5]:


# Import libaries

from itertools import count, islice
from scipy.special import binom


# In[6]:


# Program/Source Code
# Here is the source code of a Python program to calculate the zeta function values 
# The program output is shown below.

def zeta(s, t = 100):
    if s == 1:
        return float("inf")
    term = (1 / 2 ** (n + 1)   
              * sum((-1) ** k * binom(n, k) * (k +1 ) ** -s
                     for k in range (n + 1))
           for n in count(0))
    return sum(islice(term, t)) / (1 - 2 ** (1- s)) 


# In[7]:


print ("value of zeta(2)=pi²/6 ~ 1,644934")
zeta(2)


# In[8]:


#pi * pi / 6


# In[9]:


print ("value of zeta(4)=(pi²)*(pi²)/90 ~ 1,0823236")
zeta(4)


# In[10]:


zeta(1)


# In[11]:


zeta(0)


# In[12]:


print("zeta(-1)= -1/12 ~ -0,0833333333")
zeta(-1)


# In[13]:


print("****'Trival' zeros are for z=-2,-4,-6,...****")


# In[14]:


zeta(-2)


# In[15]:


zeta(-4)


# In[16]:


zeta(-6)


# In[17]:


import time
print("****current date and time **************")
print("Date and Time:",time.strftime("%d.%m.%Y %H:%M:%S"))
print("end")

