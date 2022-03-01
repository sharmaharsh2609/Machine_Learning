# try:
from sklearn.datasets import make_circles  ## to generate data
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  ## to make 3d plot
import numpy as np
from sklearn.linear_model import LogisticRegression

X,Y = make_circles(n_samples=500,noise=0.02) ## generate data

def phi(X):
    """"Non Linear Transformation"""
    X1 = X[:,0]
    X2 = X[:,1]
    X3 = X1**2 + X2**2

    X_ = np.zeros((X.shape[0],3)) ## X bar is transformed array.
    print(X_.shape)

    X_[:,:-1] = X
    X_[:,-1] = X3

    return X_
X_ = phi(X)    
    
lr = LogisticRegression()  ## create object
lr.fit(X_, Y)  ## do training
bias = lr.intercept_
wts = lr.coef_
xx,yy = np.meshgrid(range(-2,2),range(-2,2))  ## create meshgrid
z = -(wts[0,0]*xx + wts[0,1]*yy+bias)/wts[0,2]
    
def plot3d(X):
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111,projection='3d')

    ax.plot_surface(xx,yy,z,alpha=0.2) ## alpha is opacity level of plane
    ax.scatter(X[:,0],X[:,1],X[:,2],zdir='z',s=20,c=Y,cmap=plt.cm.Accent, depthshade=True)
    plt.show()

plot3d(X_)  ## call function
    
# except:
#     print("Activate virtual environment and then execute with command: 'python3 4.2lr_on_3d.py'")
    
## or we can use #! /home/harsh/Machine_learning/ML_virtual_env/bin/python at beginning and then execute this file as ./4.2lr_on_3d.py