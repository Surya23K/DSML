from sklearn.neighbors import KNeighborsClassifier

X = [[8, 6], [5, 6], [7, 3], [6, 9]]
y = ['outstanding', 'good', 'good', 'outstanding']

classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(X, y)
student= [[5, 7]]
print("Student is predicted as:", classifier.predict(student))

