import numpy as np

def LpInst(x, dBref=(2e-5)):
    # 瞬時信号(x)の音圧レベル[dB]を求める, dBref は基準音圧（初期値は20[μPa]）
    y = 20 * np.log10(x / dBref)
    return y

def PaInst(x, dBref=(2e-5)):
    # 音圧レベル(x)から瞬時音圧(Pa)を求める
    y = dBref * np.power(10, x / 20)
    return y

def dBInst(x1, x2):
    # 瞬時信号間の相対dB値を求める, x1 が x2 より何dB大きいか
    y = 20 * np.log10(x1 / x2)
    return y

def amplify(x, data):
    # 信号(data)を x[dB] 増幅する
    A = np.power(10, x / 20)  # A = 10^(x/20)
    y =  A * data
    return y

def Leq(x, dBref=(2e-5)):
    # 離散時間信号(x, n)の等価騒音レベル[dB]を求める, モノラル用
    n = x.shape[0]  # 信号xのサンプル数
    P = np.square(x) / np.square(dBref)  # (P^2)/(Pref^2)
    y = 10 * np.log10((1 / n) * np.sum(P))
    # y = 10 * log10((1/n)*Σ((P^2)/(Pref^2)))
    return y

def LeqLT(x, fs=(44100), t=(0.050), dBref=(2e-5)):
    # 離散時間信号(x, n)の長期平均等価騒音レベル[dB]を求める, モノラル用
    n = x.shape[0]  # 信号xのサンプル数
    tsamp =  int(fs * t)
    N = int(np.ceil(n / tsamp))
    zero_array = np.zeros(int((N * tsamp) - n))
    X = np.concatenate([x, zero_array])
    P = np.square(X) / np.square(dBref)  # (P^2)/(Pref^2)
    P = P.reshape(N, tsamp)

    loop = np.arange(0,N,1)
    Lsum = 0
    for l in loop:
        Li = 10 * np.log10((1 / tsamp) * np.sum(P[l]))
        Lsum = Lsum + np.power(10, Li / 10)

    y = 10 * np.log10((1 / N) * Lsum)
    return y
