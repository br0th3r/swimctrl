#!/usr/bin/env python
#########################################################################
#                                                                       #
# Name:      MAIN                                                       #
#                                                                       #
# Project:   SWIMMINGPOOL CONTROL (SWIMCTRL)                            #
# Module:    Main                                                       #
# Started:   2014061400                                                 #
#                                                                       #
# Important: WHEN EDITING THIS FILE, USE SPACES TO INDENT - NOT TABS!   #
#                                                                       #
#########################################################################
#                                                                       #
# Juan Miguel Taboada Godoy <juanmi@centrologic.com>                    #
#                                                                       #
# This file is part of SWIMCTRL                                         #
#                                                                       #
# SWIMCTRL is free software: you can redistribute it and/or modify      #
# it under the terms of the GNU General Public License as published by  #
# the Free Software Foundation, either version 2 of the License, or     #
# (at your option) any later version.                                   #
#                                                                       #
# SWIMCTRL is distributed in the hope that it will be useful,           #
# but WITHOUT ANY WARRANTY; without even the implied warranty of        #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
# GNU General Public License for more details.                          #
# You should have received a copy of the GNU General Public License     #
# along with SWIMCTRL.  If not, see <http://www.gnu.org/licenses/>.     #
#                                                                       #
#########################################################################
'''
Program to control little SWIMMINGPOOLS chemical products and water quality
'''

__version__ = "2015062000"

__all__ = []

import sys
import datetime

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Our swimmingpool
vol=1.25            # Water volumen, m3 of water
copper_sulfate=3     # 3 grams/m3 each month
flocculant=1        # 3 grams/m3 each month
chlorine=10            # 10 grams/m3 of water to increase 1 point
chlorine_day=4         # 3-5 grams/m3 of water every day
ph_minus=(10,0.2)   # 2 caps/m3 to lower it 4 decimals, 1 cap is 10 grams, 10 grams each decimal
ph_plus=(10,0.4)     # 1 cap/m3 to increase 4 decimals, 1 cap is 10 grams, 10 grams each decimal

# Contants
bar_distance=30
bar_width=0.02
clmin=1
clmax=3
phmin=7.2
phmax=7.6
tacmin=80
tacmax=120

def help():
    name=sys.argv[0]
    print
    print "Usage:"
    print "    {0} register <CL> <PH> <TAC> ['yyyy-mm-dd hh:mm:ss']                         Register details (date is optional)".format(name)
    print "    {0} products <CL> <PH-> <PH+> <SULFATE> <FLOCCULANT> ['yyyy-mm-dd hh:mm:ss'] Register details (date is optional)".format(name)
    print "    {0} bath <people> ['yyyy-mm-dd hh:mm:ss']                                    Register details (date is optional)".format(name)
    print "    {0} show                                                                     Show the graph".format(name)
    print "    {0} actions                                                                  Recommend actions to take care".format(name)
    sys.exit(1)

def arg(num):
    try:
        result=sys.argv[num]
    except:
        result=None
    return result

action=arg(1)
cl=arg(2)
ph=arg(3)
tac=arg(4)
d=arg(5)

p_cl=arg(2)
p_ph_minus=arg(3)
p_ph_plus=arg(4)
p_sulfato=arg(5)
p_flocculant=arg(6)
p_d=arg(7)

b_people=arg(2)
b_d=arg(3)

if action=='register':
    # Stabilize variables
    try:
        cl=float(cl)
    except:
        cl=None
    try:
        ph=float(ph)
    except:
        ph=None
    try:
        tac=float(tac)
    except:
        tac=None
    if d:
        try:
            (a,b)=d.split(" ")
            (x,y,z)=a.split("/")
            (x,y,z)=b.split(":")
        except:
            d=None
    else:
        d=str(datetime.datetime.now()).split(".")[0]
    
    # Process data
    if (cl is not None) and (ph is not None) and (tac is not None) and (d is not None):
        data=open('swimmingpool.dat','a')
        data.write("S\t{0}\t{1}\t{2}\t{3}\n".format(d,cl,ph,tac))
        data.close()
    else:
        if cl  is None: print "Missing CL: {0}".format(cl)
        if ph  is None: print "Missing PH: {0}".format(ph)
        if tac is None: print "Missing TAC: {0}".format(tac)
        if d  is None: print "Wrong DATE: {0}".format(d)
        help()
    
elif action=='bath':
    # Stabilize variables
    try:
        people=int(b_people)
    except:
        people=None
    if b_d:
        try:
            (a,b)=b_d.split(" ")
            (x,y,z)=a.split("/")
            (x,y,z)=b.split(":")
            d=b_d
        except:
            d=None
    else:
        d=str(datetime.datetime.now()).split(".")[0]
    
    # Process data
    if (people is not None) and (d is not None):
        data=open('swimmingpool.dat','a')
        data.write("B\t{0}\t{1}\n".format(d,people))
        data.close()
    else:
        if people  is None: print "Missing People: {0}".format(people)
        if d  is None: print "Wrong DATE: {0}".format(d)
        help()

