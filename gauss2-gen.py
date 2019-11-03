#coding:utf-8
#!/usr/local/bin/python

"""相関を持つ２次元のガウス分布からのサンプルの生成"""

import matplotlib.pyplot as plt
import numpy as np

N = 250

def gauss2(L):
    return np.dot(L, np.random.randn(2))

def main():
    # S = np.array([[1,0.9],[0.9,1]])
    S = np.array([[1,-0.7],[-0.7,1]])
    # S = np.array([[1,0],[0,1]])

    L = np.linalg.cholesky(S)
    X = np.array([gauss2(L) for n in range(N)])

    plt.plot(X.T[0], X.T[1], 'ob', markersize=6)
    plt.show()

if __name__ == "__main__":
    main()
