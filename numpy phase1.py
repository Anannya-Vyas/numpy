# %% [markdown]
# doing numpy from begening 

# %%
import numpy as np
values = np.array([10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000])
print(values)

# %%
#numpy array vs python lists 
one_d_list =[10,20,30,40,50,60,70,80,90]
print(one_d_list)
import numpy as np

one_d_array= np.array([10,20,30,40,50,60,70,80,90])
print(one_d_array)
# multiplication 
multiplication_list= one_d_list*2
multiplication_array = one_d_array*2
print(f"multiplication of list is: {multiplication_list}")
print(f"multiplication of array is: {multiplication_array}")

# %%
# numpy array type vs python list type 
list= [1,2,3,4,5,6,7,8,9,10]
print(type(list))


import numpy as np
array = np.array([1,2,3,4,5,6,7,8,9,10])
print (array.dtype)

# %% [markdown]
# <U34 is a Unicode string data type used only when the array contains strings, and the number represents the maximum string length

# %% [markdown]
# < → little-endian (how bytes are stored):Little-endian means the least significant byte is stored first in memory.
# 
# U → Unicode string
# 
# 34 → maximum length is 34 characters

# %%
# what if i take multile data types in an array 
list =[9502, "Anannya Vyas ", 230099500306, 9.44]
print("list in python is: ",list)
# converting this list to array 
import numpy as np 
new_array= np.array(list)
print("now array becomes:\n", new_array)
print("data type of this new list is:\n",new_array.dtype)


# %%
# checking the numpy version
import numpy as np
np.version
print(np.version)


# %% [markdown]
# scaler   : stores only a single value 
# vector   : one-d collection of values 
# matrices : two-d collection of values 
# tensor   : three-d collection of values 

# %% [markdown]
# BASIC ARRAY CREATION 
# range will be arange ( array range): arange
# zeros
# ones
# linear space: linspace
# 

# %% [markdown]
# for two 2 array first comes rows then columns 

# %%
import numpy as np
range_made_array= np.arange(1,100) #100 is not included 
print(range_made_array)

print("\n")

# giving steps : these steps are the gaps 
range_made_array = np.arange(1,100,10)
print("array after giving steps is",range_made_array)

# %%
# using zeros 
import numpy as np
arr= np.zeros(6)

print(arr)
# why dots(0.)
# lets check the type of array 
print(arr.dtype)


# what if i want zeros to be 2d 
arr_new= np.zeros((100,100))
print(arr_new)

# %%
#  now see the output that it give sis just so much long and its not even printing it all 
# so to make that all print you need to do one command

# use:np.set_printoptions(threshold=np.inf)
import numpy as np
np.set_printoptions(threshold=np.inf)

arr= np.zeros((100,100))
print(arr)

# %%
# using ones
import numpy as np 

arr= np.ones(3)
print(arr)

# making it 2d
arr1= np.ones((10000,6))
# row and then column
print(arr1)


# %% [markdown]
# using linear space function here you give two numbers and ten even you can tell what all no of values you want between these two numbers 
# 
#  np.linspace(start, stop, num)
#  num is number of samples 

# %%
# using linspace
arr= np.linspace(   1,100,2) # here 100 is included 
print(arr)
arr1=np.linspace(0,1,100)
print(arr1)
# this gives error because 
# arr2=np.linspace((0,7,5))
# print(arr2)
# REASON IS  LINSPACE HAS A SYNTAX: np.linspace(start, stop, number of samples(num))

# %%
# WHAT IF I GIVE A NEGATIVE LINSPACE VALUE 
arr= np.linspace(1,89,-7)
print(arr)
"""this gives error

Number of samples, {num}, must be non-negative."""


