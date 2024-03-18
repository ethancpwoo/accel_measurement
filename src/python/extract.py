import numpy as np
from scipy.signal import find_peaks

def main():

    directory = 'test2/'
    t_stamps = []
    y_accels = []
    timestamps = []

    with open(directory + 'timestamps.txt', 'r') as f: 
        for line in f:
            t_stamps.append(float(line))
    
    with open(directory + '/accelerations.txt', 'r') as f:
        for line in f:
            y_accels.append(float(line))

    # print(t_stamps)
    # print(y_accels)

    index, peaks = find_peaks(y_accels, prominence=5)
    for i in index: 
        #print(t_stamps[i])
        timestamps.append(t_stamps[i])
    
    start = timestamps[1:]
    stop = timestamps[:-1]
    start = np.array(start)
    stop = np.array(stop)

    timestamps = start - stop
    mask = np.logical_or(timestamps > 0.1, timestamps < 0.7)
    timestamps = timestamps[mask]

    period = np.sum(timestamps)/timestamps.size
    print(timestamps)
    print(period)


if __name__ == '__main__':
    main()