#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 20:10:20 2019

@author: vavan
"""

# importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import patches

# read the csv file using read_csv function of pandas
train = pd.read_csv('train.csv')

data = pd.DataFrame()

xmin = train['xmin']

# create data as format : filepath,x1,y1,x2,y2,class_name

data['format'] = 'BCD_VAN/images/' + train['image_names']

for i in range(data.shape[0]):
    data['format'][i] =  data['format'][i] + ',' + str(train['xmin'][i]) + ',' + str(train['ymin'][i]) + ',' + str(train['xmax'][i]) + ',' + str(train['ymax'][i])

data['format'] =  data['format'] + ',' + train['cell_type']

data.to_csv('annotate.txt', header=None, index=None, sep=' ')