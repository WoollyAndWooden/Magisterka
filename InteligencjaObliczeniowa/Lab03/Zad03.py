import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("iris_big.csv")

# df = pd.get_dummies(df, columns=["target_name"])

(train_set, test_set) = train_test_split (df, train_size=0.7,
                                           random_state=278008)
train_inputs = train_set.drop(columns="target_name")
#train_classes = train_set[:, 4]
test_inputs = test_set.drop(columns="target_name")
#test_classes = test_set[:, 4]

train_classes = pd.get_dummies(train_set["target_name"])
test_classes = pd.get_dummies(test_set["target_name"])
test_classes = test_classes.reindex(columns=train_classes.columns, fill_value=0)

class_columns = train_classes.columns

test_inputs = test_inputs.to_numpy()
test_classes = test_classes.to_numpy()
train_classes = train_classes.to_numpy()
train_inputs = train_inputs.to_numpy()

norm = MinMaxScaler()
normalized_train = norm.fit_transform(train_inputs)
normalized_test = norm.transform(test_inputs)

mlp4_2_1 = MLPClassifier(hidden_layer_sizes = (2,), max_iter = 10000)
mlp4_2_1.fit(normalized_train, train_classes)

prediction = mlp4_2_1.predict(normalized_test)
print("4-2-1")
print(mlp4_2_1.n_iter_)
for i, col in enumerate(class_columns):
    true_col = test_classes[:, i]
    pred_col = prediction[:, i]

    print(f"Class {col}")
    print(f"Accuracy: {accuracy_score(true_col, pred_col)}")
    print(f"Confusion Matrix:\n{confusion_matrix(true_col, pred_col)}\n")


mlp4_3_1 = MLPClassifier(hidden_layer_sizes = (3,), max_iter = 10000)
mlp4_3_1.fit(normalized_train, train_classes)

prediction = mlp4_3_1.predict(normalized_test)
print("4_3_1")
print(mlp4_3_1.n_iter_)
for i, col in enumerate(class_columns):
    true_col = test_classes[:, i]
    pred_col = prediction[:, i]

    print(f"Class {col}")
    print(f"Accuracy: {accuracy_score(true_col, pred_col)}")
    print(f"Confusion Matrix:\n{confusion_matrix(true_col, pred_col)}\n")


mlp4_2_2_1 = MLPClassifier(hidden_layer_sizes = (2, 2), max_iter = 10000)
mlp4_2_2_1.fit(normalized_train, train_classes)

prediction = mlp4_2_2_1.predict(normalized_test)
print("4-2-2-1")
print(mlp4_2_2_1.n_iter_)
for i, col in enumerate(class_columns):
    true_col = test_classes[:, i]
    pred_col = prediction[:, i]

    print(f"Class {col}")
    print(f"Accuracy: {accuracy_score(true_col, pred_col)}")
    print(f"Confusion Matrix:\n{confusion_matrix(true_col, pred_col)}\n")