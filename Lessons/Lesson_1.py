#classifier
import sqlite3
from sklearn import tree
features=[  [21,11,98],
            [20,12,96],
            [34,03,88],
            [36,04,89],
            [33,15,99]
        ]
labels=[0,0,1,1,1]
clf=tree.DecisionTreeClassifier()
clf=clf.fit(features,labels)
print (clf.predict([[21,0,98]]))
