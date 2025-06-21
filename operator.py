a=int(input("a "))
b=int(input("b "))
z=a+b  #arithmetic operator
print(z)

c=(a-b)
d=(a*b)
e=(a%b)
f=(a/b)
g=(a**b)
h=(a//b)
i=(a+b)/4

a+=b

print(f"{c},{d},{e},{f:.2f},{g},{h},{i:.2f},{a}")

if a is b:
    print(b)

l=3
s=6

print(bin(l))  #bin convert into binary
print(bin(s))
print(l & s)

if s % 2 == 0 :
    print("number is even")
    if l==0:
        print("it is l")
else:
    print("number is odd")


per = int(input("percentage ="))
if per>60:
    print("Grade A")
elif per < 60 and per > 50:
    print("Grade B")
else per < 50 and per > 40:
    print("Grade C")
else:
    print("Grade F")