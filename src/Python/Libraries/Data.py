import numpy as np

class Data:
    
    def __init__(self):
        self.data_array = np.array([])
    
    def add_data(self, new_data):
        if(self.get_num_samples() == 0): 
            self.data_array = new_data
        else:
            self.data_array = np.vstack((self.data_array, new_data))
    
    def clear_data(self):
        self.data_array = np.array([])
        
    def get_num_samples(self):
        return self.data_array.shape[0]
        
    def calc_sampling_rate(self):
        mean_diff = np.mean(np.diff(self.data_array[:,0],1,0))
        self.sampling_rate = 1000000/mean_diff
        #print(self.sampling_rate)
        return self.sampling_rate
        
