import numpy as np
import matplotlib.pyplot as plt
import os

try: os.mkdir('results')
except OSError: pass
w = open('results/task_01_40-506C_CHURSINA_8.txt', 'w')
print('x\tf(x)\n', file = w)
dx = 0.05
x = np.arange(-10, 10 + dx, dx)
A = 9.66459
f = -abs(np.sin(x) * np.cos(A) * np.exp(abs(1 -
                (x**2 + A**2) ** 0.5 / np.pi)))
for i in range(0,len(x)):
    print(x[i],'\t',f[i], file = w)
w.close()

plt.plot(x,f)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()
    
            
        
    
