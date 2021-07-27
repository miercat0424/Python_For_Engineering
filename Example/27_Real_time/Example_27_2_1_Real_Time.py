import numpy as np
import matplotlib.pyplot as plt

# plt의 X , Y 축을 설정하는 방법
plt.axis([0,10,0,1])

delay = 0.5               # Seconds

for i in range(10):
    y = np.random.random()
    plt.scatter(i,y)
    plt.pause(delay)    # Making a time in plt

# plt.show()