'''
Created on Feb 24, 2014

@author: Jason C Rodriguez, Gabriel F Colton
'''
import bursts as br
import unittest
import spikes as sp
import pandas as pd
import numpy as np


class TestBurstsFunctions(unittest.TestCase):


    def setUp(self):
        data = pd.read_csv('/Users/gabecolton/git_projects/LG_data.csv', delimiter = ',', index_col = 0)
        self.t_array = data.loc[:, '#t']
        self.v_array = data.loc[:, '#LGs_Vm']
        

    def tearDown(self):
        pass
 
        
    def testBurstNumber(self):
        spikes_series = sp.SpikeDataFrame(self.t_array, self.v_array)
        spikes_series.thresholdArray(-30)
        spikes_series.spikeArray()
        spike_times = spikes_series.threshCrossingsIndicesArray()
        test_obj = br.BurstDataFrame(spike_times)
        burst_df = test_obj.makeBursts(4,1500)
        
        burst_number = len(burst_df.columns)
                
        self.failUnless(burst_number == 10)
  
def main():
    unittest.main()
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    main()