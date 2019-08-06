#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 17:00:01 2019

@author: vavan
"""

# importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import patches

# read the csv file using read_csv function of pandas
train = pd.read_csv("BCCD_Dataset/data.csv")
train.head()

#image = train.loc[0:5,'image_names':'xmax']

image_file = train.at[20, 'image_names']

# plot the image 

fig = plt.figure()
#add axes to the image
ax = fig.add_axes([0,0,1,1])
# read and plot the image
image = plt.imread('BCCD_Dataset/BCCD/JPEGImages/' + image_file)
plt.imshow(image)

# iterating over the image for different objects

objects = train.loc[train.image_names == image_file, :]

total_of_row = objects.shape[0] # number of row

for i in range(total_of_row):
    row = objects.iloc[i]
    xmin = row.xmin
    xmax = row.xmax
    ymin = row.ymin
    ymax = row.ymax
    
    width = xmax - xmin
    height = ymax - ymin
    
    # assign different color to different classes of objects
    if row.cell_type == 'RBC':
        edgecolor = 'r'
        ax.annotate('RBC', xy=(xmax-40,ymin+20))
    elif row.cell_type == 'WBC':
        edgecolor = 'b'
        ax.annotate('WBC', xy=(xmax-40,ymin+20))
    elif row.cell_type == 'Platelets':
        edgecolor = 'g'
        ax.annotate('Platelets', xy=(xmax-40,ymin+20))
        
    # add bounding boxes to the image
    rect = patches.Rectangle((xmin,ymin), width, height, edgecolor = edgecolor, facecolor = 'none')
    
    ax.add_patch(rect)
