#coding:utf-8
#!/usr/local/bin/python

import sys
import numpy as np
from pylab import *

lim = 5

def gauss1(x):
    sigma = 1
    return 1/np.sqrt((2*np.pi) * sigma ) * np.exp(- x*x / (2 * sigma * sigma))

def main():
    N = 100

    xx = np.linspace(-lim, lim, N)
    yy = [gauss1(x) for x in xx]

    plot(xx, yy, label="standerd normal distribution")
    legend()
    show()

if __name__ == "__main__":
    main()
