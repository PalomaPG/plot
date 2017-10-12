# -*- encoding: utf-8 -*-

import numpy as np
import seaborn as sea
from matplotlib import pyplot as plt
import os
from math import log


class Plot:


    def __init__(self, path_results1, path_results2, title, xlabel, ylabel):
        self.path_results1 = path_results1
        self.path_results2 = path_results2
        self.y1= None
        self.y2 = None
        self.x = range(9, 25)
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel

    def plot(self):

        with open(self.path_results1) as f:
            lines = f.readlines()
            #self.x = [line.split()[0] for line in lines]
            self.y1 = [line.split(',')[1] for line in lines]

        with open(self.path_results2) as f:
            lines = f.readlines()
            self.y2 = [float(line.split(',')[1]) for line in lines]


        self.y2= [log(y, 10) for y in self.y2]
        self.y2.sort()
        print(len(self.y1))
        print(len(self.y2))
        print(len(self.x))

        fig = plt.figure()
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.scatter(self.x, self.y2, c="g", alpha=0.5, marker=r'$\clubsuit$',
                    label="Luck")
        plt.show()



