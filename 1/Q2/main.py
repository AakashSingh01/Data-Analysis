def five_point_summary(tmp):
    print( "1. Sample Minimum : ",tmp.min())
    print( "2. Lower Quartile : ",np.percentile(tmp, 25) )
    print( "3. Sample Median : ",tmp.median() )
    print( "4. Upper Quartile : ",np.percentile(tmp, 75) )
    print( "5. Sample Maximum : ",tmp.max())
    m = tmp.median() 
    r = (np.percentile(tmp, 75) - np.percentile(tmp, 25))*1.5
    t1 = tmp[ tmp < (m-r)  ]
    t2 = tmp[ tmp > (m+r)  ]    
    tmp = tmp[ tmp > (m-r)  ]
    tmp = tmp[ tmp < (m+r)  ]
    print( "\nNo. of outliers : ",t1.count()+t2.count() )
    return tmp
   

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Columns= ['Time', 'Latitude', 'Longitude', 'Depth/Km', 'Magnitude']
data = pd.read_csv('data/EARTHQUAKE.csv')

print("Depth/Km :")
bp1=five_point_summary(data['Depth/Km'])
print("\n\n\nMagnitude :")
bp2=five_point_summary(data['Magnitude'])

print("\n\n\nBox Plot of Depth/Km and Magnitude : ")

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax1.boxplot(bp1.values)
ax2 = fig.add_subplot(122)
ax2.boxplot(bp2.values)
plt.show()