'''
Created on Mar 21, 2014

@author: Jason C Rodriguez, Gabriel F Colton
'''

import bursts as br
import spikes as sp
import pandas as pd
import numpy as np
import summary_statistics as ss

class NeuroVolt(object)

    def __init__(self, t_array, v_array, threshold = -35, min_spike, max_ISI):
        
        spike_df = sp.SpikeDataFrame(t_array, v_array)
        spike_df.thresholdArray(threshold)
        spike_df.spikeArray()
        input_for_burst = spike_df.threshCrossingsIndicesArray()
        
        burst_df = br.BurstDataFrame(input_for_bursts)
        input_for_stats_sum = burst_df.makeBursts(min_spike, max_ISI)
        
        self.stat_sum_obj = ss.SummaryStats(input_for_stats_sum)
    
     