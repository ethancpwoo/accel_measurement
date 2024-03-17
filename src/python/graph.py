import matplotlib.pyplot as plt
import numpy as np

from matplotlib import style
from record import record

def main():

    t_stamps, y_accels = record()

    t_stamps = np.array(t_stamps)
    y_accels = np.array(y_accels)

    with open('test1/timestamps_trialtest.txt', 'w') as f: 
        for i in t_stamps:
            f.write(i)
    
    with open('test1/accelerations_trialtest.txt', 'w') as f: 
        for i in y_accels:
            f.write(i)

    print(t_stamps)
    print(y_accels)

    ax = plt.subplot()
    ax.plot(t_stamps, y_accels, label='accel')
    ax.set_ylim([50, 0])
    ax.set_yticks(np.arange(0, 50, 2))

    ax.invert_yaxis()

    ax.set_xlabel('time (s)')
    ax.set_ylabel('acceleration (m/s^2)')
    
    
    plt.savefig('test1/trial1.png')

if __name__ == '__main__':
    main()