import audioread
import wave
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import scipy
import librosa
import scipy.io.wavfile as wav
import scipy.signal as signal
f = wave.open('/mnt/c/Users/agrov/OneDrive/Desktop/IIITH/Week-3/agrover112-gmail.com.cbq/p1.wav','r')
y,sr=librosa.load('/mnt/c/Users/agrov/OneDrive/Desktop/IIITH/Week-3/agrover112-gmail.com.cbq/p1.wav')
sample_rate, samples = wav.read('/mnt/c/Users/agrov/OneDrive/Desktop/IIITH/Week-3/agrover112-gmail.com.cbq/p1.wav')

print(librosa.get_samplerate('/mnt/c/Users/agrov/OneDrive/Desktop/IIITH/Week-3/agrover112-gmail.com.cbq/p1.wav'))
frame_rate=f.getframerate()
sampling_rate=44100
sig_enc=f.readframes(-1) #Read all the frames in bytes (hex) format
sig=np.frombuffer(sig_enc,np.int16) #convert bytes to int16
time=np.arange(0,len(sig))/frame_rate   # Time = No of frames/ Frame Rate     
def time_domain_plot():
    ax1 = plt.subplot(221)
    ax1.set_xlabel("Time [sec]")
    ax1.set_ylabel("Amplitude")
    ax1.plot(time,sig)
    ax2 = plt.subplot(223)
    f, t, Zxx = signal.stft(samples, fs=sample_rate,nperseg=256)
    ax2.pcolormesh(t, f, np.abs(Zxx),shading='auto')
    ax2.set_ylabel('Frequency [Hz]')
    ax2.set_xlabel('Time [sec]')
    plt.show()
    #plt.savefig('time_domainplot.png')

time_domain_plot()


def plot_3Dspectrogram():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    f, t, Sxx = signal.spectrogram(samples, fs=sample_rate)
    ax.plot_surface(f[:, None], t[None, :], 20.0*np.log10(Sxx), cmap=matplotlib.cm.Blues)
    ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel("Time (s)")
    ax.set_zlabel("Power (dB)")
    plt.show()
  
