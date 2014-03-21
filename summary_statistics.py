'''
Created on Mar 17, 2014

@author: Jason C Rodriguez, Gabriel F Colton
'''

import pandas as pd
import numpy as np

class SummaryStats(object):

    def __init__(self, bursts_dataframe):
        self.bursts_df = pd.DataFrame(bursts_dataframe)
        
        #returns a scalar
        self.burst_number = len(self.bursts_df.columns)
        
        min_series = self.bursts_df.min()
        max_series = self.bursts_df.max()
        
        #returns a pandas series
        self.burst_duration = max_series - min_series
        
        #returns a pandas series
        self.period = min_series.diff()
        
        burst_ends = pd.DataFrame(np.append(min_series.values, max_series.values))
        
        #returns a numpy array
        self.IBI = burst_ends.diff(self.burst_number+1).dropna()
        
        #returns a pandas data frame
        self.ISI = self.bursts_df.diff()

        #returns a pandas series
        self.spikes_per_burst = self.bursts_df.count()
      
        
        
        
        
        
        
        
        