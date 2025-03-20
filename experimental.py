import numpy as np
import matplotlib.pyplot as plt

def square_wave(t, amplitude, frequency, duty_cycle):
    """Generates a square wave signal."""
    return amplitude * (np.where((t % (1/frequency)) < (duty_cycle/frequency), 1, -1))

# Parameters
amplitude = 1
frequency = 1  # Hz
duty_cycle = 0.5  # 50%
t = np.linspace(0, 32, 1000, endpoint=False)  # Time vector

# Generate the square wave
square_wave_signal = square_wave(t, amplitude, frequency, duty_cycle)

# Compute the Fourier Transform
fft_result = np.fft.fft(square_wave_signal)
frequencies = np.fft.fftfreq(len(t), 1/frequency)

# Plot the magnitude spectrum
#plt.plot(frequencies, np.abs(fft_result))
#plt.xlabel("Frequency (Hz)")
#plt.ylabel("Magnitude")
#plt.title("Fourier Transform of Square Wave")
#plt.xlim(-10, 10)  # Set x-axis limits for better visualization
#plt.show()

plt.plot(t,square_wave_signal)
plt.show()