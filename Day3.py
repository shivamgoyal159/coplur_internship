d = {1:"python",2:"java",'name':"program"}
print(d)

d = {1:"python",2:"java",'name':"program"}
print(d['name'])

d = {1:"python",2:"java",'name':"program",4:{1:"one",2:"two"}}
print(d[4][1])

dict={}
print(dict)
dict[0]="hello"
dict[1]="hey"
dict[2]="hii"
print(dict)
print(dict[2])
del(dict[0])
print(dict)
dict2=dict.copy()
print(dict2)
dict2.clear()
print(dict2)
dict.pop(1)
print(dict)
dict.popitem()
print(dict)#to remove last element

print("------------------------------------------------------------")

dict={}
print(dict)
dict[0]="hello"
dict[1]="hey"
dict[2]="hii"
print(dict)

dict2={}
print(dict2)
dict2[0]="hell"
dict2[1]="heyyyyyyy"
dict2[2]="holaaa"
print(dict2)

print(dict.get(2))
print(dict.items())
print(dict.keys())
dict.update(dict2)
print(dict)

print("------------------------------------------------------------")


t = (10,20,30,40,50,30,20,True,False)
print(t)
print(type(t))

l = len(t)
for x in range(l):
    print(x,t[x])

for x in t:
    print(x)

for x in t:
    print(t[2])

t2=('a','b')
# t4=('xyz')*3
t4=('xyz',)*3
t3=(t,t2,t4)
print(t3)
print(t3[1:])
print(t3[::-1])
print(t3[1:5])  #tuple only have 0-3 elements but no issue as it will print the elememts present in the tuple

print("------------------------------------------------------------------------------")

l=[10,20,30]
t=tuple(l)   #convert list to typle
print(t)
print(min(t))
print(max(t))
print(sum(t))
print(t.count(20))
print(t.index(30))

print("------------------------------------------------------------------------------")

s = {"a","b","c","d","e"}
print(s)

s.add("mango")
print(s)

s2 = {"apple","pineapple","grape"}
s3 = s.union(s2)
print(s3)

s4 = s | s2  #same as union
print(s3)

s5=set()
s6=set()
for i in range(5):
    s5.add(i)
for i in range(3,9):
    s6.add(i)

s7=s5.intersection(s6)
print(s7)

s8 = s5 & s6  #another way of intersection
print(s8)

print("------------------------------------------------------------------------------")

def my_fun(a,b):       #default value is set as 0
    res = a+b
    return res

sum=my_fun(12,15)
print(sum)

def fun(*city):
    print(city[1])

fun("a","b","c")


def function2(*city):
    print(city[1])

function2("mumbai","chennai","jaipur")


def function(city3,city2,city1):
    print("the first city is " + city3)

function(city1="mumbai",city2="chennai",city3="jaipur")


def function2(**city):
    print(city['f1'])

function2(f1="mumbai",f2="chennai",f3="jaipur")



f = open("new1.txt", "w")    #eak new file bani h usme ye print karaya h
f.write("this is first time ")
f.write("this is line 2")
f.close()


f = open("new1.txt", "r")
for x in f:
    print(x)


file = open("new1.txt","r")   # another way to read
print(file.read())

with open("new1.txt")as file:   # another way to read
    data = file.read()
print(data)


with open("new1.txt")as file:   # another way to read
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)