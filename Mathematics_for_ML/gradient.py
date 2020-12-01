import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt 

print('Python :{} '.format(sys.version))
print('Numpy :{} '.format(np.__version__))
print('Matplotlib :{}'.format(matplotlib.__version__))

# Generate 2D meshgrid
nx,ny = (100,100)

x=np.linspace(0,10,nx)
y=np.linspace(0,10,ny)

xv , yv = np.meshgrid(x,y)

#Define a function to plot
def f(x,y):
    return x *(y**2)

# calculate z value for each x,y
z =f(xv ,yv)

# Make a clor to display the chart
plt.figure(figsize=(14,12))
plt.pcolor(xv,yv,z)
plt.title('2D color plot of f(x,y) = xy^2')
plt.colorbar()
plt.show()

# Generate 2D mesh grid for the gradient
nx,ny =(10,10)
x=np.linspace(0,10,nx)
y=np.linspace(0,10,ny)
xg,yg = np.meshgrid(x,y)

#calculate the gradient of f(x,y)
Gy,Gx = np.gradient(f(xg,yg))

#Make a color plot to display the data
plt.figure(figsize=(14,12))
plt.pcolor(xv,yv,z)
plt.title('Gradient of f(x,y) = xy^2')
plt.colorbar()
plt.quiver(xg,yg,Gx,Gy,scale = 1000, color = 'w')
plt.show()

# Calculate the gradient of f(x,y) = xy^2
def ddx(x,y):
    return y ** 2

def ddy(x,y):
    return 2 * x * y

Gx=ddx(xg,yg)
Gy=ddy(xg,yg)

plt.figure(figsize=(14,12))
plt.pcolor(xv,yv,z)
plt.title('Plot of [y^2,2xy]')
plt.colorbar()
plt.quiver(xg,yg,Gx,Gy,scale = 1000, color = 'w')
plt.show()