elif action=='products':
    # Stabilize variables
    try:
        cl=float(p_cl)
    except:
        cl=None
    
    if cl and (len(sys.argv)==3):
        ph_minus=0.0
        ph_plus=0.0
        sulfato=0.0
        flocculant=0.0
        d=None
    else:
        try:
            ph_minus=float(p_ph_minus)
        except:
            ph_minus=None
        try:
            ph_plus=float(p_ph_plus)
        except:
            ph_plus=None
        try:
            sulfato=float(p_sulfato)
        except:
            sulfato=None
        try:
            flocculant=float(p_flocculant)
        except:
            flocculant=None
        try:
            d=float(p_d)
        except:
            d=None
    
    if d:
        try:
            (a,b)=d.split(" ")
            (x,y,z)=a.split("/")
            (x,y,z)=b.split(":")
        except:
            d=None
    else:
        d=str(datetime.datetime.now()).split(".")[0]
    
    # Process data
    if (cl is not None) and (ph_minus is not None) and (ph_plus is not None) and (sulfato is not None) and (flocculant is not None) and (d is not None):
        data=open('swimmingpool.dat','a')
        data.write("P\t{0}\t{1}\t{2}\t{3}\t{4}\t{5}\n".format(d,cl,ph_minus,ph_plus,sulfato,flocculant))
        data.close()
    else:
        if cl  is None:         print "Missing CL: {0}".format(cl)
        if ph_minus  is None:   print "Missing PH-: {0}".format(ph_minus)
        if ph_plus  is None:     print "Missing PH+: {0}".format(ph_plus)
        if sulfato is None:     print "Missing SULFATO: {0}".format(sulfato)
        if flocculant is None:  print "Missing FLOCULANTE: {0}".format(flocculant)
        if d  is None:          print "Wrong DATE: {0}".format(d)
        help()

elif action=='show':
    # Read file
    alldates=[]
    dates=[]
    cls=[]
    phs=[]
    tacs=[]
    pcl=[]
    pdates=[]
    phs_mas=[]
    phs_menos=[]
    psulfato=[]
    pflocculant=[]
    datemin=None
    f=open("swimmingpool.dat",'r')
    for line in f.readlines():
        linesp=line.split("\t")
        kind=linesp[0]
        datestring=linesp[1]
        date = datetime.datetime.strptime(datestring, '%Y-%m-%d %H:%M:%S')
        alldates.append(date)
        
        if kind=='S':
            (kind,datestring,cl,ph,tac)=line.split("\t")
            dates.append(date)
            cls.append(float(cl))
            phs.append(float(ph))
            tacs.append(float(tac))
        elif kind=='P':
            (kind,datestring,cl,ph_minus,ph_plus,sulfato,flocculant)=line.split("\t")
            pdates.append(date)
            pcl.append(float(cl))
            phs_mas.append(float(ph_plus))
            phs_menos.append(float(ph_minus))
            psulfato.append(float(sulfato))
            pflocculant.append(float(flocculant))
            
    f.close()
    alldates.append(date+datetime.timedelta(days=1))
    datemin=alldates[0]
    datemax=alldates[-1]
    
    # Preare locators
    months    = mdates.MonthLocator()           # Every month
    monthsFmt = mdates.DateFormatter('%m')      # Month
    days      = mdates.DayLocator()             # Every day
    daysFmt   = mdates.DateFormatter('%d/%m %H:%M')   # Day
    
    fig = plt.figure()
    le=len(alldates)
    
    views=[]
    views.append((411,dates,[ \
            (dates,cls, 'bo-',0), \
            (alldates,[clmin] *le, 'r-',1), \
            (alldates,[clmax] *le, 'r-',2) \
            ], 'Cloro', 0,   5))
    views.append((412,dates,[ \
            (dates,phs, 'go-',0), \
            (alldates,[phmin] *le, 'r-',1), \
            (alldates,[phmax] *le, 'r-',2) \
            ], 'PH', 6.5, 8))
    views.append((413,dates,[ \
            (dates,tacs,'yo-',0), \
            (alldates,[tacmin]*le, 'r-',1), \
            (alldates,[tacmax]*le, 'r-',2) \
            ], 'TAC', 40, 180))
    views.append((414,dates,[ \
            (pdates,pcl, ('Cloro','m'),3), \
            (pdates,phs_menos, ('ph-','g'),3), \
            (pdates,phs_mas, ('ph+','r'),3), \
            (pdates,psulfato, ('sulfato','c'),3), \
            (pdates,pflocculant, ('flocculant','b'),3), \
            ], 'Products', 0, 60))

    for (view, x, ys, ylabel, miny, maxy) in views:
        ax = fig.add_subplot(view)
        bar_offset=0
        for (xdata,ydata,yline,kind) in ys:
            if kind==1:
                ax.fill([xdata[0]]+xdata+[xdata[-1]], [miny]+ydata+[miny], yline, alpha=0.1)
            elif kind==2:
                ax.fill([xdata[0]]+xdata+[xdata[-1]], [maxy]+ydata+[maxy], yline, alpha=0.1)
            elif kind==3:
                (text,bgcolor)=yline
                newxdata=map(lambda x: x+datetime.timedelta(minutes=bar_distance*bar_offset),xdata)
                ax.bar(newxdata, ydata, [bar_width]*len(xdata),color=bgcolor,edgecolor='k', alpha=0.4, label=text)
                # Add legend
                ax.legend(loc=2, ncol=5, prop={'size':10})

