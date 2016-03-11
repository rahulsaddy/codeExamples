import numpy as np

np.zeros(10)

np.arange(10,50)

z = np.arange(10)
z = z[::-1]    # to reverse the vector

Z = np.arange(9).reshape(3,3) # reshaping

np.nonzero(z) # to check for non zero entries

np.eye(3)

z = np.random.random((3,3))
z.min() z.max() z.mean()

Z = np.diag(1+np.arange(4),k=-1) # below diagonal matrix, k=0 for diagonal

