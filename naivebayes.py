import numpy as np
import sklearn
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])
from sklearn.naive_bayes import GaussianNB #导入GaussianNB
clf = GaussianNB() #设置clf为高斯朴素贝叶斯分类器
clf.fit(X, Y) #训练数据
print(clf.predict([[-1, 0]]))
print(clf.predict([[1,3]])) #预测数据[-1,0]属于哪一类
print(clf.predict([[1,2],[1,3]]))