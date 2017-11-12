def clean (temp):
    temp = temp.replace('Not Provided',np.nan)
    temp = temp.astype('float64', raise_on_error = False)
    avg = temp.sum()/temp.notnull().sum()
    temp= temp.fillna(value=avg)
    return temp
    
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

col=['BasePay', 'OvertimePay', 'OtherPay', 'Benefits']

data = pd.read_csv('data/SALARY.csv')

for i in col :
    data[i]=clean(data[i])

col=[ 'OvertimePay', 'OtherPay', 'Benefits']

for i in col:
   plt.plot(data['BasePay'], data[i], 'ro')
   plt.show()

print("The graphs showing the following behaviour:: ")
print(" -Over time pay is highest for employees having average basic pay and lowest for the employees having high basic pay.")
print(" -Other pay decreases with increase in basic pay.")
print(" -Benefits increases with increase in basic pay")
