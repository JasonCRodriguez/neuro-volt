'''
Created on Feb 24, 2014

@author: Jason C Rodriguez, Gabriel F Colton
'''
import pandas as pd
import numpy as np

class SpikeDataFrame(object):
    
    
    
    def __init__(self, time_array, voltage_array):
        # DataFrame will normally consist of a file/CSV/spreadsheet 
        # two columns, t, V
        self.time_voltage_df = pd.DataFrame({'time': time_array, 'voltage': voltage_array})
        
        
    
    def thresholdArray(self, input_threshold):
        '''
        returns a binary series of points in the voltage array of the DataFrame 
        that are above input_threshold 
        '''
        self.threshold = input_threshold
        self.threshold_series = self.time_voltage_df.loc[:,'voltage'] > self.threshold
        return self.threshold_series.astype(int)
                    
    def spikeArray(self):
        '''
        converts a time series into a numpy boolean array with 
        True's for all threshold crossings
        '''
        
        # converts the time series produced by thresholdArray() into a numpy array
        int_array = np.array(self.thresholdArray(self.threshold).values)
        
        #makes a new array that is shifted one spot 
        #over with arbitrary place holder, 8
        int_array_shift = np.insert(int_array, [0], 8)
        
        #adds an arbitrary 8 to the end of the first array so it is the same
        # size as the comparison array
        int_array = np.append(int_array, 8)
        
        #creates a boolean array with true values for each threshold crossing
        #by comparing the shifted and non shifted arrays
        thresh_cross_bool_array = int_array_shift != int_array
        
        return thresh_cross_bool_array
      
    def threshCrossingsIndicesArray(self):
        '''
        returns a series of even or odd threshold crossings (spikes) 
        depending on the starting point
        '''
        #true - starts above threshold, false - starts below threshold         
        starting_point_relative_to_threshold = self.time_voltage_df.loc[1, 'voltage'] > self.threshold
    	
    	#deletes the last entry of the boolean array returned by spikeArray() 
        #so it is the same size as the time vector and can be used for masking
    	bool = np.delete(self.spikeArray(),-1)
    	
    	#uses the boolean vector to mask the input 
    	#time_array to get all threshold crossings
        all_thresh_cross = self.time_voltage_df.loc[bool, 'time']
       
        #returns the 3rd and every other or 2nd and every other crossings
        #depending on the starting point of the trace        
    	if starting_point_relative_to_threshold == True:
    		return all_thresh_cross.iloc[2:len:2]
    	else:
     	    return all_thresh_cross.iloc[1:len:2]
    	    
    	
    	
    	
		