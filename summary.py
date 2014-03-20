'''
Created on Mar 10, 2014

@author: Jason C Rodriguez, Gabe Colton
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Summary(object):
    def __init__(self, burst_dataframe):
        self.burst_dataframe = pd.DataFrame(burst_dataframe)
        
    def get_stats(self):
        return self.burst_dataframe.mean()



if __name__ == '__main__':
    pass