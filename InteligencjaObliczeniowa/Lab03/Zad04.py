import pandas as pd
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("diabetes.csv")

mapping = {name: i for i, name in enumerate(df['class'].unique(), start=1)}

df['class_id'] = df['class'].map(mapping)
df.drop(columns='class', inplace=True)

num_cols = df.select_dtypes(['number']).columns
num_cols = num_cols.drop('pregnant-times')
num_cols = num_cols.drop('pedigree-func')
for col in num_cols:
    df[col] = df[col].replace(0, df[col].median())
    df[col] = df[col].fillna(df[col].mean())

# Glucose
median = df.loc[(df["glucose-concentr"] < 50) | (df["glucose-concentr"] > 200), "glucose-concentr"].median()
df.loc[(df["glucose-concentr"] < 50) | (df["glucose-concentr"] > 200), "glucose-concentr"] = median

# Blood Pressure
median = df.loc[(df["blood-pressure"] < 30) | (df["blood-pressure"] > 150), "blood-pressure"].median()
df.loc[(df["blood-pressure"] < 30) | (df["blood-pressure"] > 150), "blood-pressure"] = median

# Skin Thickness
median = df.loc[(df["skin-thickness"] < 10) | (df["skin-thickness"] > 200), "skin-thickness"].median()
df.loc[(df["skin-thickness"] < 10) | (df["skin-thickness"] > 200), "skin-thickness"] = median

# Insulin
median = df.loc[(df["insulin"] < 10) | (df["insulin"] > 1000), "insulin"].median()
df.loc[(df["insulin"] < 10) | (df["insulin"] > 1000), "insulin"] = median

# Mass Index (BMI)
median = df.loc[(df["mass-index"] < 10) | (df["mass-index"] > 60), "mass-index"].median()
df.loc[(df["mass-index"] < 10) | (df["mass-index"] > 60), "mass-index"] = median

# Pedigree Function
median = df.loc[(df["pedigree-func"] < 0) | (df["pedigree-func"] > 5), "pedigree-func"].median()
df.loc[(df["pedigree-func"] < 0) | (df["pedigree-func"] > 5), "pedigree-func"] = median

print(df)

(train_set, test_set) = train_test_split (df.values, train_size=0.7,
                                           random_state=278008)
train_inputs = train_set[:, 0:8]
train_classes = train_set[:, 8]
test_inputs = test_set[:, 0:8]
test_classes = test_set[:, 8]


print("DECISION TREE")
tree = DecisionTreeClassifier(
    max_depth = None,
    random_state = 278008
)

tree.fit(train_inputs, train_classes)
tree_accuracy = tree.score(test_inputs, test_classes)
print(f"Accuracy: {tree.score(test_inputs, test_classes):.2f}")

cm = confusion_matrix(test_classes, tree.predict(test_inputs), labels=tree.classes_)

print(cm)

knn3 = KNeighborsClassifier(n_neighbors = 3)
knn3.fit(train_inputs, train_classes)
knn3_accuracy = knn3.score(test_inputs, test_classes)
print(f"Accuracy: {knn3.score(test_inputs, test_classes):.2f}")

cm_knn3 = confusion_matrix(test_classes, knn3.predict(test_inputs), labels=knn3.classes_)

print(cm_knn3)

knn5 = KNeighborsClassifier(n_neighbors = 5)
knn5.fit(train_inputs, train_classes)
knn5_accuracy = knn5.score(test_inputs, test_classes)
print(f"Accuracy: {knn5.score(test_inputs, test_classes):.2f}")

cm_knn5 = confusion_matrix(test_classes, knn5.predict(test_inputs), labels=knn5.classes_)

print(cm_knn5)

knn11 = KNeighborsClassifier(n_neighbors = 11)
knn11.fit(train_inputs, train_classes)
knn11_accuracy = knn11.score(test_inputs, test_classes)
print(f"Accuracy: {knn11.score(test_inputs, test_classes):.2f}")

cm_knn11 = confusion_matrix(test_classes, knn11.predict(test_inputs), labels=knn11.classes_)

print(cm_knn11)

nb = GaussianNB()

nb.fit(train_inputs, train_classes)
nb_accuracy = nb.score(test_inputs, test_classes)
print(f"Accuracy: {nb.score(test_inputs, test_classes):.2f}")
cm_nb = confusion_matrix(test_classes, nb.predict(test_inputs), labels=nb.classes_)

print(cm_nb)


norm = MinMaxScaler()
normalized = norm.fit_transform(train_inputs, train_classes)


mlp4_2_1 = MLPClassifier(hidden_layer_sizes = (2,), max_iter = 10000)
mlp4_2_1.fit(train_inputs, train_classes)

prediction = mlp4_2_1.predict(test_inputs)
print("4-2-1")
print(mlp4_2_1.n_iter_)
mlp_4_2_1_accuracy = accuracy_score(test_classes, prediction)
print(f"Accuracy: {accuracy_score(test_classes, prediction)}")
print(f"Confusion Matrix:\n{confusion_matrix(test_classes, prediction)}")

mlp4_3_1 = MLPClassifier(hidden_layer_sizes = (3,), max_iter = 1000)
mlp4_3_1.fit(train_inputs, train_classes)

prediction = mlp4_3_1.predict(test_inputs)
print("4-3-1")
print(mlp4_3_1.n_iter_)
mlp_4_3_1_accuracy = accuracy_score(test_classes, prediction)
print(f"Accuracy: {accuracy_score(test_classes, prediction)}")
print(f"Confusion Matrix:\n{confusion_matrix(test_classes, prediction)}")

mlp4_2_2_1 = MLPClassifier(hidden_layer_sizes = (2,2), max_iter = 1000)
mlp4_2_2_1.fit(train_inputs, train_classes)

prediction = mlp4_2_2_1.predict(test_inputs)
print("4-2-2-1")
print(mlp4_2_2_1.n_iter_)
mlp_4_2_2_1_accuracy = accuracy_score(test_classes, prediction)
print(f"Accuracy: {accuracy_score(test_classes, prediction)}")
print(f"Confusion Matrix:\n{confusion_matrix(test_classes, prediction)}")

values = [tree_accuracy, knn3_accuracy, knn5_accuracy, knn11_accuracy, nb_accuracy, mlp_4_2_1_accuracy, mlp_4_3_1_accuracy, mlp_4_2_2_1_accuracy]
labels = ["Decision Tree", "KNN3", "KNN5", "KNN11", "Gauss", "4_2_1", "4_3_1", "4_2_2_1"]

plt.bar(labels, values)
plt.ylim(0, 1)
for i, v in enumerate(values):
    plt.text(i, v + 0.01, f"{round(v * 100, 2)}%", ha="center")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()