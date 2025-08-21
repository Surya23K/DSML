chills=['Y','Y','Y','N','N','N','N','Y']
running_nose=['N','Y','N','Y','N','Y','Y','Y']
fever=['Y','N','Y','Y','N','Y','N','Y']
headache=['Mild','No','Strong','Mild','No','Strong','Strong','Mild']
flu=['N','Y','Y','Y','N','Y','N','Y']
from heapq import merge 
from sklearn import preprocessing 
le=preprocessing.LabelEncoder()
chills_encoded=le.fit_transform(chills)
print("chills:",chills_encoded)
running_nose_encoded=le.fit_transform(running_nose)
print("running_nose:",running_nose_encoded)
fever_encoded=le.fit_transform(fever)
print("fever:",fever_encoded)
headache_encoded=le.fit_transform(headache)
print("headache:",headache_encoded)
flu_le=preprocessing.LabelEncoder()
label=flu_le.fit_transform(flu) 

print("flu:",label)
features=list(zip(chills_encoded,running_nose_encoded,fever_encoded,headache_encoded))
print(features)
from sklearn.naive_bayes import GaussianNB
model=GaussianNB()
model.fit(features,label)
predicted=model.predict([[1,1,0,0]])
print("predicted value:",predicted)
print(flu_le.inverse_transform(predicted)) 