import numpy  as np
import  pandas as pd


class NoisePrep:

    def __init__(self,acc_data,window=125):
        self.acc_data=acc_data
        self.window=window
        self.window_dict={}

    
    def calculate_sum(self,slice_data):
        data=slice_data.copy()
        reference_row = data.iloc[0, 1:]
        max_differences = np.abs(data.iloc[:, 1:] - reference_row).max(axis=1)
        current_summation = np.sum(max_differences)

        return current_summation
        

    def calc_sum(self, slice_range: tuple = None, th_window: int = None):

        if th_window is None and slice_range is None:
            raise ValueError("Either give index range or th-window.")

        current_summation = 0
        data = self.acc_data.copy()

        if th_window is not None: 
            start = th_window - 1
            end = start + self.window  
            slice_data = data.iloc[start:end, :].reset_index(drop=True) 
            # print(slice_data)

        elif slice_range is not None:  
            start, end = slice_range[0], slice_range[1] + 1 
            slice_data = data.iloc[start:end-1, :].reset_index(drop=True) 
            # print(slice_data)

        current_summation = self.calculate_sum(slice_data)

        return current_summation

class AddNoise(NoisePrep):
    def __init__(self, acc_data, clean_signal,window=125):
        super().__init__(acc_data, window)
        self.window=window
        self.avgs={}
        self.clean_signal=clean_signal
        self.acc_data1=acc_data
        

    def calc_avg(self):
        clean_sig=self.clean_signal.copy()
        accData1=self.acc_data1.copy()
        prev_avg=2
        curr_avg=0
        count_sum=0
        for win in range(0,len(accData1)):
            if win+self.window<=len(accData1):
                S=self.calc_sum(slice_range=(win,win+self.window))
                count_sum+=1
                curr_avg=(0.7*prev_avg)+0.3*(S/self.window)
                self.avgs[win+1]=curr_avg
                prev_avg=curr_avg


        return self.avgs
        
                      
    def add_noise(self,scaling_factor=0.9):
        self.calc_avg()
        avgs_dict=self.avgs.copy()
        print(avgs_dict)
        clean_sig=self.clean_signal.copy()
        avgs_list=list(avgs_dict.values())
        time=clean_sig['Time [s]']
        ppg_signal=clean_sig[' PLETH']
        avgs_list=avgs_list[:len(ppg_signal)]
        scaled_averaged_noise=np.array(avgs_list)*scaling_factor
        noisy_ppg_signal =  ppg_signal + scaled_averaged_noise
        return noisy_ppg_signal,avgs_list,scaled_averaged_noise
    
