#!/usr/bin/env python
# coding: utf-8

# # Mean_Variance_Std.Deviation
# 

# In[ ]:


import numpy 
N,M = (map(int, input().split()))
my_array = numpy.array([list(map(int, input().split())) for n in range(N)])
print(numpy.mean(my_array, axis = 1))        
print(numpy.var(my_array, axis = 0))       
print(round(numpy.std(my_array, axis = None),11))


# # Dot_Cross_Product

# In[ ]:


import numpy
N = int(input())
A = numpy.array([list(map(int, input().split())) for n in range(N)])
B = numpy.array([list(map(int, input().split())) for n in range(N)])
print(numpy.dot(A,B))
print(numpy.cross(A,B)


# # Inner_Outer_Product

# In[ ]:


import numpy
A = numpy.array(list(map(int, input().split())))
B = numpy.array(list(map(int, input().split())))
print(numpy.inner(A,B))
print(numpy.outer(A,B))

