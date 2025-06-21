a=5
b=3
print(id(a))
print(id(b))

name = "helloooo"
print(name.upper()) # use to convert in upper letters
print(name.center(30)) #use to give margin from left and right
print(name.center(30 , ">"))
print(name.count("o")) # use to count specific letter
print(name.expandtabs(4))
#samaj nhi aaya
c=":"
seq = ("a","b","c")
print(c.join(seq)) #to join

str="Shivam\nis\nhuman"
print("string before splitting" +str)
print("string after splitting:")
print(str.splitlines())

l="tipon"
e="71633"
str="ye meri jindagi h!!!"
encoding = str.maketrans(l,e)
print(str.translate(encoding))

