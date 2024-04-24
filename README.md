Requirements (python packages):

1. torch
2. plotly
3. numpy
4. pandas
5. time
6. json
7. glob
8. re
9. scipy
10. matplotlib
11. tqdm

12. 
Files and Contents:

1. data_preprocess.ipynb : Here the signals are preprocessed by slicing, serializing the signals, saved as numpy(.npy) file and verify the length of serialized signals in each npy file. Modules Included: (a) slice_signal (b) process and serialize (c) data verify

2. utils.ipynb: It is a Custom Dataset and dataloader. The SignalDataset class reads audio samples from serialized files, providing functionality for selecting reference batches for virtual batch normalization and retrieving individual data samples with their clean and noisy versions. Class: SignalDataset 1. init(self, data_type): Initializes the dataset object with the specified data type (train, val, or test) and sets the corresponding data path. 2. reference_batch(self, batch_size): Randomly selects a reference batch from the dataset, used for calculating statistics for virtual batch normalization, and returns it as a PyTorch tensor. 3. getitem(self, idx): Retrieves an individual data sample from the dataset at the specified index, returning the sample along with its clean, noisy, and acceleration components as PyTorch tensors. 4. len(self): Returns the total number of samples in the dataset.

3. model.ipynb: The VirtualBatchNorm1d, Generator, and Discriminator classes together constitute a Generative Adversarial Network (GAN) model for denoising signal, incorporating virtual batch normalization for improved training stability and performance. Classes: * VirtualBatchNorm1d: Implements virtual batch normalization for normalizing activations across virtual batches in a neural network. * Generator: Represents the generator part of the GAN responsible for transforming noisy signals into clean versions. * Discriminator: Represents the discriminator part of the GAN responsible for distinguishing between real and generated signals.

4. main.ipynb: Trains, validates and tests signal data. Plots the generated clean signals. Total epochs trained: 300 Batch size: 64

5. NoisePrep.py: Here, noisy PPG is synthesized using the acc signal.The NoisePrep class in NoisePrep.py preprocesses accelerometer data to calculate the summation of maximum differences within specified windows, aiding in noise addition for PPG signals.

6. Handle_File.ipynb:

INPUT: 'filepath' from where you want to extract csv file extract_csv_files : INPUT: One specific .csv file name in the form of 'bidmc_{p_id}Signals.csv' or List of .csv files name in 'bidmc{p_id}_Signals.csv' format or None Returns: Particular csv file as mentioned above or list of csv files or all the csv files present in the 'filepath'

dict_to_list : Converts filename of dict to list.

remove_leading_spaces: Removes leading spaces from the column header. For eg: ' PLETH' to 'PLETH'

csv_to_df : Converts a file to pandas dataframe

7. dtw.ipynb: Implementation of dynamic time warping method to measure similarities between two signals. The Dtw class in the provided code implements Dynamic Time Warping (DTW) for aligning sequences x and y, calculating the alignment cost as the normalized distance between the two sequences.
