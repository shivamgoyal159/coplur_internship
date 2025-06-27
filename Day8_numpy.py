import numpy as np

print(np.__version__)

a = np.array([2,4,6])                                                     # 1 D array
a = np.array([[2,4,6],[32,62,62]])                                        # 2 D array
a = np.array([[[2,4,6],[32,62,77]],[[34,88,43],[34,54,88]]])              # 3 D array

print(a)
print(type(a))   # primary data structure in numpy is ndarray
print(a.dtype)   # data type

print("-----------------------------")

arr = np.array([35,620,73,16],dtype='S')      # |S3 yaha '3' highest length h
arr = np.array([35,62,77,16],dtype='i4')
arr = np.array(['dfhd','ebdrb','hrsb'],dtype='S')
# arr = np.array(['dfhd','ebdrb','hrsb'],dtype='i4')   # nhi chalega kyoki dtype int diya h aur element string me diye h
# arr = np.array([35,62,'h',16],dtype='i4')    # error aayega kutte char dalega to
print(arr)
print(arr.dtype)

print("------------------------------")

arr = np.array([]).dtype
print(arr)

print("------------------------------")

arr = np.zeros(5)   # to enter 0's
print(arr)

arr = np.ones(5)   # to enter 0's , 1D array
print(arr)

arr = np.ones((4,5))   #   2D array
print(arr)

arr = np.ones((4,5),order='F')   #   2D array
print(arr)

arr = np.arange(10)  #   2D array
print(arr)

arr = np.arange(1,10,2)
print(arr)

arr1 = np.linspace(0,5,num=10)    # (end - start) / num-1 =
print(arr1)

arr2 = np.linspace(0,5,num=10,endpoint= False)
print("\n" ,arr2)

arr2 = np.linspace(0,10,num=5,endpoint= False)     #false me end ka nhi leta jaise isme 10 nhi lera , false me shrif num lete h
print("\n" ,arr2)

arr2 = np.linspace(0,10,num=5,endpoint= True)     #false me end ka nhi leta jaise isme 10 nhi lera , false me shrif num-1 lete h
print("\n" ,arr2)

arr3 = np.linspace(0,5,num=10,retstep=True)    # array bhi dega aur ans ki value bhi dega(step size)
print("\n" ,arr3)

arr3 = np.linspace(0,10,num=5,retstep=False)   # sirf array dega
print("\n" ,arr3)

arr4 = np.random.rand(2,3)
print("\n" ,arr4)

arr4 = np.random.rand(2,3,7)
print("\n" ,arr4)

a = np.empty((2,3))     #garbage value deta h unlike random jo float value deta h
print(a)
print(a.dtype)


a = np.full((2,3),5)   #we can assign value which will we used
print(a)


arr = np.array([23,45,36,76])
print(arr)
print(arr[::2])

print("sum = " , arr[2]+arr[3])

arr = np.array([[23,45,36,76],[55,62,73,26]])  # 2D me
print(arr)
print(arr[0,1])
print(arr[1,1:4]) #printing specific element from a row
print(arr[0:2,1])

arr = np.array([[[23,45,36,76],[55,62,73,26]],[[43,51,66,62],[25,22,53,83]]])  #  3D me
print(arr)
# print(arr[0,1,2])
print(arr[1,0,1:3])


