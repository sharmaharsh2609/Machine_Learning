try:
    from sklearn.datasets import make_circles  ## to generate data
    from matplotlib import pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D  ## to make 3d plot
    import numpy as np
    X,Y = make_circles(n_samples=500,noise=0.02)

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

    def plot3d(X,show=True):
        fig = plt.figure(figsize=(10,10))
        ax = fig.add_subplot(111,projection='3d')
        X1 = X[:,0]
        X2 = X[:,1]
        X3 = X[:,2]

        ax.scatter(X1,X2,X3,zdir='z',s=20,c=Y,cmap=plt.cm.Accent, depthshade=True)
        plt.show()

    plot3d(X_)
    
except:
    print("Activate virtual environment and then execute with command: 'python3 4.1non_linear_classification.py'")
    
## or we can use #! /home/harsh/Machine_learning/ML_virtual_env/bin/python at beginning and then execute this file as ./4.1non_linear_classification.py