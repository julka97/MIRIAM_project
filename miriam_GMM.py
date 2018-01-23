import scipy.io.wavfile as wav
import os
import pickle
import numpy
from python_speech_features import mfcc
from python_speech_features import base
from sklearn.mixture import GaussianMixture as GMM

def if_Miriam(ramkowanie, delta_memory,data):
    treshold = -50
    with open('model.bin', 'rb') as f:
        model=pickle.load(f)
        f.close()
    fs=44100
    MFCC = mfcc(data, fs,winlen=ramkowanie, nfft=round(ramkowanie * fs) + 1, numcep=10)
    delta=base.delta(MFCC, delta_memory)
    delta_delta=base.delta(delta, delta_memory)
    MFCC_and_deltas = numpy.c_[MFCC, delta, delta_delta]
    score=model.score(MFCC_and_deltas)
    print(score)
    if score>treshold:
        return True
    else:
        return False
recordings=37
ramkowanie=0.025
components=4
delta_memory=2
path = os.getcwd()
allMFCC = numpy.empty([1, recordings], dtype=object)
i=0
for file in os.listdir(os.path.join(path, 'miriam')):
    fs, samples = wav.read(os.path.join(path, 'miriam', file))
    MFCC = mfcc(samples, fs,winlen=ramkowanie, nfft=round(ramkowanie * fs) + 1, numcep=10)
    delta=base.delta(MFCC, delta_memory)
    delta_delta=base.delta(delta, delta_memory)
    MFCC_and_deltas=numpy.c_[MFCC,delta,delta_delta]
    allMFCC[0, i] = MFCC_and_deltas
    i = i + 1

model= GMM(components, covariance_type="diag")
tmp_data = numpy.zeros((0, 30))
for j in range(0, recordings):
    tmp_data = numpy.r_[tmp_data, allMFCC[0, j]]
model.fit(tmp_data)
with open('model.bin', 'wb') as f:
    pickle.dump(model, f)
    f.close()
print(if_Miriam(ramkowanie,delta_memory, path="waves/answer.wav"))
print(if_Miriam(ramkowanie,delta_memory, path="miriam/1.wav"))