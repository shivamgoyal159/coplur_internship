import numpy as np
#
# print("\n----3D Array----\n")
#
# arr = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]]])
# print(arr)
#
# print("\n----Array Shape----\n")
#
# print(arr.shape)
#
# print("\n----Zeros Array----\n")
#
# x = np.zeros((2,3,4))
# print(x)
#
# print("\n----Array copy----\n")
#
# x = arr.copy()
# print(x)
#
# print("\n----Array View----\n")
#
# y = arr.view()
# print(y)
#
# print("\n----To print specific number in the place of other numbers----\n")
# #here full arr 0 is changed to 42
#
# arr[0]=42
# print(arr)
#
# print("\n----reshape----\n")
#
# arr = np.array([3,545,6,3,4,6,3,5])
# print(arr)
# print(arr.reshape(2,4).base)    #'base' jo bhi changes h unlo neglect kar deta h
# print(arr.reshape(2,4))
#
# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(arr.reshape(2,2,3))
#
# arr = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]]])
# # x = arr.reshape(-1)    # -1 convert all upper dimensions in 1D array
# print("----")
# x = arr.reshape(6,4)
# print(x)
#
# print("\n----to change dimension of an array----\n")
#
# arr = np.array([3,545,6,3,4,6,3,5],ndmin=5)   # ndmin me 'n' value doge vo usko 'nD' array me dega bahalai koisa bhi dimensional array ho
# # arr = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]]],ndmin=5)
#
# print(arr)
#
# print("\n----iteration----\n")
# # kholke alag alag show karta h kisme kya kya chiz h
#
# arr = np.array([[2,4,6],[32,62,77]]) # 2 D array
# for row in arr :
#     print(row)
#     for x in row:
#         print(x)
#
# arr = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]]])  # 3 D array
# for row in arr :
#     print(row)
#     for x in row :
#         print(x)
#         for y in x :
#             print(y)
#
#
# print("\n----to change data type----\n")
#
# arr = np.array([[2.2,4,6],[32,62,5.77]],dtype=int)  # dtype dene se vo usme change kar deta h
# print(arr)
# print(arr.ravel())   # to change in 1D
# print(arr.sum(1))
# print("-----")
#
# arr = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]]],dtype = float)  # 3 D array
# print(arr.ravel())   # to change in 1D
# print(arr.min())
# print(arr.max())
# print(arr.sum())
# print(arr.sum(2))
# print(arr.sum(1))
#

print("\n---- addition of two array ----\n")

a = np.array([[2,4,6],[32,62,62]])
b = np.array([[7,2,8],[3,7,2]])
# print("\n",a+b)
# print("\n",a-b)
# print("\n",a*b)
# print("\n",a/b)
# print("\n",a**b)
# print("\n",a//b)
# print("\n",a%b)


# x = a.dot(b.T)   # T = transpose
# print(x)

# padded_array=np.pad(a,pad_width=2,mode='constant')
# print(padded_array)

# x = np.transpose(a)
# print(x)

# res = np.concatenate((a,b),axis=1)
# print(res)

arr = np.arange(9)
print(arr)
print(arr[2:])

result = np.split(arr,3)   # to break into equal given parts
print(result)
# for i , sub    # kuch to tha kar lena


a = np.array([[2,8,6],[66,62,62]])                                        # 2 D array
print(a.shape)
# b = np.resize(a,(3,3))
b = np.resize(a,(4,4))    # convert karra h aur bache kuche element usi me se vapas repeat karra h
print(b)


# print(np.append(a,[7,8,9]))
print(np.append(a,[[88,55,77]],axis=0))
print(np.append(a,[[88,55,77],[99,88,77]],axis=0))
print(np.append(a,[[88,55,77],[99,88,77]],axis=1))

print(np.insert(a,3,[11,12]))  # insert at position by index

print(np.delete(a,2)) # delete at position by index

print("---")
z = np.arange(12).reshape(4,3)
print(z)

print(np.flip(z))  # reverse

print(np.sort(a))  # sort

g = np.argmax(a)   # gives the index of maximum value
print(g)

