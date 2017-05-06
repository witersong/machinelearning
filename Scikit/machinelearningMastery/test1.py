
import random, pandas
import  numpy as np
from sklearn.feature_selection.univariate_selection import SelectKBest
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2


text = [ "one","two","three","four","five","six","seven","eight","nine","ten" ]
data = [ { "name": text[random.randint(0,9)], "number": random.randint(0,99)} \
                        for i in range(0,10000) ]
df = pandas.DataFrame(data)
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dfr = pandas.read_csv("pima-indians-diabetes.data.txt", sep=",", encoding="utf8",names=names)
array = dfr.values
X = array[: ,0:8]
Y = array[: ,8]
test = SelectKBest(score_func=chi2,k=4)
fit = test.fit(X,Y)
np.set_printoptions(precision=3)
print(fit.scores_)
features = fit.transform(X)
print(features[0:5,:])

import matplotlib.pyplot as plt
t= np.arrange(0.,5.,0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()



'''
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
df  =pandas.read_csv("pima-indians-diabetes.data.txt",names=names)
array =df.values
X = array[:,0:8]
Y = array[:,8]

model = LogisticRegression()
rfe = RFE(model, 3)
fit = rfe.fit(X, Y)
print("Num Features: %d") % fit.n_features_
print("Selected Features: %s") % fit.support_
print("Feature Ranking: %s") % fit.ranking_


# Feature Extraction with Univariate Statistical Tests (Chi-squared for classification)
import pandas
import numpy
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
# load data
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pandas.read_csv("pima-indians-diabetes.data.txt", names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
print(Y)

'''