from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0,8 * np.pi,1000, endpoint=True)


plt.plot(t, signal.square(t))
plt.plot(t, np.sin(t))

plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Sine on Square Wave')

plt.axhline(y = 0, color = 'k')

plt.savefig('sinOnSquare.png')
plt.show()