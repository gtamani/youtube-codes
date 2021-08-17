import numpy as np
import sounddevice as sd
import threading

def get_frequency(note,octave):
    expo = (octave- 4 ) * 12 + (note-9)
    return 440*((2**(1/12)) ** expo)

def play(frequency,time,framerate=44100):
    t = np.linspace(0,time/1000,int(framerate*time/1000))
    wave = np.sin(2*np.pi * frequency * t)

    sd.play(wave,framerate)
    sd.wait()

def play_chord(chord):
    threads = []
    for note in chord:
        th = threading.Thread(target=lambda:play(get_frequency(note,4),1000))
        th.start()
        threads.append(th)
    
    for th in threads:
        th.join()
    
def strip_chord(chord):
    if "#" in chord or "b" in chord:
        root = notes_dictionary["alter"][chord[:2]]
        rest = chord[2:]
    else:
        root = notes_dictionary["cromatic"][chord[0]]
        rest = chords[0:]
    return root, rest




if __name__ == "__main__":
    notes_dictionary = {"cromatic":{"C":0,"D":2,"E":4,"F":5,"G":7,"A":9,"B":11},
                        "alter":{"C#":1,"Db":1,"D#":3,"Eb":3,"F#":6,"Gb":6,"G#":8,
                                "Ab":8,"A#":10,"Bb":10}}

    print(strip_chord("C#m"))
    """
    c_major = [1,5,8]
    play_chord(c_major)
    freq = get_frequency(0,4) # Do
    play(freq,500)
    """

    