from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("iris_big.csv")

mapping = {name: i for i, name in enumerate(df['target_name'].unique(), start=1)}

df['target_id'] = df['target_name'].map(mapping)
df.drop(columns='target_name', inplace=True)

(train_set, test_set) = train_test_split (df.values, train_size=0.7,
                                           random_state=278008)
train_inputs = train_set[:, 0:4]
train_classes = train_set[:, 4]
test_inputs = test_set[:, 0:4]
test_classes = test_set[:, 4]

norm = MinMaxScaler()
normalized = norm.fit_transform(train_inputs, train_classes)


mlp4_2_1 = MLPClassifier(hidden_layer_sizes = (2,), max_iter = 10000)
mlp4_2_1.fit(train_inputs, train_classes)

prediction = mlp4_2_1.predict(test_inputs)
print("4-2-1")
print(mlp4_2_1.n_iter_)
print(f"Accuracy: {accuracy_score(test_classes, prediction)}")
print(f"Confusion Matrix:\n{confusion_matrix(test_classes, prediction)}")

mlp4_3_1 = MLPClassifier(hidden_layer_sizes = (3,), max_iter = 1000)
mlp4_3_1.fit(train_inputs, train_classes)

prediction = mlp4_3_1.predict(test_inputs)
print("4-3-1")
print(mlp4_3_1.n_iter_)
print(f"Accuracy: {accuracy_score(test_classes, prediction)}")
print(f"Confusion Matrix:\n{confusion_matrix(test_classes, prediction)}")

mlp4_2_2_1 = MLPClassifier(hidden_layer_sizes = (2,2), max_iter = 1000)
mlp4_2_2_1.fit(train_inputs, train_classes)

prediction = mlp4_2_2_1.predict(test_inputs)
print("4-2-2-1")
print(mlp4_2_2_1.n_iter_)
print(f"Accuracy: {accuracy_score(test_classes, prediction)}")
print(f"Confusion Matrix:\n{confusion_matrix(test_classes, prediction)}")