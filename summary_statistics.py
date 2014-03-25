'''
Created on Mar 17, 2014

@author: Jason C Rodriguez, Gabriel F Colton
'''

import pandas as pd

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
        
        #returns a pandas series
        self.IBI = self.period - self.burst_duration
        
        #returns a pandas data frame
        self.ISI = self.bursts_df.diff()

        #returns a pandas series
        self.spikes_per_burst = self.bursts_df.count()
      
        
        print self.bursts_df
        print self.IBI
        
        
        
        
        
        