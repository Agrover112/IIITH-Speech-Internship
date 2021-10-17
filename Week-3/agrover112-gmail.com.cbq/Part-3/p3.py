import wave

import audioread
import librosa
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scipy
import scipy.io.wavfile as wav
import scipy.signal as signal
import scipy.signal.windows as w
from mpl_toolkits.mplot3d import Axes3D
from scipy.fftpack import fft

f = wave.open('Part-1/p1.wav', 'r')
#y, sr = librosa.load('Part-1/p1.wav')
sample_rate, samples = wav.read('Part-1/p1.wav')

frame_rate = f.getframerate()
sampling_rate = 44100
sig_enc = f.readframes(-1)  # Read all the frames in bytes (hex) format
sig = np.frombuffer(sig_enc, np.int16)  # convert bytes to int16
time = np.arange(0, len(sig))/frame_rate   # Time = No of frames/ Frame Rate

"""Voiced Segment NFFT changes 256,512,1024
start = 43659  # 1.01*sampling_rate 0.990
stop = 44541  # 1.03*sampling_rate  1.01
seg = sig[start:stop]
seg_len = len(seg)
time_seg = np.arange(0, len(seg))/frame_rate
#f, t, Zxx = signal.stft(seg, sample_rate, nperseg=1000)
NFFT=256
x=fft(sig,NFFT)
fVals=np.arange(start = -NFFT/2,stop = NFFT/2)*sample_rate/NFFT
plt.plot(fVals,np.abs(x),'b')
plt.title('STFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()"""

"""Voiced Segment with changing window's
#start = 43659  # 1.01*sampling_rate 0.990
#stop = 44541  # 1.03*sampling_rate  1.01
start = 43659  # 1.01*sampling_rate 0.990
stop = 44541  # 1.03*sampling_rate  1.01
seg = sig[start:stop]
seg_len = len(seg)
time_seg = np.arange(0, len(seg))/frame_rate
#f, t, Zxx = signal.stft(seg, sample_rate, nperseg=1000)
#window=signal.hamming(882)
window=w.hanning(M=882)
NFFT=256
x=fft(seg,NFFT)
fVals=np.arange(start = -NFFT/2,stop = NFFT/2)*sample_rate/NFFT  #normalizing 
#nVals = np.arange(start = 0,stop = NFFT)
plt.plot(fVals,np.abs(x),'b')
plt.title('FFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()
"""


""" Different window sizes
start = 43659  # 0.990 *sampling_rate 
stop = 44100  # 1*sampling_rate  

start2= 43659  # 0.990 *sampling_rate 
stop2= 44541  # 1.01*sampling_rate  

start3= 43659  # 0.990 *sampling_rate 
stop3= 45864  # 1.04*sampling_rate  
seg = sig[start:stop]
seg2 = sig[start2:stop2]
seg3 = sig[start3:stop3]


seg_len = len(seg)
time_seg = np.arange(0, len(seg))/frame_rate
#f, t, Zxx = signal.stft(seg, sample_rate, nperseg=1000)
#window=signal.hamming(882)
window=w.hanning(M=882)
NFFT=4096
x=fft(seg,NFFT)
fVals=np.arange(start = -NFFT/2,stop = NFFT/2)*sample_rate/NFFT  #normalizing 


x2=fft(seg2,NFFT)
fVals2=np.arange(start = -NFFT/2,stop = NFFT/2)*sample_rate/NFFT  #normalizing 



x3=fft(seg3,NFFT)
fVals3=np.arange(start = -NFFT/2,stop = NFFT/2)*sample_rate/NFFT  #normalizing 

plt.plot(fVals,np.abs(x),'b')
plt.title('FFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.savefig('10ms')
plt.plot(fVals2,np.abs(x2),'b')
plt.title('FFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.savefig('20ms')
plt.plot(fVals3,np.abs(x3),'b')
plt.title('FFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.savefig('50ms')"""


