print("---------------------------------QUESTION 1--------------------------------------\n")

d={1:"hello",2:"there",3:"!!",4:"myself",5:"Shivam"}
print(d)
# print(d.clear())
print(d.copy()) #USED TO PRINT THE COPY OF THE DICTIONARY
print(d.items()) #USED TO PRINT EACH KEY AND ITS VALUE IN TUPLE  SEPARATED BY COMMA AND IN THE FORM OF LIST
print(d.keys()) #USED TO PRINT THE KEY VALUES OF A DICTIONARY IN THE FORM OF LIST
d2={6:"i",7:"live",8:"in",9:"jaipur",10:"rajasthan"}
d2.update(d) #UPDATES d WITH VALUES OF d2 AND VALUES OF d2 COMES FIRST IN THE RESULTANT DICTIONARY
print(d2)
print(d.values())
print(d.pop(1)) #USED TO DELETE A SPECIFIED KEY
print(d.popitem()) #USED TO PRINT THE LAST INSERTED KEY AND ITS VALUE FROM THE DICTIONARY

""" STACK AND QUEUE """

print("\n---------------------------------STACK--------------------------------------")

""" STACK """ #STACK FOLLOWS LIFO

s=[]
while True:
    c=int(input('''
    1.Insert element
    2.Pop element
    3.Peek element
    4.Display stack
    5.Exit\n
    '''))
    if c==1:
        n=input("enter values : ")
        s.append(n)
        print(s)
    elif c == 2:
        if len(s) == 0:
            print("empty stack")
        else :
            p = s.pop()
            print(p)
            print(s)
    elif c == 3:
        if len(s) == 0:
            print("empty stack")
        else:
            print("Last stack value: ", s[-1])
    elif c == 4:
        print(s)
    elif c == 5:
        break
    else:
        print("Invalid input!!!")

print("\n---------------------------------QUEUE--------------------------------------\n")

""" QUEUE """

q=[10,20,30,40,50,60] #QUEUE FOLLOWS FIFO
print("Queue : ",q)
n=int(input("enter a value : "))
q.append(n)
print("Enqueue :",q) #USED TO ENTER A ELEMENT IN A QUEUE
del q[0]
print("DeQueue : ",q)
print("first element :" , q[0])
print("last element : ",q[-1])

print("\n---------------------------------TUPLE--------------------------------------\n")

""" Tuple """

t1=(10,20,30,40,50)
print(t1)
l=len(t1)
for x in range(l):
    print(t1[x])
t2=(10,"jaipur",20,"ajmer",30,"delhi")
for x in t2:
    print(x)
t3=(t1,t2) #TO MAKE A NESTED TUPLE
print(t3)
print(t1+t2) #TO CONCATENATE TWO TUPLES
t= ('xyz') * 3 #REPEATITION OF TUPLES
print(t)
t=("xyz",)*3
print(t)
t=(1,2,3,4,5)
print(t[1:]) #SLICING OF TUPLE
print(t[::-1])
print(t[2:4])
print(len(t))
l=[10,20,30,40,50]
print(tuple(l)) #CONVERTING A LIST INTO TUPLE
print(min(t))
print(max(t))
print(t.count(2)) #COUNT THE NUMBER OF SPECIFIC ELEMENTS IN TUPLE
print(t.index(2)) #PRINTS THE INDEX OF SPECIFIC ELEMENT
print(sum(t))

print("\n---------------------------------SETS---------------------------------------")

""" SETS """

s={10,20,30,40,50}
print("\n")
print(s)
print(type(s))
s={10,20,"true",1,"false",0,40,50}
print(s)
s.add("mango")
print(s)
s1={1,2,3,4,5}
s2={6,7,8,9,10}
s3=s2.union(s1)
print(s3)
s4=s1 | s2
print(s4)

print("\n---------------------------------QUESTION 2--------------------------------------")

""" Write a function for basic math operations like add,multiply,subtract,divide 
and use this in your program, take 2 number input from user."""

def maths(a=0, b=0):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)

    if b != 0:
        print(f"Division: {a / b:.2f}")
    else:
        print("Division Cannot divide by zero")


a = int(input("\nenter value of a :"))
b = int(input("enter value of b : "))

maths(a,b)

print("---------------------------------QUESTION 3--------------------------------------")

""" Write a program to check Palindrome Number """

s = input("\nEnter the string: ")
length = len(s)
mid = length // 2

rev = -1
for a in range(mid):
    if s[a] == s[rev]:
        rev -= 1
    else:
        print(s, "is not a palindrome")
        break
else:
    print(s, "is a palindrome")