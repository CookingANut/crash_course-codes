import matplotlib.pyplot as plt

x_values = list(range(1,5001))
y_values = [number**3 for number in x_values]
plt.title("plot one", fontsize=24)
plt.xlabel("x=", fontsize =24)
plt.ylabel("y=x**3", fontsize=24)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=40)
plt.axis([0,5100,0,5100**3])
plt.tick_params(axis='both',labelsize=14)

plt.show()