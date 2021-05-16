#!/usr/bin/env python
# coding: utf-8

# # Riemann's Zeta-Function and Riemann's Hypothesis 
#  
#  Powered by: Dr. Hermann Völlinger, DHBW Stuttgart(Germany); May 2021
# 
# 
# ## Item1: Riemann's Zeta-Function     
# 
# See: https://en.wikipedia.org/wiki/Riemann_zeta_function
#     
# or the following YouTube Video: https://www.youtube.com/watch?v=sZhl6PyTflw&vl=en  
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

# In[1]:


print ("*** DirichletForm of the Riemann Zeta-Fuction (Euler**** ")
print ("*** LATEX syntax of zeta-fct for re(z)>1: '$ displaystyle \\zeta(s)=\sum_{n=1}^\infty 1/n^s $' ***")

from IPython.display import Image

Image('Images/DirichletForm4Riem-ZetaFct.jpg')


# In[2]:


print ("*** Zero-free_region_for_the_Riemann_zeta-function**** ")
from IPython.display import Image

Image('Images/Zero-free_region_for_the_Riemann_zeta-function.jpg')


# In[3]:


print ("************************************************************************")
print ("****** The bridge between zeta-fct in 'Complex Analysis' and prim- *****") 
print ("****** numbers in 'Number Theory' is given by EulerProduct formula *****")
print ("************************************************************************")

from IPython.display import Image

Image('Images/EulerProduct.jpg')


# ## Item2: Riemann's Hypothesis 
#  
# See: https://en.wikipedia.org/wiki/Riemann_hypothesis 
#     
# In mathematics, the Riemann hypothesis is a conjecture that the Riemann zeta function has its zeros only at the negative even integers and complex numbers with real part = 1/2.
# Many consider it to be the most important unsolved problem in pure mathematics.[1] It is of great interest in number theory because it implies results about the distribution of prime numbers. It was proposed by Bernhard Riemann (1859), after whom it is named.
# The Riemann hypothesis and some of its generalizations, along with Goldbach's conjecture and the twin prime conjecture, comprise Hilbert's eighth problem in David Hilbert's list of 23 unsolved problems; it is also one of the Clay Mathematics Institute's Millennium Prize Problems. The name is also used for some closely related analogues, such as the Riemann hypothesis for curves over finite fields.  

# In[4]:


print (" ************************************************************** ")
print (" **** Here is an example-plot of the riemann zeta-function **** ") 
print (" **** See non-trival zeros at 'critical' line real(z)=0.5 ***** ")
print (" **** This is a visualization of the Riemann-Hypothesis ******* ")  
print (" ************************************************************** ")

from IPython.display import Image

Image('Images/riemann-zeta1.jpg')


# In[5]:


print ("*** Here is the example of a plot of the zeta function in more detail***") 
print ("*** See two zeros at at the points z=0.5 + 14,12...z=0.5-14,12...***")
print ("*********************************************************************")

from IPython.display import Image

Image('Images/riemann-zeta2.jpg')


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


# Import libaries

from itertools import count, islice
from scipy.special import binom


# In[8]:


print ("************************************")
print ("*** List of zeta-function values ***")
print ("************************************")

# 1. zeta(-2)=0
print ("1. check zeta(-2)= 0:")
print ("zeta(-2) =",zeta(-2))

# 2. zeta(-1)=-1/12=-0,08333...
print ("************************************")
print ("2. check zeta(-1)=-1/12=-0,08333...:")
print ("zeta(-1) =",zeta(-1))

# 3. zeta(0)=-1/2
print ("************************************")
print ("3. check zeta(0)=-1/2:")
print ("zeta(0) =",zeta(0))

# 4. zeta(1)=unendlich
print ("************************************")
print ("4. check zeta(1)=unendlich(inf):")
print ("zeta(1) =",zeta(1))

# 5. zeta(2)=pi²/6=1,64493...
print ("************************************")
print ("5. check zeta(2)=pi²/6=1,644934...:")
print ("zeta(2) =",zeta(2))

# 6. zeta(3)=1,2020...
print ("************************************")
print ("6. check zeta(3)= 1,202056...:")
print ("zeta(3) =",zeta(3))

# 7. zeta(4)=(pi²)²/90
print ("************************************")
print ("7. zeta(4)=((pi²))²/90 ~ 1,082323...:")
print ("zeta(4) =",zeta(4))


# In[9]:


print("***********************************************")
print("** 'Trival' zeros are for z=-2,-4,-6,-8,etc. **")
print("***********************************************")
# 1. zeta(-2)=0
print ("1. check zeta(-2)=0:")
print ("zeta(-2) =",zeta(-2))

# 2. zeta(-4)=0
print ("************************************")
print ("2. check zeta(-4)=0:")
print ("zeta(-4) =",zeta(-4))

# 3. zeta(-6)=0
print ("************************************")
print ("3. check zeta(-6)=0:")
print ("zeta(-6) =",zeta(-6))

# 4. zeta(-8)=0
print ("************************************")
print ("4. check zeta(-8)=0:")
print ("zeta(-8) =",zeta(-8))


# In[10]:


import time
print("****current date and time **************")
print("Date and Time:",time.strftime("%d.%m.%Y %H:%M:%S"))
print("end")

