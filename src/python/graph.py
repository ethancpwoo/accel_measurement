import matplotlib.pyplot as plt
import numpy as np

from matplotlib import style
from record import record

def main():

    directory = 'test2/'
    t_stamps, y_accels = record()

    t_stamps = np.array(t_stamps)
    y_accels = np.array(y_accels)

    with open(directory + 'timestamps.txt', 'w') as f: 
        for i in t_stamps:
            f.write(str(i))
            f.write('\n')
    
    with open(directory +'accelerations.txt', 'w') as f: 
        for i in y_accels:
            f.write(str(i))
            f.write('\n')

    print(t_stamps)
    print(y_accels)

    ax = plt.subplot()
    ax.plot(t_stamps, y_accels, label='accel')
    ax.set_ylim([50, 0])
    ax.set_yticks(np.arange(0, 50, 2))

    ax.invert_yaxis()

    ax.set_xlabel('time (s)')
    ax.set_ylabel('acceleration (m/s^2)')

    plt.savefig(directory + 'graph.png')

if __name__ == '__main__':
    main()