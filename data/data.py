import numpy as np

# Use the open function to open the texts files from the path
 main
input_txt = open(r"C:\Users\Tomás\Desktop\Caixa de Entrada\NOVA IMS\2º Semestre\Inteligência Computacional de Optimização\projects\Dataset\betas.txt")
target_txt = open(r"C:\Users\Tomás\Desktop\Caixa de Entrada\NOVA IMS\2º Semestre\Inteligência Computacional de Optimização\projects\Dataset\target.txt")

# Using numpy loadtxt to load the text files into a matrix format
inputs = np.loadtxt(input_txt, dtype = float)
target = np.loadtxt(target_txt,dtype = float)


#print(inputs.shape), print(target.shape)

print(np.max(target))



inputs_txt = open('/Users/goncalogomes/Documents/NOVA_IMS/2º_Semester/Computational_Inteligence/txt_files/inputs.txt', 'r')
target_txt = open('/Users/goncalogomes/Documents/NOVA_IMS/2º_Semester/Computational_Inteligence/txt_files/target.txt', 'r')

# Using numpy loadtxt to load the text files into a matrix format
inputs = np.loadtxt(inputs_txt, dtype = float)
target = np.loadtxt(target_txt,dtype = float)


print(inputs.shape), print(target.shape)

