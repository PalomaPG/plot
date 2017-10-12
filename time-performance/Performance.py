# -*- encoding: utf-8 -*-

import numpy as np
import statistics as st
import os

class Performance:

    def __init__(self, path, prefix):
        self.path = path
        self.data = None
        self.prefix = prefix
        self.output_path = path+"o"+prefix+".txt"


    def readAndCalc(self, filename):

        with open(self.path+filename,'r') as infile:
            self.data = np.genfromtxt(infile, dtype=float)

        with open(self.output_path, 'a') as out:
            out.write( "%d,%f,%f\n" %(len(self.data), st.mean(self.data), st.stdev(self.data)))


    def writeAllFiles(self):

        for file in os.listdir(self.path):
            if file.startswith(self.prefix):
                self.readAndCalc(file)

