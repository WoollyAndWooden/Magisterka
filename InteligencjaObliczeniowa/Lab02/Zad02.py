import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix

df = pd.read_csv("iris_big.csv")

(train_set, test_set) = train_test_split (df.values, train_size=0.7,
                                           random_state=278008)
train_inputs = train_set[:, 0:4]
train_classes = train_set[:, 4]
test_inputs = test_set[:, 0:4]
test_classes = test_set[:, 4]

tree = DecisionTreeClassifier(
    max_depth = None,
    random_state = 278008
)

tree.fit(train_inputs, train_classes)

plt.figure(figsize=(20,10))
plot_tree(tree, feature_names=['sepal_length', "sepal_width", "petal_length", "petal_width"],
class_names=tree.classes_, filled=True, rounded=True)
plt.show()

print(f"Accuracy: {tree.score(test_inputs, test_classes):.2f}")

cm = confusion_matrix(test_classes, tree.predict(test_inputs), labels=tree.classes_)

print(cm)