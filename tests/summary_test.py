'''
Created on Mar 10, 2014

@author: Jason C Rodriguez
'''
import unittest
import summary as sm
import numpy as np


class TestSummaryFunctions(unittest.TestCase):


    def setUp(self):
        self.burst_dataframe = { "a" : np.random.random_integers(1,10,5),
                                 "b" : np.random.random_integers(1,10,5),
                                 "c" : np.random.random_integers(1,10,5)
                                }
        self.summary_dataframe = sm.Summary(self.burst_dataframe)

    def tearDown(self):
        pass


    def testGet_Stats(self):
        print self.summary_dataframe.get_stats()
        pass
    
    def test_plot(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()