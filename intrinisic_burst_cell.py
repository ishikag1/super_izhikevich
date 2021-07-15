#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 17:18:44 2021

@author: ishikag
"""
import numpy as np
import izhikevich_cells as izh
import matplotlib.pyplot as plt

class ibCell(izh.izhCell):
   def  __init__(self, stimVal):
       super().__init__(stimVal)
       
       self.C = 150
       self.vr = -75
       self.vt = -45
       self.k = 1.2
       self.a = 0.01
       self.b = 5
       self.c = -56
       self.d = 130
       self.vpeak = 50
       self.stimVal = stimVal

def plotMyData(somecell, upLim = 1000):
    tau = somecell.tau
    n = somecell.n
    v = somecell.v
    celltype = somecell.celltype

    # Plot the results
    fig = plt.figure()
    plt.plot(tau*np.arange(0,n),v[0,:].transpose(), 'k-')
    plt.xlabel('Time Step')
    plt.xlim([0, upLim])
    plt.ylabel(celltype + ' Cell Response')
    plt.show()

def createCell():
    myCell = ibCell(stimVal=4000)        
    myCell.simulate()
    plotMyData(myCell)

if __name__=='__main__':
    createCell()

       
       
       