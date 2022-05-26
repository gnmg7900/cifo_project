from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

text1 = open(r"/Users/goncalogomes/Documents/NOVA_IMS/2º_Semester/Computational_Inteligence/cifo_project/Results/Results1.txt")
text1 = np.loadtxt(text1, dtype= float)
df1 = pd.DataFrame(text1)
results1 = np.reshape(np.array(df1.mean()), 100)

text2 = open(r"/Users/goncalogomes/Documents/NOVA_IMS/2º_Semester/Computational_Inteligence/cifo_project/Results/Results2.txt")
text2 = np.loadtxt(text2, dtype= float)
df2 = pd.DataFrame(text2)
results2 = np.array(df2.mean())

text3 = open(r"/Users/goncalogomes/Documents/NOVA_IMS/2º_Semester/Computational_Inteligence/cifo_project/Results/Results3.txt")
text3 = np.loadtxt(text3, dtype= float)
df3 = pd.DataFrame(text3)
results3 = np.array(df3.mean())

text4 = open(r"/Users/goncalogomes/Documents/NOVA_IMS/2º_Semester/Computational_Inteligence/cifo_project/Results/Results4.txt")
text4 = np.loadtxt(text4, dtype= float)
df4 = pd.DataFrame(text4)
results4 = np.array(df4.mean())

text5 = open(r"/Users/goncalogomes/Documents/NOVA_IMS/2º_Semester/Computational_Inteligence/cifo_project/Results/Results5.txt")
text5 = np.loadtxt(text5, dtype= float)
df5 = pd.DataFrame(text5)
results5 = np.array(df5.mean())

text6 = open(r"/Users/goncalogomes/Documents/NOVA_IMS/2º_Semester/Computational_Inteligence/cifo_project/Results/Results6.txt")
text6 = np.loadtxt(text6, dtype= float)
df6 = pd.DataFrame(text6)
results6 = np.array(df6.mean())

text7 = open(r"/Users/goncalogomes/Documents/NOVA_IMS/2º_Semester/Computational_Inteligence/cifo_project/Results/Results7.txt")
text7 = np.loadtxt(text7, dtype= float)
df7 = pd.DataFrame(text7)
results7 = np.array(df7.mean())

text8 = open(r"/Users/goncalogomes/Documents/NOVA_IMS/2º_Semester/Computational_Inteligence/cifo_project/Results/Results8.txt")
text8 = np.loadtxt(text8, dtype= float)
df8 = pd.DataFrame(text8)
results8 = np.array(df8.mean())

text9 = open(r"/Users/goncalogomes/Documents/NOVA_IMS/2º_Semester/Computational_Inteligence/cifo_project/Results/Results9.txt")
text9 = np.loadtxt(text9, dtype= float)
df9 = pd.DataFrame(text9)
results9 = np.array(df9.mean())

text10 = open(r"/Users/goncalogomes/Documents/NOVA_IMS/2º_Semester/Computational_Inteligence/cifo_project/Results/Results10.txt")
text10 = np.loadtxt(text10, dtype= float)
df10 = pd.DataFrame(text10)
results10 = np.array(df10.mean())

# Ploting the results over 100 generations

x = np.array(range(100))

# FPS Plots

plt.plot(x, results1, label = "Single_Point/Swap")
plt.plot(x, results2, label = "Arithmetic/Swap")
plt.plot(x, results5, label = "Single_Point/Inversion")
plt.plot(x, results6, label = "Arithmetic/Inversion")
plt.xlabel("Generations")
plt.ylabel("Fitness")
plt.legend()
plt.title("FPS Models")
plt.show()

# Tournament Plots

plt.plot(x, results3, label = "Single_Point/Swap")
plt.plot(x, results4, label = "Arithmetic/Swap")
plt.plot(x, results7, label = "Single_Point/Inversion")
plt.plot(x, results8, label = "Arithmetic/Inversion")
plt.xlabel("Generations")
plt.ylabel("Fitness")
plt.legend()
plt.title("Tournament Models")
plt.show()

# Ranking Plots

plt.plot(x, results9, label = "Single_Point/Swap")
plt.plot(x, results10, label = "Arithmetic/Swap")
plt.xlabel("Generations")
plt.ylabel("Fitness")
plt.legend()
plt.title("Ranking Models")
plt.show()

# Best ones Plot

plt.plot(x, results5, label = "Fps/Single_Point/Inversion")
plt.plot(x, results3, label = "Tournament/Single_Point/Swap")
plt.plot(x, results9, label = "Ranking/Single_Point/Swap")
plt.xlabel("Generations")
plt.ylabel("Fitness")
plt.legend()
plt.title("Best Models")
plt.show()

# all models plot

plt.plot(x, results1, label = "Fps/Single_Point/Swap")
plt.plot(x, results2, label = "Fps/Arithmetic/Swap")
plt.plot(x, results5, label = "Fps/Single_Point/Inversion")
plt.plot(x, results6, label = "Fps/Arithmetic/Inversion")
plt.plot(x, results3, label = "Tournament/Single_Point/Swap")
plt.plot(x, results4, label = "Tournament/Arithmetic/Swap")
plt.plot(x, results7, label = "Tournament/Single_Point/Inversion")
plt.plot(x, results8, label = "Tournament/Arithmetic/Inversion")
plt.plot(x, results9, label = "Ranking/Single_Point/Swap")
plt.plot(x, results10, label = "RankingArithmetic/Swap")
plt.xlim((1))
plt.xlabel("Generations")
plt.ylabel("Fitness")
plt.legend()
plt.title("All models")
plt.show()


