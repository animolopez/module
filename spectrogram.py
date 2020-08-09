import matplotlib.pyplot as plt
import numpy as np
import scipy.fft

def showSpectrogram(x, length, N=(512), frs=(44100), frange=(8000), Window=('hamming')):

    if x.ndim != 1:
        error = "dim of signal must be 1."
        return print(error)

    if Window == 'hamming':
        Win = np.hamming(N)
    elif Window == 'hanning':
        Win = np.hanning(N)

    plt.specgram(x, NFFT=N, Fs=frs, window=Win)
    plt.axis([0, length, 0, frange])
    plt.xlabel("time [s]")
    plt.ylabel("frequency [Hz]")
    plt.show()

def showFFT(x, N=(None), start=(0), frs=(44100), frange=(8000), amprange=(None)):

    if x.ndim != 1:
        error = "dim of signal must be 1."
        return print(error)

    if N == None:
        N = 2
        while len(x) > N:
            N *= 2
        info = "N = %s" % N
        print(info)

    X = scipy.fft.fft(x, n=N)
    freqList = scipy.fft.fftfreq(N, d = 1.0/ frs)
    amplitudeSpectrum = [np.sqrt(c.real ** 2 + c.imag ** 2) for c in X]
    phaseSpectrum = [np.arctan2(int(c.imag), int(c.real)) for c in X]

    # 振幅スペクトルを描画
    if amprange == None:
        amprange = np.max(amplitudeSpectrum)
    plt.subplot(211)
    plt.plot(freqList, amplitudeSpectrum, linestyle='-')
    plt.axis([0, frange, 0, amprange])
    plt.xlabel("frequency [Hz]")
    plt.ylabel("amplitude spectrum")

    # 位相スペクトルを描画
    plt.subplot(212)
    plt.plot(freqList, phaseSpectrum, linestyle='-')
    plt.axis([0, frange, -np.pi, np.pi])
    plt.xlabel("frequency [Hz]")
    plt.ylabel("phase spectrum")
    plt.show()

def showSTFT(x, N=(512), start=(0), frs=(44100), frange=(8000), amprange=(None), window=('hamming')):

    if x.ndim != 1:
        error = "dim of signal must be 1."
        return print(error)

    if N == None:
        N = 2
        while len(x) > N:
            N *= 2
        info = "N = %s" % N
        print(info)

    if window == 'hamming':
        Win = np.hamming(N)
    elif window == 'hanning':
        Win = np.hanning(N)

    x = Win * x[start:start+N]
    X = scipy.fft.fft(x, n=N)
    freqList = scipy.fft.fftfreq(N, d = 1.0/ frs)
    amplitudeSpectrum = [np.sqrt(c.real ** 2 + c.imag ** 2) for c in X]
    phaseSpectrum = [np.arctan2(int(c.imag), int(c.real)) for c in X]

    # 振幅スペクトルを描画
    if amprange == None:
        amprange = np.max(amplitudeSpectrum)
    plt.subplot(211)
    plt.plot(freqList, amplitudeSpectrum, linestyle='-')
    plt.axis([0, frange, 0, amprange])
    plt.xlabel("frequency [Hz]")
    plt.ylabel("amplitude spectrum")

    # 位相スペクトルを描画
    plt.subplot(212)
    plt.plot(freqList, phaseSpectrum, linestyle='-')
    plt.axis([0, frange, -np.pi, np.pi])
    plt.xlabel("frequency [Hz]")
    plt.ylabel("phase spectrum")
    plt.show()
