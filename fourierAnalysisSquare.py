import numpy as np
import matplotlib.pyplot as plt
import scipy

#using a wav file
file = 'cello.wav'


rate, aud_data = scipy.io.wavfile.read(file)


t = np.linspace(0, 8 * np.pi,1000, endpoint=True)

#wav file is mono.
channel_1 = aud_data[:]

fourier = np.fft.fft(channel_1)

freq = np.fft.fftfreq(len(channel_1), d=x[1]-x[0])


plt.plot(freq, abs(fourier) **2)
plt.show()