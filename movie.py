import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from itertools import chain
import cv2
from PIL import Image
import io
#Backround that is constant in every frame
def bac(x_points, y_points, med_vals):
    plt.clf()
    height = 9 
    width = 7
    width_height = (width, height) 
    fig = plt.figure(figsize=width_height)
    for arr in y_points:
        plt.plot(x_points, arr)
    plt.plot(x_points, med_vals, "r-" )
    fig.canvas.draw()
    saved_bg = fig.canvas.copy_from_bbox(fig.bbox)
    (dot,) = plt.plot([], [], 'o', color='r', markersize=5, animated=True)
    
    return (dot,saved_bg, fig)
#Generates frames
def backround_generation(x_points, median, index, d, bg, sf):
    sf.canvas.restore_region(bg)
    d.set_xdata(x_points[index])
    d.set_ydata(median)
    sf.draw_artist(d)
   
  
    sf.canvas.blit(sf.bbox)       # blit only redraws pieces that have changed
    sf.canvas.flush_events()    # blit only redraws pieces that have changed

    img = bg
    dpi = 100
    buf = io.BytesIO()
    sf.savefig(buf, format="png", dpi=dpi)
    buf.seek(0)
    img_arr = np.frombuffer(buf.getvalue(), dtype=np.uint8)
    buf.close()
    img = cv2.imdecode(img_arr, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    plt.close()
   
    return img


#Find the median value to plot red dot on
def find_median(x_arr, y_arr, collumn):
    median = []
    for i in range((len(x_arr))):
        tmp = []
        for j in range(collumn):
            tmp.append(y_arr[j + (i * collumn)])
        median.append(sorted(tmp)[int(len(tmp)//2)])        #calculation to find median
    return median





raw_data = pd.read_excel('scene2.xlsx', 'Sheet1', header=2)

x_vals = []
yp_vals = []

y_vals = []
coll = len(raw_data.columns) - 1


#Put data frame values into lists
for column in raw_data:
    if(column == 'Time'): 
        time_data = raw_data['Time']
        x_vals = raw_data['Time']
    else:
        column_obj = raw_data[column]
        yp_vals.append(column_obj.values)
        


df1 = raw_data.loc[:, raw_data.columns != 'Time']           #orient Y values to be put in list as rows (easier to find median)
for i in df1.stack():
    y_vals.append(i)

#Median points that the red dot moves on
med_values = find_median(x_vals, y_vals, coll)

#General movie settings 
size = (700, 900)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
output_file = "movie3.avi"
video_writer = cv2.VideoWriter(output_file, fourcc, 85, size)

#Generate the cosntant backround 
d,bg,sf = bac(x_vals, yp_vals, med_values)
#Put final frames together 
for idx, med in enumerate(med_values):
   
    final_img = backround_generation(x_vals, med, idx, d, bg, sf)
    video_writer.write(final_img)
    cv2.imshow('frame', final_img)
    
video_writer.release()
cv2.destroyAllWindows()
