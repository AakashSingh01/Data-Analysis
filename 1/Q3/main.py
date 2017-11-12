def clean (temp):
    temp = temp.replace('?',np.nan)
    temp = temp.astype('float64', raise_on_error = False)
    avg = temp.sum()/temp.notnull().sum()
    temp= temp.fillna(value=avg)
    return temp
    
def distribution(dat):
    kde = gaussian_kde( dat )
    dist_space = linspace( min(dat), max(dat), 100 )
    plt.plot( dist_space, kde(dist_space) )

import numpy as np
import pandas as pd
from scipy.stats.kde import gaussian_kde
from numpy import linspace
from matplotlib import pyplot as plt
data = pd.read_csv('data/AUTOMOBILES.csv')
# [ 'normalized-losses', 'wheel-base', 'length', 'width', 'height', 'curb-weight',  'engine-size',  'bore', 'stroke', 'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg', 'price']

print("Nominal : symboling,make,fuel-type,body-style,drive-wheels,engine-location,engine-type,fuel-system,")
print("\nOrdinal : aspiration,num-of-doors,num-of-cylinders,")
print("\nInterval : wheel-base,length,width,height,curb-weight,engine-size,bore,stroke,compression-ratio,")
print("\nRatio : normalized-losses,horsepower,peak-rpm,city-mpg,highway-mpg,price")

typ = [ 'normalized-losses', 'bore', 'stroke',  'horsepower', 'city-mpg','peak-rpm', 'price']

for i in typ :
    data[i] = clean ( data[i] )

for i in typ :   
    print('\n\n',i,"\nMean : ",data[i].mean())
    print("Median : ",data[i].median())
    print("Mode : ",data[i].mode())

distribution(data['peak-rpm'])
distribution(data['city-mpg'])
