from sklearn import datasets
iris=datasets.load_iris()

X=iris.data
Y=iris.target

from sklearn.cross_validation import train_test_split