# UnVoiced Segment NFFT changes 256,512,1024
"""
start = 50626  # 1.1480*sampling_rate 1.1480
stop = 51508  # 1.158*sampling_rate  1.1680
seg = sig[start:stop]
seg_len = len(seg)
time_seg = np.arange(0, len(seg))/frame_rate
#f, t, Zxx = signal.stft(seg, sample_rate, nperseg=1000)
NFFT=256
x=fft(sig,NFFT)
fVals=np.arange(start = -NFFT/2,stop = NFFT/2)*sample_rate/NFFT
plt.plot(fVals,np.abs(x),'b')
plt.title('STFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.savefig('u256_fft')

NFFT=512
x2=fft(sig,512)
fVals2=np.arange(start = -NFFT/2,stop = NFFT/2)*sample_rate/NFFT
plt.plot(fVals2,np.abs(x2),'b')
plt.title('STFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.savefig('u512_fft')

NFFT=1024
x3=fft(sig,1024)
fVals3=np.arange(start = -NFFT/2,stop = NFFT/2)*sample_rate/NFFT
plt.plot(fVals3,np.abs(x3),'b')
plt.title('STFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.savefig('u1024_fft')
"""
"""
start = 50626  # 1.1480*sampling_rate 1.1480
stop = 51508  # 1.158*sampling_rate  1.1680
seg = sig[start:stop]
seg_len = len(seg)
time_seg = np.arange(0, len(seg))/frame_rate
#f, t, Zxx = signal.stft(seg, sample_rate, nperseg=1000)
hanning=w.hanning(M=882)
hamming=w.hamming(M=882)
rectangular=w.kaiser(M=882,beta=0)
NFFT=256
x1=fft(seg*hanning,NFFT)
x2=fft(seg*hamming,NFFT)
x3=fft(seg*rectangular,NFFT)
fVals=np.arange(start = -NFFT/2,stop = NFFT/2)*sample_rate/NFFT
plt.plot(fVals,np.log(np.abs(x1)),'b')
plt.title('FFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.savefig('u256_hanning')

plt.plot(fVals,np.log(np.abs(x2)),'b')
plt.title('FFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.savefig('u256_hamming')

plt.plot(fVals,np.log(np.abs(x3)),'b')
plt.title('FFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.savefig('u256_rectangular')
"""

# Unvoiced different window sizes
"""
start = 50626  # 0.990 *sampling_rate 1.1480
stop =  51067  # 1*sampling_rate      1.1580

start2= 50626  # 0.990 *sampling_rate  1.1480
stop2= 51508 # 1.01*sampling_rate   1.1680

start3= 50626  # 0.990 *sampling_rate 
stop3= 52831  # 1.04*sampling_rate  1.198
seg = sig[start:stop]
seg2 = sig[start2:stop2]
seg3 = sig[start3:stop3]


seg_len = len(seg)
time_seg = np.arange(0, len(seg))/frame_rate
#f, t, Zxx = signal.stft(seg, sample_rate, nperseg=1000)
#window=signal.hamming(882)
window=w.hanning(M=882)
NFFT=4096
x=fft(seg,NFFT)
fVals=np.arange(start = -NFFT/2,stop = NFFT/2)*sample_rate/NFFT  #normalizing 


x2=fft(seg2,NFFT)
fVals2=np.arange(start = -NFFT/2,stop = NFFT/2)*sample_rate/NFFT  #normalizing 



x3=fft(seg3,NFFT)
fVals3=np.arange(start = -NFFT/2,stop = NFFT/2)*sample_rate/NFFT  #normalizing 

plt.plot(fVals,np.abs(x),'b')
plt.title('FFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.savefig('10ms')
plt.plot(fVals2,np.abs(x2),'b')
plt.title('FFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.savefig('20ms')
plt.plot(fVals3,np.abs(x3),'b')
plt.title('FFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.savefig('50ms')
"""
