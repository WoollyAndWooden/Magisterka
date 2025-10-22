import pandas as pd
from sklearn.model_selection import train_test_split


def classify_iris(sl, sw, pl, pw):
    if sl > 4:
        return("Setosa")
    elif pl <= 5:
        return("Virginica")
    else:
        return("Versicolor")


df = pd.read_csv("iris_big.csv")

(train_set, test_set) = train_test_split (df.values, train_size=0.7,
                                           random_state=278008)
train_inputs = train_set[:, 0:4]
train_classes = train_set[:, 4]
test_inputs = test_set[:, 0:4]
test_classes = test_set[:, 4]
good_predictions = 0
len = test_set.shape[0]

for i in range(len):
    if classify_iris(test_inputs[i][0], test_inputs[i][1],
                     test_inputs[i][2], test_inputs[i][3]) == test_classes[i]:
        good_predictions += 1

print(good_predictions)
print(good_predictions / len * 100, "%")


