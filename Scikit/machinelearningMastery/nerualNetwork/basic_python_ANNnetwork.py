import numpy as np
import matplotlib as plt
import  pandas
from sklearn.feature_selection import VarianceThreshold

from sklearn.svm import  LinearSVC
from sklearn.feature_selection  import SelectFromModel
from sklearn.model_selection import train_test_split
pandas.read_csv('');
X = np.array([ [0,0,1],[0,1,1],[1,0,1],[1,1,1] ])
Y = np.array([0,1,1,0],dtype=int,copy=bool)
syn0 = 2*np.random.random((3,5))-1
syn1 = 2*np.random.random((4,1))-1
