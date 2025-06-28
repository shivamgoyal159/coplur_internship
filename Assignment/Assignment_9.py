import numpy as np

print("---------Question 1---------\n")

a = np.array([1, 2, 3])
b = np.array([[4, 5, 6], [7, 8, 9]])

a_reshaped = a.reshape(1, -1)
print(a_reshaped)
combined = np.concatenate((a_reshaped, b), axis=0)
print(" Concatenate result = \n", combined)

print("\n---------Question 2---------\n")

c = np.array([[1, 2], [3, 4]])
flattened = c.flatten()
print(" Flattened Array = ", flattened)

print("\n---------Question 3---------\n")

arr = np.array([1, 2, 3, 4, 5])
reversed_arr = arr[::-1]
print(" Reversed Array = ", reversed_arr)

print("\n---------Question 4---------\n")

arr = np.array([10, 40, 30])

print(" Maximum number = ", np.max(arr))

print(" Minimum number = ", np.min(arr))

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(" Number of rows and columns = ", arr.shape)

print(arr[0,2])
print(arr[1])

sum = 0
for row in arr:
    for x in row:
        sum += x
print(" sum = ",sum)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(" Addition = ", a+b)
print(" Subtraction =", a-b)
print(" Multiplication =", a*b)
print(" Division = ", a/b)

