print("-----------------------------1-------------------------------")

for x in range(10):  #'range' it will consider 0-9
    print(x)
print("-----------------------------2-------------------------------")

for x in range(1,10,2):
    print(x)
print("-----------------------------3-------------------------------")

for x in range(10, 1,-2):
    print(x)
print("-----------------------------4-------------------------------")

for x in range(9,0,-1):
    pass
    print("Python")
print("-----------------------------5-------------------------------")

n1 = int(input("num = "))

for x in range(1,11,1):
    print(n1 ,"*" , x , "=" , n1*x)
print("-----------------------------6-------------------------------")

for x in range(1,11,1):
    if x>5:
        break
    print(n1 ,"*" , x , "=" , n1*x)

print("-----------------------------7-------------------------------")

for x in range(1,11,1):
    if x==5:
        continue
    print(n1 ,"*" , x , "=" , n1*x)

print("-----------------------------8-------------------------------")

for x in range(1,11,1):
    if (x*n1)%2 == 0:
        continue
    print(n1 ,"*" , x , "=" , n1*x)
print("-----------------------------9-------------------------------")

for x in range(3):
    for y in range(5):
        print(x,y)

print("-----------------------------10-------------------------------")

for x in range(2,5):
    for y in range(1,11):
        print(x,"*",y,"=",x*y)
print("-----------------------------11-------------------------------")

for x in range(0,10,1):
    for y in range(1,x,1):
        print("*" , end=" ")
    print()

print("-----------------------------12-------------------------------")

for x in range(0, 10, 1):
    for y in range(1, x, 1):
       print(y, end=" ")
    print()

print("-----------------------------13-------------------------------")

i=1
while (i<10):
    print(i)
    i+=1

print("-----------------------------14-------------------------------")

while True:   #idher true ki vajah se loop infinite chalega
    n = int(input("enter any number and 0 exit"))
    if n == 0:
        break
    print(n)

print("-----------------------------15-------------------------------")

str = "python program"
print(str[2])   # to print according to index number

print("-----------------------------16-------------------------------")

str = "python program"
print(str[0::2])   # [starting:ending:inc or dec]

print("-----------------------------17-------------------------------")

str = "python program"
print(str[-1::-5])   # for right to left

print("-----------------------------18-------------------------------")

str = "python program"
l = len(str)
print(l)
for x in range(l):
    print(str[x])

print("-----------------------------19-------------------------------")

print(ord("a"))  #to print ascii code
print(chr(97))   #to print chr of number

print("-----------------------------20-------------------------------")

l=[10,20,30,40,"python",[1,2,3]]  # in  list we use square bracket and use ',' to seperate the elements
print(type(l))
print(l[4])
print(l[4][1])
print(l[-4])
print(l[-1::-1])

for x in l:
    print(x)

# print("-----------------------------21-------------------------------")
#
# t=[10,20,30,40,53,3]
# s=int(input())

print("-----------------------------22-------------------------------")

k=[]
k.append(55)
k.append(73)
k.insert(1,39)
k.extend([5,"python","java"])
k.pop()  #to delete last element
k.remove('python')   #to delete specific
k.remove(55)
print(k)