import numpy as np
import pyaudio
import wave


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


record()
