#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3

plt.plot(np.arange(len(y)), y, color='red', linewidth=1.0)
plt.show()
