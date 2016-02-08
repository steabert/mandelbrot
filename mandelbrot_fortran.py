#!/usr/bin/python

# Plotting a mandelbrot fractal
# This version uses a fortran subroutine to fill in the points

import numpy
import matplotlib.pyplot as plt
import mandelbrot

def mandelbrot_plot ():
    # input values
    xOff = -2.0
    yOff = -1.0
    xRange = 3.0
    yRange = 2.0
    Res = 1000
    mxStep = 100
    # create matrix
    iMax = int(Res * xRange)
    jMax = int(Res * yRange)
    fMatrix = numpy.empty((jMax,iMax),order='F',dtype=numpy.int32)
    mandelbrot.mandelbrot(xOff, yOff, xRange, yRange, Res, mxStep, fMatrix)
    # plot the image matrix
    plt.imshow(fMatrix.transpose())
    plt.savefig("mandelbrot_fortran.png",dpi=300)
    return

mandelbrot_plot()
