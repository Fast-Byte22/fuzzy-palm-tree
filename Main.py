import os
import threading as th
import json
import urllib.request
from ast import literal_eval

# import tensorflow as tf
# import pathlib

# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np

#np.set_printoptions(precision=4)


# eur/czk 74450 

contents =  urllib.request.urlopen("https://freeserv.dukascopy.com/2.0/?path=api/historicalPrices&key=dae9gsyrj4000000&instrument=74450&timeFrame=tick&count=5000")
contentsJ = json.loads(contents.read().decode('utf-8'))
tList = []
Abid, Aask, tot, Hbid, Lbid, Hask, Lask = 0 , 0 ,0 , 0, contentsJ['ticks'][0].get('bid'), 0,  contentsJ['ticks'][0].get('ask')
for x in contentsJ['ticks']:
    bid = x.get('bid')
    ask = x.get('ask')
    print('bid - ' + str(bid)+ ': ask - ' + str(ask))
    Abid +=  bid
    Aask += ask
    tot += 1
    if Hbid < bid:
        Hbid = bid
    if Lbid > bid:
        Lbid = bid
    if Hask < ask:
        Hask = ask
    if Lask > ask:
        Lask = ask

print('--- avg. bid - '+ str(Abid/tot) + ' -- avg. ask - ' + str( Aask/tot) +' ---' )
print('--- hig. bid - '+ str(Hbid) +     ' -- low bid - '  + str( Lbid) +' ---'     )
print('--- hig. ask - '+ str(Hask) +     ' -- low ask - '  + str( Lask) +' ---'     )
print('--- ticks - ' + str(tot)+ ' ---' )

input('press enter to exit')