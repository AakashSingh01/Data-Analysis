def func(tmp):
    print("Mean : ",data[tmp].mean())
    sv=data[tmp].sample(50).var()
    pv=data[tmp].var()
    print("Sample Variance : ",sv)
    print("Population Variance : ",pv)
    print("Difference in Sample and Population Variances : ",abs(sv-pv))

import pandas as pd
data = pd.read_csv('data/IRIS.csv')

typ = [ 'SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']

for i in typ:
    print(i)
    func(i)
    print()
