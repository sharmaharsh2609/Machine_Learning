#! /home/harsh/Machine_learning/ML_virtual_env/bin/python

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

X = pd.read_csv("./Training Data/Linear_X_Train.csv").values
Y = pd.read_csv("./Training Data/Linear_Y_Train.csv").values

theta = np.load("ThetaList.npy")  # load the theta list that is saced at end if file 2.ipynb
# theta is if size 100x2 originally
T0  = theta[:,0]
T1 = theta[:,1]

plt.ion()  # ion means interactive on which means turn on the interactive mode. 
for i in range(0,50,3):  # we draw images at each 3rd step for better visualization
    y_ = T1[i]*X + T0  
    # This plots all the points 
    plt.scatter(X,Y)
    # This plots our line at each step as y_ changes in each steo
    plt.plot(X,y_,'red')
    plt.draw()
    plt.pause(1)
    plt.clf()  # It destroys the interactive plot so that new will be plotted in next iteration at beginning.
    
##### From output, we can see that line moves towards best fit at fast rate initially and then it moves slowly later bcoz it reaches to the saturation point after that.