import numpy as np


print("------SWAP-------\n")
print("\n----1d----\n")

arr = np.array([10,20,30,40,50])
print(arr[1])
# arr[0] , arr[2] = arr[2] , arr[0]
arr[2] , arr[1] , arr[0] , arr[3] = arr[1] , arr[2] , arr[3] , arr[0]
print(arr)

print("\n----2d----\n")

arr = np.array([[10,20,30,40,50],[2,5,6,8,9],[5,8,2,8,1]])
print(arr)
arr [0,3] , arr [1,1] = arr [1,1] , arr[0,3]
print(arr)

print("\n----row swap----\n")
arr [[0,2],:] = arr[[2,0],:]   # here 0,2 are not indexes of element here they are rows , we are swapping 0 and 2 row
print(arr)

print("\n----column swap----\n")
arr [:,[0,2]] = arr[:,[2,0]]
print(arr)

print("\n----3d----\n")

arr = np.array([[[10,20,30,40,50],[2,5,6,8,9],[5,8,2,8,1]],[[10,20,30,40,50],[25,555,55,555,5],[5,8,2,8,1]]])
print(arr)

# arr [0,0,4] , arr [1,2,3] = arr [1,2,3] , arr [0,0,4]
# print(arr)

print("\n----row swap----\n")

arr [[0,1],:] = arr[[1,0],:]
arr [[0,1],[0,1],:] = arr[[1,0],[1,0],:]
print(arr)

print("\n----column swap----\n")

arr [:,:,[0,2]] = arr [:,:,[2,0]]
print(arr)

print("\n----identifying missing data----\n")

arr = np.array([1,2,np.nan,4,np.nan,5])
print(arr)
emp = np.isnan(arr)
print(emp)

res = np.nan_to_num(arr,copy=True,nan=0,posinf=None,neginf=None)   # 0 ki jagah kuch bhi de sakti h ,  posinf=None,neginf=None ye lagana jaroori nhi h
print(res)

print("\n------to store binary format------\n")

a = np.array([[2,4,6],[32,62,62]])
np.save('data.npy',a)

res = np.load('data.npy')  # npy save karta h single array
print(res)

a = np.array([2,4,6])
b = np.array([[2,4,6],[32,62,62]])

np.savez('data.npz',array=a , array2=b)    # behaving like dictionary but it is not a dictionary

res = np.load('data.npz')  # npz save karta h multiple array
print("\n", res)
print("\n", res['array'])
print("\n", res['array2'])

print("----for text format----")
with open('data.txt','w') as f:
    f.write("1.0 2.0 3.0\n4.0 5.0 6.0\n7.0 8.0 9.0")

res = np.loadtxt('data.txt')
print(res)

data = np.array([[2.0,4.0,6.0],[44.0,62.0,52.0],[34.0,56.0,64.0]])
np.savetxt("output.txt",data,delimiter=' ',fmt='%1.1f')

res = np.loadtxt('output.txt')
print(res)

print("\n----csv file----\n")

with open('data.csv','w') as f:
    f.write("1.0,2.0,3.0\n4.0,5.0,6.0\n7.0,8.0,9.0")

data = np.genfromtxt('data.csv', delimiter=',')  # yaha delimiter me vhi dalna jo elements ke bichme ho eq: space ya coma
print(data)

print("\n----linear equation----\n")

a1 = np.array([[3,2],[1,2]])    # here it is representing 3x+2y=5 and x+2y=6
a2 = np.array([5,6])

res = np.linalg.solve(a1,a2)  # here it is finding tha values of variables
print(res)

print("\n----matrix inverse----\n")

a1 = np.array([[3,2],[1,2]])
a2 = np.array([5,6])

a1_inv = np.linalg.inv(a1)     # finding inverse
print(a1_inv)

res = np.dot(a1_inv,a2)   # multiplication
print(res)