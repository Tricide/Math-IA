import numpy as np
import matplotlib.pyplot as plt
import scipy

#using a wav file
file = 'cello.wav'
rate, aud_data = scipy.io.wavfile.read(file)


#Convert wav file is mono.
if aud_data.ndim > 1:
    aud_data = aud_data[:, 0]
else:
    pass

n = len(aud_data)
yf = np.fft.fft(aud_data)
xf = np.fft.fftfreq(n, 1/rate)

plt.plot(xf, np.abs(yf))
plt.title('Fourier Transform')
plt.xlabel('Hertz')
plt.ylabel('Amplitude')
plt.show()