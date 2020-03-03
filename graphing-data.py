#!/usr/bin/env python
# coding: utf-8
'''
Name: Gargeya Vunnava
GitHub: gargeyavunnava
Date created: 2/28/2020
The following code represents the data given to us in the assignment graphically (selected columns only)
The code takes two arguments from command line. The first argumnet is the input filename of the file containing the data 
and the second argument is the desired output pdf filename 

'''

#import numpy to work with arrays
import numpy as np

#import plplot from matplotlib to plot graphs
import matplotlib.pyplot as plt

#import gridspec from matplotlib to organize subplots spacing and size
import matplotlib.gridspec as gridspec

#import sys module for using command line arguments
import sys

# sys.argv[i] contains file name when i=0 and input arguments for i>0
file_in = sys.argv[1] #input filename as 1st argument
file_out = sys.argv[2] #output filename as 2nd argument

# reading data from input txt file as arrays using genfromtext
data = np.genfromtxt(file_in, delimiter = '\t',skip_header=1, names= ['Year','Mean','Max','Min','StdDev','Tqmean','RBindex'],dtype=['int','float','float64','float64','float','float','float'])

#storing required array as list to make it easier to call them in plot functions
x= data['Year']
y= [data['Mean'],data['Max'],data['Min'],data['Tqmean'],data['RBindex']]

# set up overall plot
fig = plt.figure(1)
# set up subplot grid
gridspec.GridSpec(8,1)


#specifying position and size for Streamflow subplot
plt.subplot2grid((8,1),(0,0), rowspan=2)
#specifying x and y values for the plots along with color of the line and labels
plt.plot(x,y[0],color='black',label='Mean')
plt.plot(x,y[1],color='red',label='Max')
plt.plot(x,y[2],color='blue',label='Min')
plt.legend(['Mean','Max','Min'])
plt.xlabel('Year')
plt.ylabel('Streamflow (cfs)')
#specifying plot title
plt.title('Mean, maximum and minimum daily streamflow')

#specifying position and size for Tqmean subplot
plt.subplot2grid((8,1),(3,0), rowspan=2)
#specifying x and y values (multiplied by 100) for the plots along with symbols style (green diamonds) and labels
plt.plot(x,y[3]*100,'dg')
plt.xlabel('Year')
plt.ylabel('Tqmean (%)')
#specifying plot title
plt.title('Tqmean, multiplied by 100%')

#specifying position and size for R-B index subplot
plt.subplot2grid((8,1),(6,0), rowspan=3)
#creating a bar plot with labels
plt.bar(x,y[4])
plt.xlabel('Year')
plt.ylabel('R-B Index (ratio)')
#specifying plot title
plt.title('Bar plot of R-B index')

#setting the overall figure size
fig.set_size_inches(w=10,h=15)
#reading the second input argument from command line and using that to output pdf file name
fig.savefig(file_out+'.pdf')





