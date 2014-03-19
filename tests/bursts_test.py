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
<<<<<<< HEAD

    def testthresholdArray(self):
        obj = brst.SpikeDataFrame(self.t_array, self.v_array)
        threshold_series = obj.thresholdArray(self.threshold)
        self.failUnless(list(threshold_series) == [0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1])
=======
 
        
    def testBurstNumber(self):
        spikes_series = sp.SpikeDataFrame(self.t_array, self.v_array)
        spikes_series.thresholdArray(-30)
        spikes_series.spikeArray()
        spike_times = spikes_series.threshCrossingsIndicesArray()
        test_obj = br.BurstDataFrame(spike_times)
        burst_df = test_obj.makeBursts(4,1500)
        
        burst_number = len(burst_df.columns)
                
        self.failUnless(burst_number == 10)
>>>>>>> 5cba42e086bd71dbb1611cef62ac241e21a0985a
  
def main():
    unittest.main()
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    main()