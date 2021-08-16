import pandas as pd
file= pd.read_excel('dataNew.xls')
print(file)

files=file['Period'].str.split(' ',n=1,expand=True)
print(files)

file= file.assign(year=files[1])

file.index=file['year']
del file['year']
print(file.index)

setA=file.head(11)
print(setA)

setB=file.iloc[11:21]
print(setB)

setC=file.tail(10)
print(setC)

import numpy as np
import matplotlib.pyplot as plt

ps =setA['Calories'].sort_values()
index=np.arange(len(ps.index))
plt.bar(ps.index, ps.values)
plt.xlabel("Year", fontsize=17)
plt.ylabel("No. of calories",fontsize=17)
plt.xticks(index, ps.index, fontsize=14)
plt.title("[1900-1910]",fontsize=17)
plt.show();

ps =setB['Calories'].sort_values()
index=np.arange(len(ps.index))
plt.bar(ps.index, ps.values)
plt.xlabel("Year", fontsize=17)
plt.ylabel("No. of calories",fontsize=17)
plt.xticks(index, ps.index, fontsize=14)
plt.title("[1910-1920]",fontsize=17)
plt.show();

ps =setC['Calories'].sort_values()
index=np.arange(len(ps.index))
plt.bar(ps.index, ps.values)
plt.xlabel("Year", fontsize=17)
plt.ylabel("No. of calories",fontsize=17)
plt.xticks(index, ps.index, fontsize=14)
plt.title("[1920-1930]",fontsize=17)
plt.show();

setAsum=sum(setA['Calories'])
print(round(setAsum))

setBsum=sum(setB['Calories'])
print(round(setBsum))

setCsum=sum(setC['Calories'])
print(round(setCsum))

setAmean=setAsum/len(setA["Calories"])
print(round(setAmean,2))

setBmean=setBsum/len(setB["Calories"])
print(round(setBmean,2))

setCmean=setCsum/len(setC["Calories"])
print(round(setCmean,2))
