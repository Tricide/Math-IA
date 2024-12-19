from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0,8 * np.pi,1000, endpoint=True)


plt.plot(t, signal.square(t))
plt.plot(t, (4/np.pi)*(np.sin(t*3)/3 + np.sin(t) + np.sin(t*5)/5 + np.sin(t*7)/7 + np.sin(t*9)/9 + np.sin(t*11)/11))

plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Sine on Square Wave')

plt.axhline(y = 0, color = 'k')

plt.savefig('newThing2.png')
plt.show()