# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 11:25:45 2018

@author: Alan , IIIT Bh
"""

from __future__ import print_function
from __future__ import division
from matplotlib import pyplot as plt
import cv2 as cv
import numpy as np
import argparse

## [Load three images with different environment settings]
parser = argparse.ArgumentParser(description='Code for Histogram Comparison using Chi Square Method')
parser.add_argument('--img1', help='Path to input image 1.')
parser.add_argument('--img2', help='Path to input image 2.')
parser.add_argument('--img3', help='Path to input image 3.')
parser.add_argument('--img4', help='Path to input image 3.')
parser.add_argument('--img5', help='Path to input image 3.')
args = parser.parse_args()

frame1 = cv.imread(args.img1)
frame2 = cv.imread(args.img2)
frame3 = cv.imread(args.img3)
frame4 = cv.imread(args.img4)
frame5 = cv.imread(args.img5)
if frame1 is None or frame2 is None or frame3 is None or frame4 is None or frame5 is None :
    print('Could not open or find the images!')
    exit(0)
## [Load the images with different environment settings]
cv.imshow('Frame1',frame1)
cv.imshow('Frame2',frame2)
cv.imshow('Frame3',frame3)
cv.imshow('Frame4',frame4)
cv.imshow('Frame5',frame5)

cv.waitKey(0)
cv.destroyAllWindows()
## [Convert to HSV]
hsv_f1 = cv.cvtColor(frame1, cv.COLOR_BGR2HSV)
hsv_f2 = cv.cvtColor(frame2, cv.COLOR_BGR2HSV)
hsv_f3 = cv.cvtColor(frame3, cv.COLOR_BGR2HSV)
hsv_f4 = cv.cvtColor(frame4, cv.COLOR_BGR2HSV)
hsv_f5 = cv.cvtColor(frame5, cv.COLOR_BGR2HSV)
## [Convert to HSV]

#hist = cv.calcHist([hsv_base], [0, 1], None, [180, 256], [0, 180, 0, 256])
## [Using 50 bins for hue and 60 for saturation]
h_bins = 50
s_bins = 60
histSize = [h_bins, s_bins]

# hue varies from 0 to 179, saturation from 0 to 255
h_ranges = [0, 180]
s_ranges = [0, 256]
ranges = h_ranges + s_ranges # concat lists

# Use the 0-th and 1-st channels
channels = [0, 1]
## [Using 50 bins for hue and 60 for saturation]

## [Calculate the histograms for the HSV images]
h1 = cv.calcHist([hsv_f1], channels, None, histSize, ranges, accumulate=False)
cv.normalize(h1, h1, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

h2 = cv.calcHist([hsv_f2], channels, None, histSize, ranges, accumulate=False)
cv.normalize(h2, h2, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

h3 = cv.calcHist([hsv_f3], channels, None, histSize, ranges, accumulate=False)
cv.normalize(h3, h3, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

h4 = cv.calcHist([hsv_f4], channels, None, histSize, ranges, accumulate=False)
cv.normalize(h4, h4, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

h5 = cv.calcHist([hsv_f5], channels, None, histSize, ranges, accumulate=False)
cv.normalize(h5, h5, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)
## [Calculate the histograms for the HSV images]

# List of Normalized Color Histograms
Normalized_Hist=[h1,h2,h3,h4,h5]
## [Selecting Histogram Comparision Method -Chi SQuare ]
compare_method =1

print('Chi Square Values on Comparing between 2  Normalized Color Histogram')

for hist in Normalized_Hist:
    for histo  in Normalized_Hist:
        Frame1_Frame2 = cv.compareHist(hist, histo, compare_method)
        print(Frame1_Frame2)
    print('\n')

## [Apply the histogram comparison methods]