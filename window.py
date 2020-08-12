import numpy as np
from scipy import signal

def sqrtCosEnv(length,rft=(0.005),fs=(44100)):
    """
    rft    : rise and fall time [s]
    length : total length of window [s]
    fs    : sampling freq [Hz]
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
    rft    : rise and fall time [s]
    length : total length of window [s]
    fs    : sampling freq [Hz]
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

def ButterworthBP(x,lowcut,highcut,fs,order=(None)):
    """
    x       : input signal
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

    return y

def ButterworthLP(x,cutoff,fs,order=(None)):
    """
    x       : input signal
    cutoff  : cutoff frequency [Hz]
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

    return y

def ButterworthHP(x,cutoff,fs,order=(None)):
    """
    x       : input signal
    cutoff  : cutoff frequency [Hz]
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

    return y
