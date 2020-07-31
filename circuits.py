# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 21:12:31 2020

@author: jheins3
"""
import math
#import cmath

def phasor(real, cmplex):
    magnitude = math.sqrt((real^2) + (cmplex^2))
    angle = math.degrees(math.radians((cmplex/real)))
    return magnitude, angle

def phasorToComplex(magnitude,angle):
    real = magnitude * math.cos(math.radians(angle))
    imaginery = magnitude * math.sin(math.radians(angle))
    return complex(real, imaginery)

def omega(frequency):
    return 2 * math.pi * frequency

def Z_Capacitance(omega, capacitance):
    return (1/(complex(0,1/(omega*capacitance)))).conjugate()

def Z_Inductance(omega, inductance):
    return complex(0,omega*inductance)

if __name__ == '__main__':

    w = omega(60)
    print(Z_Inductance(w, .02))
    print(Z_Capacitance(w, (50*10^-6)))



