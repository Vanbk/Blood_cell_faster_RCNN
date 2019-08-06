#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 14:14:59 2019

@author: vavan
"""

import xml.etree.ElementTree as ET
import os

A = []
A.append(['image_names', 'cell_type', 'xmin', 'xmax', 'ymin', 'ymax'])

list_of_xml = os.listdir("./BCCD/Annotations/")

for picture_xml in list_of_xml:
       
    tree = ET.parse('./BCCD/Annotations/' + picture_xml)
    root = tree.getroot()
    image_name = root.find('filename').text
    
    for object in root.findall('object'):
        cell_type = object.find('name')
        xmin = object.find('bndbox/xmin').text
        xmax = object.find('bndbox/xmax').text
        ymin = object.find('bndbox/ymin').text
        ymax = object.find('bndbox/ymax').text
        
        A.append([image_name, cell_type.text, int(xmin), int(xmax), int(ymin), int(ymax)])

# generate the data.csv file

import csv

with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(A)