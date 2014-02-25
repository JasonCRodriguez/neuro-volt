'''
Created on Feb 24, 2014

@author: Jason C Rodriguez
'''
import pandas as pd
import numpy as np

class SpikeTimeSeries(object):
    
    def __init__(self, time_series):
        self.time_series = pd.Series(time_series)
    
    def threshold(self, threshold):
        self.threshold = threshold
        self.threshold_series = self.time_series > self.threshold
        return self.threshold_series.astype(int)