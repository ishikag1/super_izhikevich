#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 18:03:09 2021

@author: ishikag
"""

import numpy as np
import izhikevich_cells as izh
import matplotlib.pyplot as plt

class cCell(izh.izhCell):
   def  __init__(self, stimVal):
       super().__init__(stimVal)
       
       self.C = 50
       self.vr = -60
       self.vt = -40
       self.k = 1.5
       self.a = 0.03
       self.b = 1
       self.c = -40
       self.d = 150
       self.vpeak = 25
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
    myCell = cCell(stimVal=4000)        
    myCell.simulate()
    plotMyData(myCell)

if __name__=='__main__':
    createCell()