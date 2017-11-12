import pandas as pd
import scipy.stats as ss

data = pd.read_csv('data/SNACKS.csv')
matrix=ss.spearmanr(data)
print("Corelation Matrix : \n",matrix[0])
coeff_deter = matrix[0]**2
print("\n\nCoefficient of determination :",coeff_deter)



