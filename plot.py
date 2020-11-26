
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import math
#constant
M= 4.3/(17.223*100)
S = 1/240

def getData(csv_path):
    #open file
    file_handle = pd.read_csv(csv_path+".csv")
    #gather y data
    y_column_source =file_handle.loc[:,'YM']
    y_pixels = y_column_source.values
    #gather x data 
    x_column =file_handle.loc[:,'Slice']
    x_frame = x_column.values 
    #change units
    y_meter = y_pixels*M
    x_sec = x_frame*S
    #substract from initial condition
    y = (y_meter-14*M)
    x= x_sec-28*S
    
    plt.plot(x,y,'ok',label = "Data Points")
    z = np.polyfit(x, y, 2,full=True)
    trendpoly = np.poly1d(z[0]) 
    print(trendpoly)
    print(2*z[0][0]/np.cos(0.21))
  
    plt.plot(x,trendpoly(x),'r',label ="Second Order Polynomial fit")
    plt.xlabel('Time(second)')
    plt.ylabel('y-position(meter)')
    plt.title('y-position v/s time for a free falling beer pong')
    plt.legend()
    plt.show()
    
    #residuals
    # residuals =[]
    # rao =[]
    # rbo =[]
    # rto =[]
    # for x_o,y_o in zip(x,y):

    #     y_c = 4.848*(x_o**2)+0.7369*x_o
    #     r = y_o - y_c
    #     residuals.append(r)
    #     if r > 0 :
    #         rao.append(r)
    #     elif r < 0 :
    #         rbo.append(r)
    #     elif r == 0:
    #         rto.append(r)
    # print(len(rao))
    # print(len(rbo))
    # print(len(rto))
    # plt.axhline(y = 0, color ="black", linestyle ="-") 
    # plt.plot(x,residuals,'ok')
    # plt.grid(True)
    # plt.xlabel('Time(t)')
    # plt.ylabel('Residuals')
    # plt.title('Residuals(g) for the second order polynomial fit')
    # plt.show()

   
    return x,y,z,g

l1 = getData("improved/csv/1")
print(l1[3])


# plt.plot(x,y,'o')
# trendpoly = np.poly1d(z) 
# plt.plot(x,trendpoly(x))
# plt.show()