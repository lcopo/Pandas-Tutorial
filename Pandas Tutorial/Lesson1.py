# Import all libraries needed for the tutorial

# General syntax to import specific functions in a library:
##from (library) import (specific library function)
from pandas import DataFrame, read_csv

# General syntax to import a library but no functions:
##import (library) as (give the library a nickname/alias)
import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import os
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number

#print('Python version ' + sys.version)
#print('Pandas version ' + pd.__version__)
#print('Matplotlib version ' + matplotlib.__version__)


# The inital set of baby names and bith rates
names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]

#Zip merges the lists
BabyDataSet = (zip(names,births))

#Creating the DataFrame object
df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])

#Export DataFrame to a csv file
df.to_csv('BirthsInfo.csv', index=False, header=False)
#Read csv file
FilePath = 'C:\Users\Luis\Desktop\Luis\Cursos\Pandas Tutorial\BirthsInfo.csv'
df = pd.read_csv(FilePath)

df = pd.read_csv(FilePath, header=None)
df = pd.read_csv(FilePath, names=['Names', 'Births'])
print df

#Remove the csv file
os.remove(FilePath)

#Check DataTypes
#print df.dtypes
#print df.Births.dtype

#Select the baby name with the highest birth rate
#print df['Births'].max()
Sorted = df.sort_values(['Births'])
print Sorted
print Sorted.tail(1)

#Create graph
df['Births'].plot()
#Maximum value in the dataset
MaxValue = df['Births'].max()
# Name associated with the maximum value
MaxName = df['Names'][df['Births'] == df['Births'].max()].values
# Text to display on graph
Text = str(MaxValue) + " - " + MaxName

# Add text to graph
plt.annotate(Text, xy=(1, MaxValue), xytext=(8, 0),
                 xycoords=('axes fraction', 'data'), textcoords='offset points')

print("The most popular name")
df[df['Births'] == df['Births'].max()]