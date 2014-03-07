import pandas as pd
import numpy as np
import spikes_with_df as sp
import matplotlib.pyplot as plt

t_array = range(16) 
v_array = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 
                            1, 2, 3, 4, 5]
threshold = int(3)






sample = sp.SpikeDataFrame(t_array, v_array)

print sample.thresholdArray(threshold)

print sample.spikeArray()

print sample.threshCrossingsIndicesArray()