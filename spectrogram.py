import matplotlib.pyplot as plt
import numpy as np
import scipy.fft

def showSpectrogram(x, length, N=(512), frs=(44100), frange=(8000), Window=('hamming')):
    if Window == 'hamming':
        Win = np.hamming(N)
    elif Window == 'hanning':
        Win = np.hanning(N)

    plt.specgram(x, NFFT=N, Fs=frs, window=Win)
    plt.axis([0, length, 0, frange])
    plt.xlabel("time [s]")
    plt.ylabel("frequency [Hz]")
    plt.show()

def showSpectrum(x, start=(0), N=(8192), frs=(44100), frange=(8000), Window=('hamming')):
    if Window == 'hamming':
        Win = np.hamming(N)
    elif Window == 'hanning':
        Win = np.hanning(N)

    x = Win * x[start:start+N]
    X = scipy.fft.rfft(x[start:start+N])
    freqList = scipy.fft.rfftfreq(N, d = 1.0/ frs)
    amplitudeSpectrum = [np.sqrt(c.real ** 2 + c.imag ** 2) for c in X]
    phaseSpectrum = [np.arctan2(int(c.imag), int(c.real)) for c in X]

    # 振幅スペクトルを描画
    plt.subplot(211)
    plt.plot(freqList, amplitudeSpectrum, marker= 'o', linestyle='-')
    plt.axis([0, frange, 0, 2])
    plt.xlabel("frequency [Hz]")
    plt.ylabel("amplitude spectrum")

    # 位相スペクトルを描画
    plt.subplot(212)
    plt.plot(freqList, phaseSpectrum, marker= 'o', linestyle='-')
    plt.axis([0, frange, -np.pi, np.pi])
    plt.xlabel("frequency [Hz]")
    plt.ylabel("phase spectrum")
    plt.show()
