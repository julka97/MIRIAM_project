#componentów 4-8
#ramkowanie 10/25 ms
#mfcc 13
#delty! python_speech_features.base.delta()
import scipy.io.wavfile as wav
import fnmatch
import os
import pickle
import numpy
from python_speech_features import mfcc
from python_speech_features import base
from sklearn.mixture import GaussianMixture as GMM

recordings=7
ramkowanie=0.025
components=4
delta_memory=2
path = os.getcwd()
allMFCC = numpy.empty([1, recordings], dtype=object)
i=0
for file in os.listdir(os.path.join(path, 'miriam')):
    fs, samples = wav.read(os.path.join(path, 'miriam', file))
    MFCC = mfcc(samples, fs,winlen=ramkowanie, nfft=round(ramkowanie * fs) + 1, numcep=13)
    delta=base.delta(MFCC, delta_memory)
    delta_delta=base.delta(delta, delta_memory)
    MFCC_and_deltas=numpy.c_[MFCC,delta,delta_delta]
    allMFCC[0, i] = MFCC_and_deltas
    i = i + 1
# w nazwie pliku jest liczba parametrow mfcc z ktorej zostala funkcja wywołana
#with open('mfcc_miriam.bin', 'wb') as f:
#    pickle.dump(allMFCC, f)
#    f.close()

model= GMM(components, covariance_type="diag")
tmp_data = numpy.zeros((0, 39))
for j in range(0, recordings):
    tmp_data = numpy.r_[tmp_data, allMFCC[0, j]]
model.fit(tmp_data)
with open('model.bin', 'wb') as f:
    pickle.dump(model, f)
    f.close()
def if_Miriam(ramkowanie, delta_memory):
    treshold = -50
    path="miriam/1.wav"
    with open('model.bin', 'rb') as f:
        model=pickle.load(f)
        f.close()
    fs, data = wav.read(path)
    MFCC = mfcc(samples, fs,winlen=ramkowanie, nfft=round(ramkowanie * fs) + 1, numcep=13)
    delta=base.delta(MFCC, delta_memory)
    delta_delta=base.delta(delta, delta_memory)
    MFCC_and_deltas = numpy.c_[MFCC, delta, delta_delta]
    score=model.score(MFCC_and_deltas)
    print(score)
    if score>treshold:
        return True
    else:
        return False
print(if_Miriam(ramkowanie,delta_memory))