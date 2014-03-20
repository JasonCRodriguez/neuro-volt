'''
Created on Feb 24, 2014

@author: Jason C Rodriguez, Gabriel F Colton
'''

import pandas as pd
import numpy as np

class BurstDataFrame(object):

    def __init__(self, spike_times_series):
        self.raster = spike_times_series
    
    def makeBursts(self, min_spike_number, max_ISI):
        raster_array  = np.array(self.raster)
        dif_array = np.diff(raster_array)
        
        #Trues for all indices of last spike in each burst
        bool_burst_ends = dif_array > max_ISI
        
        #times of each spike that is the last spike in a burst
        last_SPB_times = raster_array[bool_burst_ends]
        
        #adds the time of the last spike to the array (not included because of use of diff)
        last_SPB_times = np.append(last_SPB_times, raster_array[-1])
               
        
        burst_number_count = 0

        output_df = pd.DataFrame()
        
        key_count = 0
        
        #iterates through spike times and time of each last spike
        #adds spike times to an array and deletes that spike time
        #does this until it reaches the current burst's
        #last spike then joins that array to output_df 

        for last_sp in last_SPB_times:
            burst_array = np.array([])
            
            for spike_time in raster_array:
                
                if spike_time <= last_sp:
                    # print spike_time< last_sp
                    burst_array = np.append(burst_array, spike_time)
                    raster_array = np.delete(raster_array, 0)
                    
            key_name = 'Burst_%s' % key_count      
            df_temp = pd.DataFrame({key_name : burst_array})
            output_df = output_df.join(df_temp, how = 'outer')
            burst_number_count+=1
            key_count+=1
       
        return output_df
        


