import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

def get_frequency(note,octave):
    expo = (octave- 4 ) * 12 + (note-10)
    return 440*((2**(1/12)) ** expo)

def play(frequency,time,framerate=44100):
    t = np.linspace(0,time/1000,int(framerate*time/1000))
    wave = np.sin(2*np.pi * frequency * t)
    print(framerate,len(t),len(wave))
    #plt.plot(wave[:1000])
    #plt.show()

    sd.play(wave,framerate)
    sd.wait()


if __name__ == "__main__":
    freq = get_frequency(10,4)
    beep(freq,500)
