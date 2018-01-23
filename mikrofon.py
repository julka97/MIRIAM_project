import numpy as np
import pyaudio
import wave
import miriam_GMM
def record():
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 15
    WAVE_OUTPUT_FILENAME = "waves/answer.wav"
    THRESHOLD = 20

    audio = pyaudio.PyAudio()

    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print("recording...")
    frames = []

    def if_silent(data):
        y = np.fromstring(data, dtype=np.int16)
        return np.sqrt(np.mean(np.array(y) ** 2)) < THRESHOLD

    tmp = 0
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        if if_silent(data):
            tmp = tmp + 1
        else:
            tmp = 0
        if tmp == int(RATE / CHUNK * 2):
            break
        frames.append(data)

    print("finished recording")
    print(frames[0])
    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

def listen_for_miriam():
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    dt=0.025
    CHUNK =np.int(dt*RATE)
    OVER_LAPP=np.int((0.25*RATE)/CHUNK)

    audio = pyaudio.PyAudio()
    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print("recording...")

    buffer1=np.empty([0,1])
    tmp1 = 0
    buffer2=np.empty([0,1])
    tmp2 =-OVER_LAPP
    buffer3=np.empty([0,1])
    tmp3 = -2*OVER_LAPP
    find=False
    while find==False:
        data = np.fromstring(stream.read(CHUNK))
        tmp1 = tmp1 + 1
        tmp2 = tmp2 + 1
        tmp3 = tmp3 + 1
        if tmp1>0:
            buffer1=np.c_[buffer1,data]
        if tmp2 > 0:
            buffer2 = np.c_[buffer2, data]
        if tmp3>0:
            buffer3=np.c_[buffer3,data]
        if tmp1==1/dt:
            if miriam_GMM.if_Miriam(dt,2,buffer1):
                break
            buffer1=np.empty([0,1])
            tmp1=0
        if tmp2==1/dt:
            if miriam_GMM.if_Miriam(dt,2,buffer2):
                break
            buffer2=np.empty([0,1])
            tmp2=0
        if tmp3==1/dt:
            if miriam_GMM.if_Miriam(dt,2,buffer3):
                break
            buffer3=np.empty([0,1])
            tmp3=0

    print("Here is our Miriam!")

    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

#record()
