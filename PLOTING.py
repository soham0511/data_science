import matplotlib.pyplot as plt

x=[1,4,7,9,12]
y=[2,5,12,68,34]
plt.plot(x,y,'b--')
plt.plot(y,x,'r--')
plt.xlabel("Time")
plt.ylabel("Stakes")
plt.title("The ShareMarket")
plt.show()