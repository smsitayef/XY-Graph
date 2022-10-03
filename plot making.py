

import os
import pandas as pd
from matplotlib import pyplot as plt


#set working directory and read data

path = '/Users/user/Desktop'
os.chdir(path)
a = pd.read_csv('Ogallaladata.csv')

# extract WD and DWT

WD = a.WellDepth
DWT = a.DWT

plt.plot(WD, DWT,'ro') #ro for red

plt.xlabel('Well Depth, ft')
plt.ylabel('Depth of Water table(ft)')
plt.grid() #a grid for aesthetics
plt.title('Wall Depth to water table relationship')
plt.legend(['DWT'],loc='upper left')
plt.show()
