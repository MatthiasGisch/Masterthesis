from sklearn import datasets
import matplotlib.pyplot as plt

from LDA import LDA

data = datasets.load_iris()
X = data.data
y = data.target

lda = LDA(2)
lda.fit(X,y)
X_projected = lda.transform(X)

print('Shape of X:', X.shape)
print('Shape of transformed X:', X_projected.shape)

x1 = X_projected[:, 0]
x2 = X_projected[:, 1]

plt.scatter(x1, x2,
            c=y, edgecolors='none', alpha=0.8)

plt.xlabel('Linear Discriminant 1')
plt.ylabel('Linear Discriminant 2')
plt.colorbar()
plt.show