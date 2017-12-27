def build_roc(Y,y):
    fpr, tpr, thresholds = roc_curve(Y, y[:, 1])
    import matplotlib.pyplot as plt
    plt.plot(fpr, tpr)
    plt.show()



def naive_bayes_GB(X_train, X_test,Y_train, Y_test):
    from sklearn.naive_bayes import GaussianNB

    clf = GaussianNB()
    clf.fit(X_train, Y_train)
    Y = clf.predict(X_test)
    Y=Y.reshape(-1, 1)
    print(confusion_matrix(Y_test,Y))
    y = clf.predict_proba(X_test)
    build_roc(Y_test,y)  
    print("Accuracy : ",accuracy_score(Y_test,Y))
    print("Precision : ",precision_score(Y_test,Y))
    return accuracy_score(Y_test,Y), precision_score(Y_test,Y)



def decision_tree(X_train, X_test,Y_train, Y_test):
    from sklearn import tree

    clf = tree.DecisionTreeClassifier()
    clf.fit(X_train, Y_train)
    Y = clf.predict(X_test)
    Y=Y.reshape(-1, 1)
    print(confusion_matrix(Y_test,Y))
    y = clf.predict_proba(X_test)
    build_roc(Y_test,y)
    print("Accuracy : ",accuracy_score(Y_test,Y))
    print("Precision : ",precision_score(Y_test,Y))
    return accuracy_score(Y_test,Y),precision_score(Y_test,Y)



def support_vector_machine(X_train, X_test,Y_train, Y_test):
    from sklearn import svm

    clf = svm.SVC()
    clf.fit(X_train, Y_train)
    Y = clf.predict(X_test)
    Y=Y.reshape(-1, 1)
    print(confusion_matrix(Y_test,Y))
    print("Accuracy : ",accuracy_score(Y_test,Y))
    print("Precision : ",precision_score(Y_test,Y))
    return accuracy_score(Y_test,Y),precision_score(Y_test,Y)




import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import roc_curve

df = pd.read_csv('CCD.csv')

df['churn'] = [ 1 if x==' True' else 0 for x in df['churn'] ]
df['international_plan'] = [ 1 if x==' yes' else 0 for x in df['international_plan'] ]
df['voice_mail_plan'] = [ 1 if x==' yes' else 0 for x in df['voice_mail_plan'] ]
churn = df['churn']
drop = ['Id','state','area_code','phone_number','churn']
df = df.drop(drop,axis=1)

sss = StratifiedShuffleSplit(n_splits=3, test_size=0.25, random_state=0)

nb_a,nb_p=0,0
dt_a,dt_p=0,0
svm_a,svm_p=0,0
i=0
for train_index, test_index in sss.split(df, churn):

   X_train, X_test = df.iloc[train_index], df.iloc[test_index]
   Y_train, Y_test = churn.iloc[train_index], churn.iloc[test_index]
   i+=1
   print("\n\nConfusion Matrix for ",i," testing set with Naive Bayes Classification :")
   a,p=naive_bayes_GB(X_train, X_test,Y_train, Y_test)
   nb_a+=a
   nb_p+=p
   print("\n\nConfusion Matrix for ",i," testing set with Decision Tree Classification :")
   a,p=decision_tree(X_train, X_test,Y_train, Y_test)
   dt_a+=a
   dt_p+=p
   print("\n\nConfusion Matrix for ",i," testing set with Support Vector Machines Classification :")
   a,p=support_vector_machine(X_train, X_test,Y_train, Y_test)
   svm_a+=a
   svm_p+=p

   
print("\nAverage Accuracy and Precision with Naive Bayes Classification : ")
print(nb_a/3,nb_p/3)

print("\nAverage Accuracy and Precision with Decision Tree Classification : ")
print(dt_a/3,dt_p/3)

print("\nAverage Accuracy and Precision with Support Vector Machines Classification : ")
print(svm_a/3,svm_p/3)

print("\nWe can see Decision tree is providing better accuracy and ROC curves. ")
print("Hence Desicion Tree model is preferable here.")