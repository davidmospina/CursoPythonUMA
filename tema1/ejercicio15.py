import numpy as np

X1 = [2,3,4,6,12,18,22,33,40,45,50,57]
X2 = np.array = [2,3,4,6,12,18,22,33,40,45,50,57]

# C1 = np.sum(X2)
# C2 = 0
# for valor in X2:
#     C2 +=valor
# print(C1)
# print(C2)

for i in range(len(X1)):
    X1[i] += 30

print(X1)

X3 = X2 + np.ones(len(X2))*30

print(X3)


