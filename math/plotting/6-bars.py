#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

labels = ['Farrah', 'Fred', 'Felicia']

apples = fruit[0]
bananas = fruit[1]
oranges = fruit[2]
peaches = fruit[3]

fig, ax = plt.subplots(figsize=(8, 6))

ax.bar(labels, apples, label='apples', color='red')
ax.bar(labels, bananas, bottom=apples, label='bananas', color='yellow')
ax.bar(labels, oranges, bottom=apples + bananas, label='oarnges', color='#ff8000')
ax.bar(labels, peaches, bottom=apples + bananas + oranges, label='peaches', color='#ffe5b4')

ax.set_ylabel('Quantity of Fruit')
ax.set_xlabel('Quarters')
ax.set_title('Number of Fruit per Person')
ax.set_ylim(0, 70)
ax.legend(loc='upper right')

plt.tight_layout()
plt.show()