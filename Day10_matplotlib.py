from cProfile import label

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,100)
y = np.sin(x) # to calculate sin values

"""both are of tan"""
# y = np.sin(x)/np.cos(x)
# y = np.tan(x)
print(y)

# plt.plot(x,y,label = 'sin(x)',color='red',linestyle = '-' )
# plt.plot(x,y,label = 'sin(x)',color='red',linestyle = '--' )
# plt.plot(x,y,label = 'sin(x)',color='red',linestyle = '-.' )
plt.plot(x,y,label = 'sin(x)',color='red',linestyle = '-.' )


plt.title('Line plot of sin(x)')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.legend()

plt.grid(True)
# plt.grid(False)

plt.show()







a = np.random.rand(50)
b = np.random.rand(50)
# plt.plot(x,y,color='red',linestyle = '-.' )
plt.scatter(a,b,color='red',alpha = 0.7 )   # aplha mean transparancy ki kitna light dhikega kitna dark dhikega

plt.title('scatter plot')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.legend()

plt.grid(True)

plt.show()







categories = ['A','B','D','E']
values = [1,2,3,4]

plt.bar(categories,values,color='red')

plt.title('bar plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.legend()

plt.show()







labels = ['A','B','D','E']
sizes = [1,2,3,4]

# plt.pie(categories,values,color='red')
plt.pie(sizes,labels=labels,autopct='%1.1f%%',startangle = 140,shadow=True,explode = (0,0.1,0,0))
plt.title('pie Chart')

plt.show()