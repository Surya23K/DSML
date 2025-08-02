from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
irisdata=load_iris()
x=irisdata.data
y=irisdata.target
print("x values")
print(x)
print("y values")
print(y)
x_train,x_test,y_train,y_test=train_test_split(x,y)
print("X Train values")
print(x_train)
print("X Test values")
print(x_test)
print("Y Train values")
print(y_train)
print("Y Test values")
print(y_test)