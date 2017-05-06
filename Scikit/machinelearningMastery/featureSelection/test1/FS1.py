import matplotlib.pyplot as plt
from sklearn import datasets

from sklearn.feature_selection import univariate_selection
iris = datasets.load_iris()
X =iris.data[:,:2]
Y =iris.target


plt.figure(2,figsize=(8,6))
plt.clf()

plt.scatter(X[:,0],X[:,1]);
plt.show()