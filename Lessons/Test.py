#classifier
from sklearn import tree
a=1
b=2
features=[[a,1],[a,1],[b,0],[b,0]]
labels=[0,0,1,1]
clf=tree.DecisionTreeClassifier()
clf=clf.fit(features,labels)
print (clf.predict([[b,0]]))
