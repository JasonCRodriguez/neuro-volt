'''
Created on Feb 24, 2014

@author: Jason C Rodriguez
'''
import spikes
import unittest


class TestSpikesFunctions(unittest.TestCase):


    def setUp(self):
        self.series = range(10)
        self.threshold = int(5)

    def tearDown(self):
        pass

    def testSpikes(self):
        obj = spikes.SpikeTimeSeries(self.series)
        threshold_series = obj.thresholdArray(self.threshold)
        self.failUnless(list(threshold_series) == [0,0,0,0,0,0,1,1,1,1])

      
def main():
    unittest.main()
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    main()