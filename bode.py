# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 16:36:54 2020

@author: jhein
"""
#import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math
import cmath

FREQUENCY_RANGE = 1000     #change this to max freq in Hz

def V_o(frequency):
    s = complex(0, 2 * math.pi * frequency)
    Hf = 150/(15+(s/10)+1/(s*.00253)); # replace this with your own function
    return Hf


def main (x_axis = FREQUENCY_RANGE, y_axis = V_o(FREQUENCY_RANGE)):

    values = np.arange(1, x_axis+1).tolist()
    y_values = list(map(V_o, values))
    x_values = np.arange(1,1000+1).tolist()

    #frequency response
    ig, ax = plt.subplots()
    ax.plot(x_values, y_values)
    ax.set(xlabel="Frequency (Hz)", ylabel='Voltage (Output)', title= 'Magnitude of Voltage')

    #phase plot
    ih, ay = plt.subplots()
    ay.plot(x_values, list(map(cmath.phase, y_values)))
    ay.set(xlabel="Frequency (Hz)", ylabel='Voltage (Output)', title= 'Phase of Voltage')


if __name__ == '__main__':

    main()


