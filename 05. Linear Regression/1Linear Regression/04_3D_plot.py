#! /home/harsh/Machine_learning/ML_virtual_env/bin/python

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from warnings import filterwarnings
filterwarnings("ignore") # to remove all the warnings

x = np.arange(-1,1,0.02)  # from -1 to 1 with a gap of 0.02
y = x 
x,y = np.meshgrid(x,y)

fig = plt.figure()
axes = fig.gca(projection='3d')
# axes.surface_plot(x,y,x**2+y**2,cmap='rainbow') # try executing this also
axes.contour(x,y,x**2+y**2,cmap='rainbow')
plt.show()
## PRESS 'q' TO CLOSE THE WINDOW

## For this program you need to install tkinter module as it opens window using tkinter module