import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#read in the file
df = pd.read_csv('userdatamonth.csv', sep = '\t')

#change csv string values into datetime objects and create hour / day columns 
df['date'] = pd.to_datetime(df['date'])
df['hour'] = df['date'].dt.hour
df['day'] = df['date'].dt.dayofweek

#create a list of the df column names excluding the columns we don't want to iterate through
my_col = list(df.columns.values)
my_col.remove('date')
my_col.remove('day')
my_col.remove('hour')

#iterate through columns and replace raw values with a normalized value
for column in my_col:
    maximum = df[f'{column}'].max()
    minimum = df[f'{column}'].min()
    my_range = maximum - minimum
    df[f'{column}'] = (df[column] - minimum) / my_range

#get a sum of all the normalized values 
df['normalized total'] = df[my_col].sum(axis = 1)


#plot the data
fig, axes = plt.subplots(3,1)
fig.set_size_inches(12, 8)
fig.suptitle("Woodworking Subreddits Active User Data")
axes[0].set_title('User Count by Hour')
axes[1].set_title('User Count by Day - Mon=0')
axes[2].set_title('User Count by Day - raw')
sns.boxplot(ax = axes[0], data = df, y  ='normalized total',x = 'hour')
sns.violinplot(ax = axes[1], data = df, y  ='normalized total',x = 'day')
sns.scatterplot(ax = axes[2],data=df, x='date', y='normalized total')
fig.tight_layout()
plt.show()
fig.savefig('userdatamonth.png')

