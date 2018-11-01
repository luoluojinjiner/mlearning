import numpy as np
from numpy.linalg import cholesky
import matplotlib.pyplot as plt

sampleNo = 1000
mu = np.array([[1, 5]])
Sigma = np.array([[10, 5], [5, 5]])
R = cholesky(Sigma).T
va,vc = np.linalg.eig(Sigma); R2 = (np.diag(va)**0.5)@vc.T

#s1 = np.random.randn(sampleNo, 2) @ R + mu #法1
#s2 = np.random.randn(sampleNo, 2) @ R2 + mu #法2
s3 = np.random.multivariate_normal(mu[0],Sigma,sampleNo) #法3

#plt.plot(*s1.T,'.',label = 's1')
#plt.plot(*s2.T,'.',label = 's2')
plt.plot(*s3.T,'.',label = 's3')
plt.axis('scaled')
plt.legend()
plt.show()