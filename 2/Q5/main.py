import numpy as np
import pandas as pd
data = pd.read_csv('data/GAMES.csv')

ac=[]
nonac=[]
for i in range (16719):
    if(data['User_Score'][i] is not np.nan and data['User_Score'][i] != 'tbd'):
        if(data['Genre'][i]=='Action'):
            ac.append(data['User_Score'][i])
        else :
            nonac.append(data['User_Score'][i])
#ac.remove('tbd')
ac=[float(i) for i in ac]
nonac=[float(i) for i in nonac]
print("                 Average rating")
print("Action films : ",np.mean(ac))
print("Other films  : ",np.mean(nonac))

print("Here hypothesis fails that action films are  more rated.")
