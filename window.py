import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def sqrtCosEnv(length,rft=(0.005),fs=(44100)):
    """
    rft    : Rise and fall time [s]
    length : Total length of window [s]
    fs    : Sampling freq [Hz]
    """
    rfsamp = int(np.round(rft * fs))
    windowsamp = int(np.round(length * fs))
    flatsamp = windowsamp - (2 * rfsamp)
    time_index = np.arange(0, 1, 1 / rfsamp)

    r_env = np.sqrt((1 + np.cos(np.pi + np.pi * time_index)) / 2)
    f_env = np.sqrt((1 + np.cos(np.pi * time_index)) / 2)
    flat_env = np.ones(flatsamp)
    env = np.concatenate((r_env, flat_env, f_env), 0)

    return env

def CosEnv(length,rft=(0.005),fs=(44100)):
    """
    rft    : Rise and fall time [s]
    length : Total length of window [s]
    fs    : Sampling freq [Hz]
    """
    rfsamp = int(np.round(rft * fs))
    windowsamp = int(np.round(length * fs))
    flatsamp = windowsamp - (2 * rfsamp)
    time_index = np.arange(0, 1, 1 / rfsamp)

    r_env = (1 + np.cos(np.pi + np.pi * time_index)) / 2
    f_env = (1 + np.cos(np.pi * time_index)) / 2
    flat_env = np.ones(flatsamp)
    env = np.concatenate((r_env, flat_env, f_env), 0)

    return env

def ButterworthBP(x,lowcut,highcut,fs,order=(None),plot=('False')):
    """
    x       : Input signal
    lowcut  : Lowcut frequency [Hz]
    highcut : Highcut frequency [Hz]
    fs      : Sampling frequency [Hz]
    order   : Order of the butterworth bandpath filter
    """
    if order == None:
        wslow = lowcut * 0.5
        wshigh = highcut * 2
        order, wn = signal.buttord(wp=[lowcut,highcut], ws=[wslow,wshigh], gpass=3, gstop=80, fs=fs)
        print('order: %d' % order)
    else:
        wn = [lowcut, highcut]

    sos = signal.butter(order, wn, btype='bandpass', output='sos', fs=fs)
    y = signal.sosfilt(sos, x)

    if plot == 'True':
        w, h = signal.sosfreqz(sos, worN=2000)
        plt.plot((fs * 0.5 / np.pi) * w, abs(h), label="order = %d" % order)
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Gain')
        plt.grid(True)
        plt.legend(loc='best')
        plt.show()

    return y

def ButterworthLP(x,cutoff,fs,order=(None),plot=('False')):
    """
    x       : Input signal
    cutoff  : Cutoff frequency [Hz]
    fs      : Sampling frequency [Hz]
    order   : Order of the butterworth bandpath filter
    """
    if order == None:
        ws = cutoff * 2
        order, wn = signal.buttord(wp=cutoff, ws=ws, gpass=3, gstop=80, fs=fs)
        print('order: %d' % order)
    else:
        wn = cutoff

    sos = signal.butter(order, wn, btype='lowpass', output='sos', fs=fs)
    y = signal.sosfilt(sos, x)

    if plot == 'True':
        w, h = signal.sosfreqz(sos, worN=2000)
        plt.plot((fs * 0.5 / np.pi) * w, abs(h), label="order = %d" % order)
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Gain')
        plt.grid(True)
        plt.legend(loc='best')
        plt.show()

    return y

def ButterworthHP(x,cutoff,fs,order=(None),plot=('False')):
    """
    x       : Input signal
    cutoff  : Cutoff frequency [Hz]
    fs      : Sampling frequency [Hz]
    order   : Order of the butterworth bandpath filter
    """
    if order == None:
        ws = cutoff * 0.5
        order, wn = signal.buttord(wp=cutoff, ws=ws, gpass=3, gstop=80, fs=fs)
        print('order: %d' % order)
    else:
        wn = cutoff

    sos = signal.butter(order, wn, btype='highpass', output='sos', fs=fs)
    y = signal.sosfilt(sos, x)

    if plot == 'True':
        w, h = signal.sosfreqz(sos, worN=2000)
        plt.plot((fs * 0.5 / np.pi) * w, abs(h), label="order = %d" % order)
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Gain')
        plt.grid(True)
        plt.legend(loc='best')
        plt.show()

    return y

def GaussWin(length,fs,sigma=(None)):
    """
    length : Window length [s]
    fs     : Sampling frequency [Hz]
    sigma  : sigma
    F(n,σ) = (1 / σ * (2π)^(-1/2)) * e^((-1/2) * (n/σ)^2)
    """
    samp_length = length * fs
    half_samp_length = samp_length / 2

    if sigma == None:
        sigma = samp_length / 8

    index = np.arange(-half_samp_length,half_samp_length,1)
    y = np.reciprocal(np.sqrt(2 * np.pi) * sigma) * np.exp(-0.5 * np.square(index / sigma))

    return y
