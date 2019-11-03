#coding:utf-8
#!/usr/local/bin/python

"""2次元の多変数寮ガウス分布N(0, I)の確立密度関数"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

[xmin,xmax] = [-4,4]

def gauss2 (x):
    return np.exp (lgauss2(x))

def lgauss2 (x):
    D = len(x)
    return - np.dot(x,x) / 2 - np.log (2 * np.pi) * D / 2

def main(N):
    xx = np.linspace (xmin, xmax, N)
    X,Y = np.meshgrid (xx,xx)
    Z = np.array ([gauss2([x,y]) for x in xx for y in xx]).reshape (N,N)

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
    plt.show()

if __name__ == "__main__":
    main(N=25)
