import pandas as pd
import numpy as np
import spikes as sp
import matplotlib.pyplot as plt

x = np.arange(0, 20, .001)
y = np.sin(x)


sample = sp.SpikeTimeSeries(y)

sample.thresholdArray(-.4)

sample.threshCrossingsIndicesArray()
