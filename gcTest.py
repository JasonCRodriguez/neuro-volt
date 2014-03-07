import pandas as pd
import numpy as np
import spikes as sp
import matplotlib.pyplot as plt

x = np.arange(0, 20, .001)
y = np.sin(x)


sample = sp.SpikeTimeSeries(y)

sample.thresholdArray(-.4)

#thresh = sample.spikeArray()


thresh = np.delete(thresh, [1])

print sample.starting_point_relative_to_threshold

plt.plot(x,y)
print x.size
print thresh.size

for i in x[thresh]:
    plt.vlines(i, np.min(y), np.max(y))

plt.hlines(-.4, 0, 20)

plt.show()


