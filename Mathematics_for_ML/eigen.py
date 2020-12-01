import sys

import numpy as np

print('Python : {}'.format(sys.version))

print('Numpy : {}'.format(np.__version__))

from numpy import linalg

# Define an Array 
A=np.arange(9) - 3
A

B=A.reshape(3,3)

B



#Ecludian L2 norm - default
print(np.linalg.norm(A))
print(np.linalg.norm(B))

#the frogeniuos norm is the L2 norm for a matrix
print(np.linalg.norm(B,'fro'))

# the max norm ( p = infinity)
print(np.linalg.norm(A,np.inf))
print(np.linalg.norm(B,np.inf))

# Vector normalization - normalization to produce a vector
norm = np.linalg.norm(A)
A_unit = A / norm
print(A_unit)

# the magnitude of a unit vector is equal to 1
np.linalg.norm(A_unit)

#Eigendecomposition

#The eigendecomposition is one form of matrix decomposition.
#Decomposing a matrix means that we want to find a product of matrices that is equal to the initial matrix. 
#In the case of eigendecomposition, we decompose the initial matrix into the product of its eigenvectors and eigenvalues.
#Before all, let’s see the link between matrices and linear transformation. Then, you’ll learn what are eigenvectors and eigenvalues.

# find the eigen values and eigen vector for a simple squaematrix

A =np.diag(np.arange(1,4))
A

eigenvalues,eigenvectors = np.linalg.eig(A)
eigenvalues

eigenvectors

# eigenvalue w[i] corresponds to the eigenvector v[:,i]
print('Eigenvalue : {}'.format(eigenvalues[2]))
print('Eigenvector : {}'.format(eigenvectors[:,1]))

np.diag(eigenvalues)

np.linalg.inv(eigenvectors)



# verify eigen decomposition

matrix = np.matmul(np.diag(eigenvalues),np.linalg.inv(eigenvectors))
output = np.matmul(eigenvectors,matrix).astype(np.int)
print (output)



# import necessary matplotlib libraries
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
%matplotlib inline

# plot the eigen vectors
origin = [0,0,0]

fig = plt.figure(figsize=(18,10))
axl = fig.add_subplot(121, projection='3d')

axl.quiver(origin,origin,origin,eigenvectors[0,:],eigenvectors[1,:],eigenvectors[2,:],color='k')
axl.set_xlim([-3,3])
axl.set_ylim([-3,3])
axl.set_zlim([-3,3])
axl.set_xlabel('x axis')
axl.set_ylabel('y axis')
axl.set_zlabel('z axis')
axl.view_init(15,30)
axl.set_title('Before Multiplication')

#show the plot
plt.show()

# plot the eigen vectors
origin = [0,0,0]

fig = plt.figure(figsize=(18,10))
axl = fig.add_subplot(121, projection='3d')

axl.quiver(origin,origin,origin,eigenvectors[0,:],eigenvectors[1,:],eigenvectors[2,:],color='k')
axl.set_xlim([-3,3])
axl.set_ylim([-3,3])
axl.set_zlim([-3,3])
axl.set_xlabel('x axis')
axl.set_ylabel('y axis')
axl.set_zlabel('z axis')
axl.view_init(15,30)
axl.set_title('Before Multiplication')

# now lets multiply origin matrix by eigenvectors
new_eig = np.matmul(A, eigenvectors)
ax2 = plt.subplot(122,projection = '3d')
ax2.quiver(origin,origin,origin,new_eig[0,:],new_eig[1,:],new_eig[2,:],color='k')

#add the eigenvalues to the plot
ax2.plot(eigenvalues[0]*eigenvectors[0],eigenvalues[1]*eigenvectors[1],eigenvalues[2]*eigenvectors[2],'rX')
ax2.set_xlim([-3,3])
ax2.set_ylim([-3,3])
ax2.set_zlim([-3,3])
ax2.set_xlabel('x axis')
ax2.set_ylabel('y axis')
ax2.set_zlabel('z axis')
ax2.view_init(15,30)
ax2.set_title('After Multiplication')
#show the plot
plt.show()



