def func(tmp):
    lst = []
    for i in range (0,111):
        lst.append( tmp[i].mean() )
    return lst


import numpy as np
import pandas as pd
data = pd.read_csv('data/weather.csv')
typ= ['Station Name', 'Month', 'Period','No. of Years', 'Maximum Temperature', 'Minimum Temperature', 'Mean Rainfall']

city = data['Station Name'].unique()
month =data['Month'].unique()

rain = np.split(data['Mean Rainfall'], 111)
year_rain = func(rain)

MaxTemp = np.split(data['Maximum Temperature'], 111)
year_MaxTemp = func(MaxTemp)

MinTemp = np.split(data['Minimum Temperature'], 111)
year_MinTemp = func(MinTemp)

roll1 = pd.DataFrame(index=month, columns=city, data=np.transpose(rain))
roll2 = pd.DataFrame(index=city, columns=['year_rain'] ,data=year_rain )
roll2['year_MaxTemp']=year_MaxTemp
roll2['year_MinTemp']=year_MinTemp

print("\n\nFirst RollUp\n")
print(roll1)
print("\n\nSecond RollUp\n")
print(roll2)
print("\n\nFirst DrillDown\n")
print(roll1)
print("\n\nSecond DrillDown\n")
print(data)


print("\n\n Sample Slice of First RollUp\n")
print(roll1[:1])

print("\n\n Sample Dice of Second RollUp\n")
print(roll2['year_rain'])