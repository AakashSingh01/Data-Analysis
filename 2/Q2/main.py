def nonlinearcheck(a,b):
    for i in range(4):
        x = np.polyfit(a,b,i)
        print(i,"order Equation:",x)
   

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/NUTRITION.csv',  header=0,  skiprows=[1])
coff = np.corrcoef(data['sugars'],data['rating'])[0][1]

print("Correlation coefficient = ",coff,"\n This implies sugar and rating has negative correlation.\n")
print("(r square )r^2 = ",coff**2)

nonlinearcheck(data['sugars'],data['rating'])
fit = np.polyfit(data['sugars'],data['rating'],3)
fit_fn = np.poly1d(fit) 
plt.clf()
plt.plot(data['sugars'],data['rating'], 'yo', np.sort(data['sugars']), fit_fn(np.sort(data['sugars'])), '--k')
plt.show()

print("Here we can see that the coeffcients are samller for higer order terms.")
print("Hence the  correlation is almost linear.")