#                for x in newxdata:
#                    ax.text(x+datetime.timedelta(minutes=4), -2, text, horizontalalignment='center', verticalalignment='top', color='k', rotation=90)
                bar_offset+=1
            else:
                # Normal plot
                ax.plot(xdata, ydata, yline)
        
        # Add label on y
        plt.ylabel(ylabel)
        
        # Format the ticks
        ax.xaxis.set_major_locator(days)
        ax.xaxis.set_major_formatter(daysFmt)
        ax.xaxis.set_minor_locator(days)
        ax.xaxis.set_major_formatter(daysFmt)
        
        # Set limits
        ax.set_xlim(datemin, datemax)
        ax.set_ylim(miny, maxy)
        
        # Format dates
        ax.format_xdata = mdates.DateFormatter('%d/%m/%Y')
        
        # Add a grid
        ax.grid(True)
    
    # Rotates and right aligns the x labels, and moves the bottom of the axes up to make room for them
    fig.autofmt_xdate()
    plt.xticks(rotation=60)
    
    # Reduce margins
    plt.subplots_adjust(left=0.05, right=0.95, top=0.98, bottom=0.15)
    
    # Plot everything
    plt.show()

elif action=='actions':
    # Read data
    dates=[]
    cls=[]
    phs=[]
    tacs=[]
    datemin=None
    f=open("swimmingpool.dat",'r')
    for line in f.readlines():
        linesp=line.split("\t")
        if linesp[0]=='S':
            (kind,datestring,cl,ph,tac)=line.split("\t")
            date = datetime.datetime.strptime(datestring, '%Y-%m-%d %H:%M:%S')
            if datemin is None:
                datemin = date
            datemax = date
            dates.append(date)
            cls.append(float(cl))
            phs.append(float(ph))
            tacs.append(float(tac))
    f.close()
    
    # Get last values
    lastcl=cls[-1]
    lastph=phs[-1]
    lasttac=tacs[-1]
    
    # Analize chlorine
    print "CHLORINE: {0}".format(lastcl),
    if lastcl<=clmin:
        print "OK for a bath but add {0} grams of chlorine".format(chlorine*vol*(clmax-lastcl))
    elif lastcl>clmax:
        print "Don't get a bath, chlorine is too high!"
    else:
        print "OK"
    
    # Analize PH
    print "PH: {0}".format(lastph),
    if lastph>phmax:
        print "Don't get a bath, add {0} grams PH reductor".format(ph_minus[0]*vol*(lastph-phmin)/ph_minus[1])
    elif lastph<phmin:
        print "Don't get a bath, add {0} grams PH aumentador".format(ph_plus[0]*vol*(phmax-lastph)/ph_plus[1])
    elif lastph==phmax:
        print "OK for a bath, add {0} grams PH reductor".format(ph_minus[0]*vol*(lastph-phmin)/ph_minus[1])
    else:
        print "OK"
    
    # Analize TAC
    print "TAC: {0}ppm".format(lasttac),
    if lasttac>tacmax:
        print "your TAC is high"
    elif lasttac<tacmin:
        print "your TAC is low"
    else:
        print "OK"
    
    # Remember
    print
    print "Remember:"
    print "- Add {0} grams of 'copper sulfate' once a month".format(copper_sulfate*vol)
    print "- Add {0} ml of 'flocculant' once a week and make purificator work for 8 hours".format(flocculant*vol)
    print "- Add {0} grams of 'chlorine' per day".format(chlorine_day*vol)
    print "- If TAC is high, means your products will have less effect, you will need to increse the quantities"
    print
    print "!!!!!!!!!!!!!!!!!!!!!!!!! IMPORTANT !!!!!!!!!!!!!!!!!!!!!!!!"
    print "Do not get a bath after adding the products, always add the"
    print "chemical products at the end of the they (when nobody is"
    print "going to get a bath anymore until the next day"
    print "!!!!!!!!!!!!!!!!!!!!!!!!! IMPORTANT !!!!!!!!!!!!!!!!!!!!!!!!"

else:
    help()
