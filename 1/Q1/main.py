import pandas as pd
import scipy.stats.mstats as sc

data = pd.read_csv('data/CARS.csv')

print("SPEED:\nArithmetic Mean = " +str(data['speed'].mean()) )
print("Geometric Mean = " +str(sc.gmean(data['speed'])) )  
print("Harmonic Mean = " +str(sc.hmean(data['speed'])) +"\n") 

print("Distance:\nArithmetic Mean = " +str(data['dist'].mean()) )
print("Geometric Mean = " +str(sc.gmean(data['dist'])) )  
print("Harmonic Mean = " +str(sc.hmean(data['dist']))) 