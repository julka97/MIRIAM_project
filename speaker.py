import pyaudio
import wave
import trybun
from pathlib import Path


def load_answers():
    file_name = Path("tts_output1.wav")
    # jeżeli nie mamy jednej wypowiedzi to nie mamy wszystkich, bo pierwszy raz otwieramy program
    if (file_name.is_file() == False):
        trybun.run('tts_output1.wav',
                   "Witaj w filmotece Na dole widzisz listę dostępnych filmów Chcesz coś oglądnąć czy uzyskać informacje o filmie? ")
        trybun.run('tts_output2.wav', "Jaki film chcesz oglądnąć?")
        trybun.run('tts_output3.wav', "Podaj tytuł filmu")
        trybun.run('tts_output4.wav', "Przepraszam, nie zrozumiałam. Chcesz coś oglądnąć czy uzyskać informacje o filmie?")
        trybun.run('tts_output5.wav', "Chcesz coś oglądnąć czy uzyskać informacje o filmie? ")


def say_hello():
    CHUNK = 10240

    wf = wave.open("tts_output1.wav", 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    while data != b'':
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()
def ask_button():
    CHUNK = 10240

    wf = wave.open("tts_output5.wav", 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    while data != b'':
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()


def ask_watch():
    CHUNK = 10240

    wf = wave.open("tts_output2.wav", 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    while data != b'':
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()


def ask_description():
    CHUNK = 10240

    wf = wave.open("tts_output3.wav", 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    while data != b'':
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()


def misunderstand():
    CHUNK = 10240

    wf = wave.open("tts_output4.wav", 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    while data != b'':
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()
