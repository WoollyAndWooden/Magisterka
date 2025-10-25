import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.naive_bayes import GaussianNB

df = pd.read_csv("iris_big.csv")

(train_set, test_set) = train_test_split (df.values, train_size=0.7,
                                           random_state=278008)
train_inputs = train_set[:, 0:4]
train_classes = train_set[:, 4]
test_inputs = test_set[:, 0:4]
test_classes = test_set[:, 4]

knn3 = KNeighborsClassifier(n_neighbors = 3)
knn3.fit(train_inputs, train_classes)

print(f"Accuracy: {knn3.score(test_inputs, test_classes):.2f}")

cm_knn3 = confusion_matrix(test_classes, knn3.predict(test_inputs), labels=knn3.classes_)

print(cm_knn3)

knn5 = KNeighborsClassifier(n_neighbors = 5)
knn5.fit(train_inputs, train_classes)

print(f"Accuracy: {knn5.score(test_inputs, test_classes):.2f}")

cm_knn5 = confusion_matrix(test_classes, knn5.predict(test_inputs), labels=knn5.classes_)

print(cm_knn5)

knn11 = KNeighborsClassifier(n_neighbors = 11)
knn11.fit(train_inputs, train_classes)

print(f"Accuracy: {knn11.score(test_inputs, test_classes):.2f}")

cm_knn11 = confusion_matrix(test_classes, knn11.predict(test_inputs), labels=knn11.classes_)

print(cm_knn11)

nb = GaussianNB()

nb.fit(train_inputs, train_classes)
print(f"Accuracy: {nb.score(test_inputs, test_classes):.2f}")
cm_nb = confusion_matrix(test_classes, nb.predict(test_inputs), labels=nb.classes_)

print(cm_nb)