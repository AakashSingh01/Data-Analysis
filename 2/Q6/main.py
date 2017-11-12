def stock(t,share,names,y):
    import matplotlib.pyplot as plt
    from sklearn.linear_model import LinearRegression
    import statsmodels.api as sm
    ls=[share[i] for i in range (126217) if(names[i]==t)]
    #plt.plot(ls)
    #plt.show()
    model = sm.OLS(y, ls).fit()
    print("Predicted value for",t," is :",model.predict([250]))
       
            

import pandas as pd
import scipy.stats.mstats as sc

data = pd.read_csv('data/STOCKS.csv')
Columns= ['Close', 'Name']
a=list(set(data['Name']))
y=[i+1 for i in range (252)]
#for i in a :
 #   print(i,"curve : ")

