import wave
import struct
import sys

def wav_to_floats(wave_file): # From https://stackoverflow.com/questions/7769981/how-to-convert-wave-file-to-float-amplitude
    w = wave.open(wave_file)
    astr = w.readframes(w.getnframes())
    # convert binary chunks to short 
    a = struct.unpack("%ih" % (w.getnframes()* w.getnchannels()), astr)
    a = [int(val) for val in a]
    return a

# read the wav file specified as first command line arg
signal = wav_to_floats(sys.argv[1])
with open(sys.argv[1] + '—result.txt', 'w') as file:
    file.write(str(signal))