import numpy as np
import matplotlib.pyplot as plt
import scipy

file = 'cello.wav'
rate, aud_data = scipy.io.wavfile.read(file)

duration = len(aud_data)/rate
time = np.arange(0, duration, 1/rate)

plt.plot(time, aud_data)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Cello A")
plt.show()