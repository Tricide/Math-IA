import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import signal

#using a wav file
file = 'cello.wav'


rate, aud_data = scipy.io.wavfile.read(file)


t = np.linspace(0, 8 * np.pi,1000, endpoint=True)


square_wave = signal.square(t)

fft_result = np.fft.fft(square_wave)
#wav file is mono.

freq = np.fft.fftfreq(len(t),1)

plt.plot(freq, abs(fft_result))
plt.show()