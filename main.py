
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import math
from scipy.optimize import curve_fit
#constant
#32/(130.004*100)
#4.3/(17.000*100)
m=4.3/(17.223*100)
s = 1/240
def getData(csv_path):
    #open file
    file_handle = pd.read_csv(str(csv_path)+".csv")
    #gather y data
    y_column_source =file_handle.loc[:,'YM']
    y_pixels = y_column_source.values
    #gather x data
    x_column =file_handle.loc[:,'Slice']
    x_frame = x_column.values 
    #change units
    y_meter = y_pixels*m
    x_sec = x_frame*s
    #substract from initial condition
    y = (y_meter-14*m)
    x= x_sec-28*s
    
 #fit with a second order polnomial 
    z = np.polyfit(x, y, 2)
    g = (z[0]*2)/np.cos(0.21)
    return x,y,z,g
g_list = []
v_li=[]
f_li =[]
for i in range(1,11):
    data =getData("improved/csv/"+str(i))
    g_list.append(data[3])
    v_li.append(data[2][1])
    f_li.append(data[2][2])


std = np.std(g_list, dtype=np.float64)

print(g_list)
print(std)
print(np.mean(g_list))
print(std/(10**(1/2)))
print(v_li)
# g_list_residual = 9.80655-np.array(g_list,float)

# t = np.arange(0,10)
# plt.errorbar(t,g_list_residual,yerr=std,fmt='o')
# plt.axhline(y=0, color='r', linestyle='-')
# plt.xlabel('Initial Velocity(ms^-1)')
# plt.ylabel('g(ms^-2)')
# plt.title('initial velocity vs g')
# # trendpoly = np.poly1d(z) 
# # plt.plot(x,trendpoly(x))
# plt.show()