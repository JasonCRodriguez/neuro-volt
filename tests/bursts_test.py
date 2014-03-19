'''
Created on Feb 24, 2014

@author: Jason C Rodriguez, Gabriel F Colton
'''
import bursts as brst
import unittest


class TestBurstsFunctions(unittest.TestCase):


    def setUp(self):
        self.t_array = range(16) 
        self.v_array = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 
                            1, 2, 3, 4, 5]
        self.threshold = int(3)

    def tearDown(self):
        pass

    def testthresholdArray(self):
        obj = brst.SpikeDataFrame(self.t_array, self.v_array)
        threshold_series = obj.thresholdArray(self.threshold)
        self.failUnless(list(threshold_series) == [0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1])
  
def main():
    unittest.main()
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    main()