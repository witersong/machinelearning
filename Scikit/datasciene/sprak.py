from sklearn import svm
from sklearn import cluster, datasets
clf = svm.SVC()
iris = datasets.load_iris()
X_iris,y_iris = iris.data,iris.target
clf.fit(X_iris, y_iris)
list(clf.predict(iris.data[:3]))
clf.fit(iris.data, iris.target_names[iris.target])

x_min, x_max = X_iris[:, 0].min() - .5, X_iris[:, 0].max() + .5

print(x_max,x_min)