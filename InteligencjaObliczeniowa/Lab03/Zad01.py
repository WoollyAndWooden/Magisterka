from math import e
from sys import argv


def forwardPass(age, weight, height):
    activate = lambda x : 1 / (1+(e**(-x)))
    hidden1 = (age * -0.46122) + (weight * 0.97314) + (height * -0.39203) + 0.80109
    hidden2 = (age * 0.78548) + (weight * 2.10584) + (height * -0.57847) + 0.43529

    return round(activate(hidden1) * -0.815546 + activate(hidden2) * 1.03775 + -0.2368, 5)

print(forwardPass(float(argv[1]), float(argv[2]), float(argv[3])))


