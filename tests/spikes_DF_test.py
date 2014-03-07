'''
Created on Feb 24, 2014

@author: Jason C Rodriguez
'''
import spikes_with_df
import unittest


class TestSpikesFunctions(unittest.TestCase):


    def setUp(self):
        self.t_array = range(16) 
        self.v_array = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 
                            1, 2, 3, 4, 5]
        self.threshold = int(3)

    def tearDown(self):
        pass

    def testthresholdArray(self):
        obj = spikes_with_df.SpikeDataFrame(self.t_array, self.v_array)
        threshold_series = obj.thresholdArray(self.threshold)
        self.failUnless(list(threshold_series) == [0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1])
       
    def testspikeArrayTest(self):
        obj = spikes_with_df.SpikeDataFrame(self.t_array, self.v_array)
        threshold_series = obj.thresholdArray(self.threshold)
        boolean_spike_array = obj.spikeArray()
        self.failUnless(list(boolean_spike_array) == [True, False, False, False, True, 
            False, False, True, False, False, False, False, False, False, True, 
            False, True])
    
    def testthreshCrossingsIndicesArrayTest(self):
        obj = spikes_with_df.SpikeDataFrame(self.t_array, self.v_array)
        threshold_series = obj.thresholdArray(self.threshold)
        index_array = obj.threshCrossingsIndicesArray()
        self.failUnless(list(index_array) == [4, 14])
   
  
def main():
    unitteast.main()
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    main()