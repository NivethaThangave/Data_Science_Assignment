import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
# reading the CSV file 
foodData = pd.read_csv("foodData.csv")
# for styling the plot
plt.style.use('default')

# To indicate the x data
x=foodData.Year
# To Indicate the Y data
y=foodData.Percentage
# Plotting the normal graph using x and y axis
plt.plot(x,y)

# converting the pandas dataset column Percentage to a numpy array by following below:
mov_avg = foodData['Percentage'].to_numpy()

# giving the mean_interval as 3 , so that it will calculate as a1+a2+a3/(n)
mean_interval = 3
# craeting a Simple Moving Average function which pass Percentage and Mean_interval value to calculate the Simple Moving Average for the foodData Percentagee
def SMA(Percentage, mean_interval):
    i = 0
    moving_averages = []
    while i < len(Percentage) - mean_interval + 1:
        window = Percentage[i : i + mean_interval]
        window_average = round(np.sum(window) / mean_interval, 2)
        moving_averages.append(window_average)
        i += 1
    return moving_averages
Simple_Moving_Average = SMA(mov_avg, mean_interval)

print(Simple_Moving_Average)

plt.plot(Simple_Moving_Average, 'r', label="Simple Moving Average" )
plt.plot(mov_avg, '--b', label="Percentage" )
plt.legend()
