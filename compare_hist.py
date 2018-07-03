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
parser.add_argument('--input1', help='Path to input image 1.')
parser.add_argument('--input2', help='Path to input image 2.')
parser.add_argument('--input3', help='Path to input image 3.')
args = parser.parse_args()

src_base = cv.imread(args.input1)
src_test1 = cv.imread(args.input2)
src_test2 = cv.imread(args.input3)
if src_base is None or src_test1 is None or src_test2 is None:
    print('Could not open or find the images!')
    exit(0)
## [Load three images with different environment settings]
cv.imshow('Detected Person at Frame125',src_base)
cv.imshow('Detected Person at Frame167',src_test1)
cv.imshow('Detected Person at Frame168',src_test2)

cv.waitKey(0)
cv.destroyAllWindows()
## [Convert to HSV]
hsv_base = cv.cvtColor(src_base, cv.COLOR_BGR2HSV)
hsv_test1 = cv.cvtColor(src_test1, cv.COLOR_BGR2HSV)
hsv_test2 = cv.cvtColor(src_test2, cv.COLOR_BGR2HSV)
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
hist_base = cv.calcHist([hsv_base], channels, None, histSize, ranges, accumulate=False)
cv.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

hist_test1 = cv.calcHist([hsv_test1], channels, None, histSize, ranges, accumulate=False)
cv.normalize(hist_test1, hist_test1, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

hist_test2 = cv.calcHist([hsv_test2], channels, None, histSize, ranges, accumulate=False)
cv.normalize(hist_test2, hist_test2, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)
## [Calculate the histograms for the HSV images]

## [Selecting Histogram Comparision Method -Chi SQuare ]
compare_method =1
base_base = cv.compareHist(hist_base, hist_base, compare_method)
base_test1 = cv.compareHist(hist_base, hist_test1, compare_method)
base_test2 = cv.compareHist(hist_base, hist_test2, compare_method)

print('Method: Chi Square ,Base-Base, Base-Test(1), Base-Test(2) :',\
          base_base, '/', base_test1, '/', base_test2)
## [Apply the histogram comparison methods]