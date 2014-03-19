'''
Created on Mar 10, 2014

@author: Jason C Rodriguez
'''
import unittest
import summary as sm


class TestSummaryFunctions(unittest.TestCase):


    def setUp(self):
        burst_summary = sm.summary(burst_data_object)


    def tearDown(self):
        pass


    def testGet_Stats(self):
        burst_summary.get_stats()
        pass
    
    def test_plot(self):
        burst_summary.plot()
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()