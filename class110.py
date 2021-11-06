import plotly.figure_factory as ff
import csv
import statistics 
import random 
import pandas as pd 
import plotly.graph_objects as go

df=pd.read_csv("data110pt2.csv")
data=df["temp"].tolist()

populationMean = statistics.mean(data)
populationSTDEV = statistics.stdev(data)    

#find mean and stdev of 100 data points
dataset=[]

for i in range(0,100):
    random_index=random.randint(0,len(data))
    value=data[random_index]
    dataset.append(value)

mean=statistics.mean(dataset)
std_deviation=statistics.stdev(dataset)
print("mean : ",mean)
print("st dev : ",std_deviation)


#function to plot the mean of the graph
#def show_fig(mean_list):
    #df=mean_list

fig = ff.create_distplot([data], ['temp'], show_hist = False)
#fig.add_trace(go.Scatter(x=[populationMean,populationMean],y=[0,1],mode="lines",name="MEAN"))
fig.show()
print(populationMean, populationSTDEV)