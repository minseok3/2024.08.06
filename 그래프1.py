import matplotlib.pyplot as plt

labels = ['english', 'math', 'science', 'history']
sizes = [45,30,15,10]

plt.clf()
plt.pie(sizes, labels= labels, autopct= '%1.1f%%',
        startangle=140, colors= ['lightblue', 'lightgreen', 'lightcoral', 'lightsalmon'])

plt.title('subjects distribution')
plt.show()