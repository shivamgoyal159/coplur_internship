import numpy as np
import matplotlib.pyplot as plt

print("----------Question 1----------\n")

arr=np.array([[6,-8,73,-110],[np.nan,-8,0,94]])
print(arr)

arr=np.nan_to_num(arr,copy=True,nan=0.0)
print(arr)
print("-----------")

arr[:, [0, 1]] = arr[:, [1, 0]]
arr[:, [2, 3]] = arr[:, [3, 2]]
arr[:, [1, 3]] = arr[:, [3, 1]]
print(arr)
arr[[0, 1]] = arr[[1, 0]]
print(arr)

print("\n----------Question 2----------\n")

arr=np.array([[[3,4,5],[6,7,8]],[[1,4,0],[-1,-5,-6]]])
print(arr)
print(arr.shape)
arr=np.transpose(arr,(1,2,0))
print(arr)
print(arr.shape)

print("\n----------Question 3----------\n")

c_avg=np.nanmean(arr,axis=0)
a=np.nan_to_num(arr,nan=c_avg)
print(arr)
print(a)

print("\n----------Question 4----------\n")

import numpy as np
arr = np.array([[1, -2, 3], [-4, 5, -6]])
arr[arr < 0] = 0
print("Array after replacing negatives with 0:\n", arr)

print("\n----------Question 6----------\n")

d=np.array([1,2,3])
d1=np.array([78,98,44])
d3=np.median(np.concatenate((d,d1)))
print("average",(d+d1)/2)
print("median",np.median(d3))

print("\n----------Question 7----------\n")

e1=np.array([[1,2,5],[0,8,6]])
e2=np.array([[8,3,4],[6,0,0]])
print("mean: ",np.mean((np.concatenate((e1,e2)))))
print("median: ",np.median((np.concatenate((e1,e2)))))

print("\n----------Question 8----------\n")

u=np.array([[1,-2,3],[-1,3,-1],[2,-5,5]])
print("matrix first\n",u)
v=np.array([9,-6,17])
print("matrix second\n",v)
m=np.linalg.solve(u,v)
print("solution:\n ",m)
u_inv=np.linalg.inv(u)
print("inverse of first\n",u_inv)
res=u_inv.dot(v)
print("inverse:\n ",res)

print("\n----------Question 9----------\n")

sem1 = np.array([90, 80, 70, 60, 55])
sem2 = np.array([90, 80, 85, 99, 100])
subjects = np.arange(5)
bar_width = 0.35
x1 = subjects
x2 = subjects + bar_width
plt.bar(x1, sem1, width=bar_width, label='Sem 1', color='cyan')
plt.bar(x2, sem2, width=bar_width, label='Sem 2', color='purple')
plt.xlabel('Subject')
plt.ylabel('Marks')
plt.title('Comparison of Sem 1 and Sem 2 Marks')
plt.legend()
plt.grid(True,axis='y', alpha=0.3,color='grey')
plt.show()