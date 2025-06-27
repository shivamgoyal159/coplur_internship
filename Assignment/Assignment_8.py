import numpy as np

print("--------------Question 1-----------------\n")

empty_array = np.empty((4, 2))
print("\n Empty 4x2 array = \n", empty_array)

full_array = np.full((4, 2), 7)
print("\n Full 4x2 array filled with 7 = \n", full_array)

zeros_array = np.zeros((3, 5))
print("\n 3x5 array filled with zeros = \n", zeros_array)

ones_array = np.ones((4, 3, 2))
print("\n 4x3x2 array filled with ones = \n", ones_array)

print("\n--------------Question 2-----------------\n")

matrix = np.arange(2, 11).reshape(3, 3)
print(" 3x3 matrix with values from 2 to 10 = \n", matrix)

print("\n--------------Question 3-----------------\n")

null_vector = np.zeros(10)
null_vector[5] = 11
print(" Null vector with sixth element as 11 = \n", null_vector)

print("\n--------------Question 4-----------------\n")

arr = np.array([10, 20, 30, 40, 50])
reversed_arr = arr[::-1]
print(" Original array = \n", arr)
print(" Reversed array = \n", reversed_arr)

print("\n--------------Question 5-----------------\n")

original_array = np.array([1,2,3,4])
print(" Original array = \n ", original_array)

float_array = original_array.astype(float)
print(" Array converted to float type = \n", float_array)
