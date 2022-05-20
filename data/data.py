import numpy as np

# Use the open function to open the texts files from the path
input_txt = open(r"/Users/goncalogomes/Documents/NOVA_IMS/2º_Semester/Computational_Inteligence/txt_files/inputs.txt")
target_txt = open(r"/Users/goncalogomes/Documents/NOVA_IMS/2º_Semester/Computational_Inteligence/txt_files/target.txt")

# Using numpy loadtxt to load the text files into a matrix format
inputs = np.loadtxt(input_txt, dtype = float)
target = np.loadtxt(target_txt, dtype = float)


print(inputs.shape), print(target.shape)
