import numpy as np

def sqrtCosEnv(length,rft=(0.005),frs=(44100)):
    """
    rft    ：rise and fall time [s]
    length : total length of window [s]
    frs    : sampling freq [Hz]
    """
    rfsamp = int(np.round(rft * frs))
    windowsamp = int(np.round(length * frs))
    flatsamp = windowsamp - (2 * rfsamp)
    time_index = np.arange(0, 1, 1 / rfsamp)

    r_env = np.sqrt((1 + np.cos(np.pi + np.pi * time_index)) / 2)
    f_env = np.sqrt((1 + np.cos(np.pi * time_index)) / 2)
    flat_env = np.ones(flatsamp)
    env = np.concatenate((r_env, flat_env, f_env), 0)

    return env

def CosEnv(length,rft=(0.005),frs=(44100)):
    """
    rft    ：rise and fall time [s]
    length : total length of window [s]
    frs    : sampling freq [Hz]
    """
    rfsamp = int(np.round(rft * frs))
    windowsamp = int(np.round(length * frs))
    flatsamp = windowsamp - (2 * rfsamp)
    time_index = np.arange(0, 1, 1 / rfsamp)

    r_env = (1 + np.cos(np.pi + np.pi * time_index)) / 2
    f_env = (1 + np.cos(np.pi * time_index)) / 2
    flat_env = np.ones(flatsamp)
    env = np.concatenate((r_env, flat_env, f_env), 0)

    return env
