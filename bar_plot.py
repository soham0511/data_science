import matplotlib.pyplot as plt
import numpy as np
# x=[i for i in range(10)]
# y=[3,6,8,5,9,1,2,4,7,11]
# plt.bar(x,y,width=0.3,color="red")
# plt.show()

x=[i for i in range(10)]
y=[3,6,8,5,9,1,2,4,7,1]
z=[2,5,1,6,8,2,2,6,9,1]
plt.bar(x,y,width=0.3,color="red",label="2019")
x=[i+0.3 for i in range(10)]
plt.bar(x,z,width=0.3,color="blue",label="2020")
plt.legend()
plt.show()