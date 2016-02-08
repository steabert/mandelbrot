#!/usr/bin/python

# Plotting a mandelbrot fractal
# This version separates the image parameters

import numpy
import matplotlib.pyplot as plt
import cProfile

def mandelbrot_image (xOff, yOff, xRange, yRange, xRes, yRes, mxStep):
    iMax = int(xRes * xRange)
    jMax = int(yRes * yRange)
    fMatrix = numpy.empty((iMax,jMax),dtype=numpy.int8)
    for i in range(iMax):
        for j in range(jMax):
            iStep = 0
            x0 = float(i) / xRes + xOff
            y0 = float(j) / yRes + yOff
            xOld = x0
            yOld = y0
            while (not((xOld*xOld+yOld*yOld>4) or (iStep>mxStep))):
                xNew = xOld*xOld-yOld*yOld+x0
                yNew = 2*xOld*yOld+y0
                xOld = xNew*xNew-yNew*yNew+x0
                yOld = 2*xNew*yNew+y0
                iStep = iStep+2
            fMatrix[i,j] = iStep
    return plt.imshow(fMatrix)

def mandelbrot ():
    xOff = -2.0
    yOff = -1.0
    xRange = 3.0
    yRange = 2.0
    xRes = 200
    yRes = 200
    mxStep = 100
    image = mandelbrot_image (xOff, yOff, xRange, yRange, xRes, yRes, mxStep)
    plt.savefig("mandelbrot_numpy.png", dpi=300)
    return

mandelbrot()
#cProfile.run('mandelbrot()')
