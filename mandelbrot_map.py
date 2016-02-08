#!/usr/bin/python

# Plotting a mandelbrot fractal
# This version uses a list to gather the points

import matplotlib.pyplot as plt
import cProfile

def mandelbrot (xOff, yOff, xRange, yRange, xRes, yRes, mxStep):
    iMax = int(xRes * xRange)
    jMax = int(yRes * yRange)
    xVal = []
    for i in range(iMax):
        yVal = []
        for j in range(jMax):
            x0 = float(i) / xRes + xOff
            y0 = float(j) / yRes + yOff
            yVal.append(taxi(x0, y0, mxStep))
        xVal.append(yVal)
    return plt.imshow(xVal)

def taxi (x0, y0, mxStep):
    xOld = x0
    yOld = y0
    iStep = 0
    while (not((xOld*xOld+yOld*yOld>4) or (iStep>mxStep))):
        xNew = xOld*xOld-yOld*yOld+x0
        yNew = 2*xOld*yOld+y0
        xOld = xNew*xNew-yNew*yNew+x0
        yOld = 2*xNew*yNew+y0
        iStep = iStep+2
    return iStep

def mandelbrot_plotter ():
    xOff = -2.0
    yOff = -1.0
    xRange = 3.0
    yRange = 2.0
    xRes = 200
    yRes = 200
    mxStep = 100
    image = mandelbrot (xOff, yOff, xRange, yRange, xRes, yRes, mxStep)
    plt.savefig("mandelbrot_map.png",dpi=300)
    return

mandelbrot_plotter()
