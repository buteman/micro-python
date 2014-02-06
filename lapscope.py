#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider, RadioButtons
import sys
import time

with open('./rdata.txt') as f:
    for i, l in enumerate(f):
        pass
i+=1

fig, ax = plt.subplots(figsize=(17, 10))
plt.hold(False)
plt.subplots_adjust(bottom=0.25, top= 0.90)
plt.autoscale (enable=False, axis='x') 
#axcolor = 'lightblue'
axcolor = 'lightgrey'
#axcolor = 'lightgoldenrodyellow'
#axcolor = 'white'
ax.set_ylabel('Voltage')
ax.set_title('Micropython Scope')
def endit(mock):
    sys.exit() 

def update(val):
    howmany = int(axvals.val)

def writefile(dummy):
    total = int(round(axvals2.val))
    print("hello" + str(total))# this is just a test to make sure function is called by my code
    # this will need to be programmed
    # to write the number of seconds to sample
    # to the SD card on the micropython (MP) board.
    # then some part of the program needs to wait for the
    #samples to be taken and written to another file on the SD card.
    # MP will read the command file and delete it then 
    # it will write the file and then write a small dummy file to signify
    # that all the data has been written.
    # The program, after it has waited say 1 second longer than the sample time
    # will read the data and do the plot.

def static_plot(dummy):
    ydata =  []
    ymax = 0
#    ax1 = plt.axes ()
    myfile = open("rdata.txt", "r")
    for myline in myfile:
        q = myline
        ydata.append(q)  
        if int(q) > ymax:
            ymax = int(q)
            print (q, '  ', ymax)
    file.close(myfile)
    fst = int(round(ax1st.val))
    lst = int(round(axvals.val)) + fst
    ax1 = plt.axes()
    if (lst >= i - 1):
        lst = i 
    plt.axis([fst, lst, 0, ymax])
    line, =  plt.plot (ydata[fst:lst + 1])
    plt.draw()


def plotit(dummy):
    howmany = int(axvals.val)
    wait_time = (int(axvals1.val))
    top = i
    plt.ion() # set plot to animated
    xdata = []
    c = 0
    for a in range(0,top):
        xdata.append(a)
        c+=1

    ydata =  []
    ax1 = plt.axes ()  

    myfile = open("rdata.txt", "r")
    for myline in myfile:
        q = myline
        ydata.append(q)  
    file.close(myfile)
    c = 0
# Make plot
    line, =  plt.plot (ydata[0:howmany])
    for p in range(0, top ):
        del  ydata [ 0 ]
        line.set_xdata (np.arange ( len (ydata)))
        line.set_ydata (ydata)   # update the data
        plt.draw () # update the plot
        op='Plotting ' + str((int(p/10))*10)
#        ax.set_title(op)	
        time.sleep(wait_time)


axvals = plt.axes([0.36, 0.10, 0.30, 0.025], axisbg=axcolor)
axvals = Slider(axvals, 'Points to\n display', 1, i, valfmt='%1.0f', facecolor='lightgreen')
axvals1 = plt.axes([0.36, 0.05, 0.30, 0.025], axisbg=axcolor)
axvals1 = Slider(axvals1, 'Pause', 0, 1.0, valfmt='%1.2f', facecolor='lightgreen')
axvals2 = plt.axes([0.08, 0.15, 0.20, 0.025], axisbg=axcolor)
axvals2 = Slider(axvals2, 'Seconds\n to Record', 0.0, 60, valfmt='%1.0f', facecolor='lightgreen')
ax1st = plt.axes([0.36, 0.15, 0.30, 0.025], axisbg=axcolor)
ax1st = Slider(ax1st, '1st Point\nto display', 1, i, valfmt='%1.0f', facecolor='lightgreen')

axplot = plt.axes([0.74, 0.05, 0.07, 0.075])
aplot = Button(axplot, 'Dynamic\nPlot')
aplot.on_clicked(plotit)

axstat = plt.axes([0.82, 0.05, 0.07, 0.075])
astat = Button(axstat, 'Static\nPlot')
astat.on_clicked(static_plot)

axout = plt.axes([0.90, 0.05, 0.07, 0.075])
aout = Button(axout, 'Exit')
aout.on_clicked(endit)

axnum = plt.axes([0.13, 0.05, 0.07, 0.075])
anum = Button(axnum, 'Start\nmeasuring')
anum.on_clicked(writefile)


plt.show()


