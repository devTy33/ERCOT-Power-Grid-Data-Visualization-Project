# ERCOT-Power-Grid-Data-Visualization-Project
Python script to help visualize frequency oscillation points in the Texas ERCOT power grid


This program is for CURENT. They are an engineering research center headquartered here at the University of Tennessee. They work a lot in power grid
research, and this program will help them visualize oscillation data in the Texas ERCOT power grid.

oscillation_data.txt contains the power grid oscillation data. The data is collected through censors around the state of Texas called "buses". Each row in 
the excel file represents readings from a single bus over a given period of time. 

movie.py reads in the oscialtion data using pandas and creates plots using matplotlib. Each bus is a line on the matplotlib graph. The red line on the
graph is the median of all the bus data at that given time. The matlplot lib graph is then turned into a collection of frames. A red dot traces the 
red median line for each x value. I save all of these frames and collect them together into a video using a library called OpenCV.

The output video is contained in this google drive: https://drive.google.com/drive/u/0/folders/1Yg9HoycC6-pdKb7HmFQRW9Vr1DU5ZbUY


This is half of the project. The rest of the project is currently being developed. The final result should look something like this, the only difference 
is that the map will be of the Texas ERCOT grid: 

  https://www.youtube.com/watch?v=N1h8Q8WFPX8
