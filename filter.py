# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 20:58:18 2020

@author: jhein3
"""

import circuits
import math


def low_pass(R, C, wc, plot = True):
    """
    Function for calculating a low pass filter. And optionally, can plot the
    response.

    Parameters
    ----------
    R : Float
        Resistance, 0 if you want to solve for a resistance value
    C : Float
        Capacitance, 0 if you want to solve for a Capacitance Value
    wc : Cut-off Frequency
        Frequency at which Gv = 1/sqrt(2), 0 if you want to solve for Cut-off Frequency
    plot : Boolean, optional
        Plots the Gv, Magnitude, and Phase shift. The default is True.

    Returns
    -------
    Gv : Float
        Voltage Gain
    Magnitude : Float
        Magnitude
    phi : Float
        Phase Shift
    """


    if R and C and wc != 0:
        w = circuits.omega(wc)
        tau = R * C
        Gv = 1 / (complex(1, w * tau))
        Magnitude = 1 /(math.sqrt(complex(1, w * tau)**2))
        phi = -math.atan(w * tau)

        if plot == True:
            plot()


    elif C == 0 and R != 0 and wc != 0:

        if plot == True:
            low_pass(R,C, wc,) #recursively calls low pass with solved R/C values to plot response.

        return C


    elif R == 0 and C != 0 and wc != 0:

        low_pass(R,C, wc,)
        pass

    elif wc == 0 and R != 0 and C != 0:

        low_pass(R,C, wc,)
        pass

    else:
        print('You did not use your brain, RTFM')
        quit()

    if plot == True:
        plot()

    return Gv, Magnitude, phi

def high_pass(R, C, plot = True):

    tau = R * C

    if plot == True:
        plot()
    return

def band_pass(R, C, plot = True):

    tau = R * C

    if plot == True:
        plot()
    return

def band_rejection(R, C, plot = True):

    if plot == True:
        plot()
    return

def plot(x_range, y_range):

    if plot == True:
        plot()
    return

if __name__ == "__main__":
    print('I may be gay')