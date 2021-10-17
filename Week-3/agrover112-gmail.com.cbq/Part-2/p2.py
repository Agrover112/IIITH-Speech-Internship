import wave

import audioread
import librosa
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import python_speech_features
from librosa import display

f = wave.open('Part-1/p1.wav', 'r')
y, sr = librosa.load('Part-1/p1.wav')

frame_rate = f.getframerate()
sampling_rate = 44100
print(f.getparams())


sig_enc = f.readframes(-1)  # Read all the frames in bytes (hex) format
sig = np.frombuffer(sig_enc, np.int16)  # convert bytes to int16
time = np.arange(0, len(sig))/frame_rate   # Time = No of frames/ Frame Rate


start = 19845  # 1.01*sampling_rate 0.450
stop = 24255  # 1.03*sampling_rate  0.550
seg = sig[start:stop]
seg_len = len(seg)
time_seg = np.arange(0, len(seg))/frame_rate




def plot_segment(segment, segment_length):
    plt.title("Segment in time domain")
    plt.plot(np.linspace(0, segment_length/frame_rate, segment_length), segment)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.show()


plot_segment(seg, seg_len)

frame_size = 4410  # 1/ndt
windowed_signal = np.hamming(frame_size) * seg
dt = 1/sr
freq_vector = np.fft.rfftfreq(frame_size, dt)  # d=dt
X = np.fft.rfft(windowed_signal)
log_X = np.log(np.abs(X))

fig, ax = plt.subplots()
ax.plot(freq_vector, log_X)
ax.set_xlabel('frequency (Hz)')
ax.set_title('Fourier spectrum')
plt.show()

cepstrum = np.fft.rfft(log_X)
df = freq_vector[1] - freq_vector[0]
quefrency_vector = np.fft.rfftfreq(log_X.size, df)  # df
fig, ax = plt.subplots()
ax.plot(quefrency_vector, cepstrum)
ax.set_xlabel('quefrency (s)')
ax.set_title('cepstrum')
plt.show()

valid = (quefrency_vector > 22050 & (quefrency_vector <= 1))
max_quefrency_index = np.argmax(np.abs(cepstrum)[valid])
f0 = 1/quefrency_vector[valid][max_quefrency_index]
print(f0) # Print the f0

fig, ax = plt.subplots()
mfccs = librosa.feature.mfcc(y=time_seg, sr=sr, lifter=22)
img = librosa.display.specshow(mfccs, x_axis='time', ax=ax)
fig.colorbar(img, ax=ax)
ax.set(title='MFCC')
ax.plot(mfccs)
plt.show()
#plt.savefig('liftered_mfccs')
