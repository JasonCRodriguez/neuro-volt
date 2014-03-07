'''
Created on Feb 24, 2014

@author: Jason C Rodriguez
'''
import pandas as pd
import numpy as np

class SpikeDataFrame(object):
    
    
    
    def __init__(self, time_array, voltage_array):
        self.time_voltage_df = pd.DataFrame({'time': time_array, 'voltage': voltage_array})
        # DataFrame will normally consist of a file/CSV/spreadsheet 
        # two columns, t, V
        
    
    def thresholdArray(self, input_threshold):
        '''
        returns a binary series of points in self.time_series 
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
        thresh_cross_bool_array = int_array_shift != int_array
              
                
        #print thresh_cross_bool_array       
        #print int_array_shift
        #print int_array
        
        return thresh_cross_bool_array
      
    def threshCrossingsIndicesArray(self):
        
        
        starting_point_relative_to_threshold = self.time_voltage_df.loc[1, 'voltage'] > self.threshold
    	print starting_point_relative_to_threshold
    	#true - starts above threshold, false - starts below threshold 
    	bool = np.delete(self.spikeArray(),-1)
    	print bool
        all_thresh_cross = self.time_voltage_df.loc[bool, 'time']
        print all_thresh_cross
        len = all_thresh_cross.count()
        print len
    	if starting_point_relative_to_threshold == True:
    		return all_thresh_cross.iloc[2:len:2]
    	else:
    	    return all_thresh_cross.iloc[1:len:2]
    	
    	# spike_array_length = bool.size
#      	print spike_array_length
#      	
#     	even = np.array(range(1,spike_array_length, 2))
#     	odd = np.array(range(0,spike_array_length, 2))
#     	thresh_crossing_indices = np.where(start_point, even, odd) 
    	# if self.starting_point_relative_to_threshold == true: #starts above threshold
# 	        even = np.array(range(1,spike_array_length, 2)   
# 	    else:
# 	        odd = np.array(range(2,spike_array_length, 2)   

	            
	            
		