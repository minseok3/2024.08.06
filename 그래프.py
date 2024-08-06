import matplotlib.pyplot as plt

x = [17, 18, 19, 20, 21, 22, 23]
y = [65, 70, 70, 75, 80, 85, 85]

plt.plot(x,y, marker= '*', linestyle= "-", color= 'red', label= "temp" )
plt.title("daily humidity")
plt.xlabel('time')
plt.ylabel('humidity')
plt.show()
plt.legend()
plt.grid(True)
plt.savefig('./linechart.png')