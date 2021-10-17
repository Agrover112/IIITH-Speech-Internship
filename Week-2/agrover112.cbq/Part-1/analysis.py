import audioread
import wave
import numpy as np
import matplotlib.pyplot as plt
import scipy
import librosa
from scipy import signal
from scipy.io import wavfile
f = wave.open('/mnt/c/Users/agrov/OneDrive/Desktop/IIITH/agrover112.cbq/Part-1/p1.wav','r')
y,sr=librosa.load('/mnt/c/Users/agrov/OneDrive/Desktop/IIITH/agrover112.cbq/Part-1/p1.wav')

print(librosa.get_samplerate('/mnt/c/Users/agrov/OneDrive/Desktop/IIITH/agrover112.cbq/Part-1/p1.wav'))
frame_rate=f.getframerate()
sampling_rate=44100
print(f.getparams()) # nch=1, SampleWidth=1, FrameRate=44100 ,nFrames=65162,not compressed


sig_enc=f.readframes(-1) #Read all the frames in bytes (hex) format
sig=np.frombuffer(sig_enc,np.int16) #convert bytes to int16
time=np.arange(0,len(sig))/frame_rate   # Time = No of frames/ Frame Rate     

plt.title("Time Domain plot")
plt.xlabel("Time")
plt.ylabel("Amplitude")
#plt.plot(time,sig)
#plt.savefig('time_domainplot.png')

#seg=sig[60840:62181] # 1.38s - 1.41s
#seg=sig[61000:62181]
start=61500
stop=62500 # start= 1.39 *Frame Rate
seg=sig[start:stop]
seg_len= len(seg)
time_seg=np.arange(0,len(seg))/frame_rate 
def plot_segment(segment,segment_length,segment_time):
    plt.title("Segment in time domain")
    plt.plot(np.linspace(0,seg_len/frame_rate,seg_len),seg)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    #plt.show()
    plt.savefig('segment_plot.png')

    plt.title("Segment Spectrogram")
    plt.specgram(seg,Fs=sampling_rate)
    plt.xlabel("Time")
    plt.ylabel("Frequency(Hz)")
    #plt.show()
    plt.savefig('segement_spectrogram.png')
def zero_crossing(seg):
    print("Number of zero crossings :",len(librosa.zero_crossings(seg))) # Extremely Large number of zero crossings 
def energy(seg,time_seg):
    energy=np.square(seg)
    print(np.max(energy))
    plt.title("Segment Energy Plot")
    plt.xlabel("Time(s)")
    plt.ylabel("Energy (J)")
    plt.plot(time_seg,energy)
    #plt.show()
    plt.savefig('segement_energy.png')

def auto_correlate(sig ,start ,stop):
    #autocorr = scipy.signal.correlate(sig[start:stop],sig[start:stop],mode = 'same',method = 'auto')
    acorr=librosa.autocorrelate(sig[start:stop])
    plt.xlabel('Lags')
    plt.ylabel('Autocorrelation ')
    plt.title("Segment Autocorrelation Plot")
    plt.plot(acorr)    # Highly unccorelated
    #plt.show()
    plt.savefig('segement_autocorelation.png')

#plot_segment(seg,seg_len,time_seg)
#zero_crossing(seg)
energy(seg,time_seg)
#auto_correlate(sig,start,stop)