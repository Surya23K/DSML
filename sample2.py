from sklearn.neighbors import KNeighborsClassifier

X = [[10, 9], [1, 4], [10, 1], [7, 10], [3, 10], [1, 1]]
y = ['fruit', 'protein', 'fruit', 'vegetable', 'vegetable', 'protein']

classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(X, y)
tomato = [[6, 4]]
print("Tomato is predicted as:", classifier.predict(tomato)[0])
carrot = [[4, 9]]
print("Carrot is predicted as:", classifier.predict(carrot)[0])