'''
Created on Mar 21, 2014

@author: Jason C Rodriguez, Gabriel F Colton
'''

import bursts as br
import spikes as sp
import summary_statistics as ss

class NeuroVolt(object):
    
    def __init__(self, t_array, v_array, min_spike=4, max_ISI=100, threshold=-35):
        
        self.min_spike = min_spike
        self.max_ISI = max_ISI
        self.threshold = threshold
        self.t_array = t_array
        self.v_array = v_array
        spike_df = sp.SpikeDataFrame(self.t_array, self.v_array)
        spike_df.thresholdArray(self.threshold)
        spike_df.spikeArray()
        self.input_for_bursts = spike_df.threshCrossingsIndicesArray()
        
        self.burst_df = br.BurstDataFrame(self.input_for_bursts)
        self.input_for_stats_sum = self.burst_df.makeBursts(self.min_spike, self.max_ISI)
        
        self.stat_sum_obj = ss.SummaryStats(self.input_for_stats_sum)
  
