def clean (temp):
    avg = temp.sum()/temp.notnull().sum()
    temp= temp.fillna(value=avg)
    return temp
    
def avg(temp,year):
    summ=0
    count=0
    for i in range(5043) :
        if(year[i]<=2015):
            summ+=temp[i]
            count+=1
    return summ/count

    
import pandas as pd
import numpy as np
import math
import scipy.stats as st

data = pd.read_csv('data/MOVIE.csv',  header=1)
hd=list(data[:0])

for i in hd :
    if isinstance(data[i][2], np.float64):
        data[i]=clean(data[i])

print("Population mean from all the movies up to 2015 on imdb_score: ",avg(data["imdb_score"],data["title_year"]))

sample = data[ data.title_year == 2016 ]

print("\n\n\n Sample:\n",sample)


pop_mean = np.mean(data.imdb_score)
sam_mean = np.mean(sample.imdb_score)
sam_sd = np.std(sample.imdb_score)
pop_sd = np.std(data.imdb_score)
sam_size = len(sample)
print("\n\nPopulation mean : ", pop_mean)
print("Sample mean : ",sam_mean )
print("Population standard deviation : ",pop_sd )
print("Sample standard deviation : ",sam_sd )
print("Sample size : ",sam_size )

Z = (sam_mean-pop_mean)/(pop_sd/math.sqrt(sam_size))
print("\n\nTest Statistics when population standard deviation is known (Z) : ",Z)
print("Critical value : ",st.norm.ppf(.95))


T = (sam_mean-pop_mean)/(sam_sd/math.sqrt(sam_size))
print("\n\nTest Statistics when population standard deviation is not known (T) : ",T)
print("Critical value : ",st.t.ppf(abs(.95),1))
