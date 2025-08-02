import numpy as np
import matplotlib.pyplot as plt
y=[10,20,30,40]
quantiles=np.linspace(0,1,len(y))
sorted_y=np.sort(y)
plt.plot(quantiles,sorted_y,marker="o")
plt.xlabel("quantiles")
plt.ylabel("values")
plt.title("Quantile plot")
plt.grid(True)
plt.show()

