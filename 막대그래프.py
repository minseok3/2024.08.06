import matplotlib.pyplot as plt

categories = ["apple", 'banana', 'orange','strawberry', 'grape' ]

values = [25, 30, 15, 20, 35]

plt.clf()
plt.bar(categories, values, color= 'skyblue')
plt.title("fruit sales")
plt.xlabel('fruit')
plt.ylabel('sales')
plt.show()
# plt.savefig('./linechart.png')