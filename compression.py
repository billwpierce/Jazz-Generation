import wave
import struct
import sys

def floats_to_wav(txt_file):
    with open(txt_file, 'rb') as file:
        b = file.read().split(", ")
        # print(b[0])
        test = struct.pack("%ih" % int(len(b)* 1), *[int(element.strip("[").strip("]")) for element in b])
        w = wave.open(txt_file + " translated.wav", "w")
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(48000)
        w.setnframes(7374848)
        w.writeframesraw(test)

# read the wav file specified as first command line arg
floats_to_wav(sys.argv[1])