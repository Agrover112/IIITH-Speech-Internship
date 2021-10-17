"""Pls uncomment the plt.plot() to see the plots or else view the saved figures"""


import wave

import audioread
import librosa
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy import signal
from scipy.io import wavfile
import parselmouth
f = wave.open(
    '/mnt/c/Users/agrov/OneDrive/Desktop/IIITH/Week-2/agrover112.cbq/Part-3/H_MKB.wav', 'r')
y, sr = librosa.load(
    '/mnt/c/Users/agrov/OneDrive/Desktop/IIITH/Week-2/agrover112.cbq/Part-3/H_MKB.wav')

print(librosa.get_samplerate(
    '/mnt/c/Users/agrov/OneDrive/Desktop/IIITH/Week-2/agrover112.cbq/Part-3/H_MKB.wav'))
snd = parselmouth.Sound(
    '/mnt/c/Users/agrov/OneDrive/Desktop/IIITH/Week-2/agrover112.cbq/Part-3/H_MKB.wav')

frame_rate = f.getframerate()
sampling_rate = 44100
print(f.getparams())


sig_enc = f.readframes(-1)  # Read all the frames in bytes (hex) format
sig = np.frombuffer(sig_enc, np.int16)  # convert bytes to int16
time = np.arange(0, len(sig))/frame_rate   # Time = No of frames/ Frame Rate

plt.title("Time Domain plot")
plt.xlabel("Time")
plt.ylabel("Amplitude")
# plt.plot(time,sig)
# plt.savefig('time_domainplot.png')


""" UNVOICED Region Analysis"""
start = 148969  # 3.378*sampling_rate
stop = 159851  # 3.398*sampling_rate
seg = sig[start:stop]
seg_len = len(seg)
time_seg = np.arange(0, len(seg))/frame_rate


""" VOICED Region Analysis"""
ustart = 299880  # 6.8*sampling_rate)
ustop = 300762  # 6.82*sampling_rate)
useg = sig[ustart:ustop]
useg_len = len(useg)
utime_seg = np.arange(0, len(useg))/frame_rate


def plot_segment(segment, segment_length, segment_time):
    plt.title("Segment in time domain")
    plt.plot(np.linspace(0, segment_length/frame_rate, segment_length), segment)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.show()

    # plt.savefig('segment_plot.png')


def spectrogram(segment):
    plt.title("Segment Spectrogram")
    plt.specgram(segment, Fs=sampling_rate)
    plt.xlabel("Time")
    plt.ylabel("Frequency(Hz)")
    # plt.show()
    plt.savefig('segement_spectrogram.png')


def zero_crossing(seg):
    # Extremely Large number of zero crossings
    print("Number of zero crossings :", sum(librosa.zero_crossings(seg)))


def energy(seg, time_seg):
    seg = np.abs(seg)
    energy = np.square(seg, dtype=np.float64)
    max = np.max(energy)
    print(max)
    plt.title("Segment Energy Plot")
    plt.xlabel("Time(s)")
    plt.ylabel("Energy (J)")
    plt.plot(time_seg, energy)
    plt.show()
    # plt.savefig('segement_energy.png')


def auto_correlate(sig, start, stop):
    #acorr = scipy.signal.correlate(sig[start:stop],sig[start:stop],mode = 'same',method = 'auto')
    acorr = librosa.autocorrelate(sig[start:stop])
    plt.xlabel('Lags')
    plt.ylabel('Autocorrelation ')
    plt.title("Segment Autocorrelation Plot")
    plt.plot(acorr)    # Highly unccorelated
    plt.show()
    # plt.savefig('segement_autocorelation.png')


#plot_segment(seg, seg_len, time_seg)
# spectrogram(seg)
# zero_crossing(seg)
# energy(seg,time_seg)
# auto_correlate(sig,start,stop)

#plot_segment(useg, useg_len, utime_seg)
# spectrogram(useg)
# zero_crossing(useg)
# energy(useg,utime_seg)
# auto_correlate(sig,ustart,ustop)
def pitch(start,stop,plot=False):
    snd_part = snd.extract_part(from_time=start,to_time = stop, preserve_times=True)
    pitch = snd_part.to_pitch()
    pitch_values = pitch.selected_array['frequency']
    pitch_values[pitch_values==0] = np.nan
    max = np.nanmax(pitch_values)
    min= np.nanmin(pitch_values)
    print("The maximum pitch frequency is = {maximum} Hz , at time t = {time} seconds".format(maximum=max ,time =  pitch.xs()[np.nanargmax(pitch_values)]))
    print("The minimum pitch frequency is = {minimum} Hz , at time t = {time} seconds".format(minimum=min, time =  pitch.xs()[np.nanargmin(pitch_values)]))

    # replacing  samples by NaN 
    plt.plot(pitch.xs(), pitch_values,'o', markersize=5, color='w')
    plt.plot(pitch.xs(), pitch_values,'o', markersize=4)
    plt.grid(True)
    plt.ylim(0, pitch.ceiling/2)
    plt.ylabel("Pitch in Hz")
    plt.xlabel("time in seconds")
    plt.show()
    



pitch(3.378,3.5)
pitch(6.78,6.84)
start=3.378
stop=3.5
snd_part = snd.extract_part(from_time=start,to_time = stop, preserve_times=True)
plt.plot(snd_part.xs(), snd_part.values.T)
plt.axvspan(3.439,3.441, color = 'red', alpha = 0.7, label = "Max-Pitch")
plt.axvspan(3.479,3.481, color = 'green' , alpha = 0.7, label = "Min-Pitch" )
plt.legend() 
plt.xlim([snd_part.xmin, snd_part.xmax])
plt.xlabel("time [s]")
plt.ylabel("amplitude")
plt.title('Time Domain Plot')
plt.savefig('Unvoiced.png')
plt.close()
start=6.78
stop=6.84
snd_part = snd.extract_part(from_time=start,to_time = stop, preserve_times=True)
plt.plot(snd_part.xs(), snd_part.values.T)
plt.axvspan(6.8,6.802, color = 'red', alpha = 0.7, label = "Max-Pitch")
plt.axvspan(6.81,6.812, color = 'green' , alpha = 0.7, label = "Min-Pitch" )
plt.legend() 
plt.xlim([snd_part.xmin, snd_part.xmax])
plt.xlabel("time [s]")
plt.ylabel("amplitude")
plt.title('Time Domain Plot')
plt.savefig('Voiced.png')
