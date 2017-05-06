
from sklearn.feature_selection import  variance_threshold
from sklearn import datasets
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
import  pandas as pd
import  numpy  as np

class C:
    def getFeatureSelection(self):
        dataset = datasets.load_iris()
        model = LogisticRegression()
        rfe =RFE(model,3)
        rfe.fit(dataset.data,datasets.target)
        print(rfe.support_)

    def getPreprocssing (self):
        print('preprocessing')

    def getData(self):
        X = pd.read_csv(input, sep=",", header=0, delimiter=',',encoding ='utf-8')

if __name__ == '__main__':
    input = 'data1.csv'
    c = C()
    c.getData(input);
    c.getFeatureSelection();