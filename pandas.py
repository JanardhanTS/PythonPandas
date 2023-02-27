import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

url = 'https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv'
df = pd.read_csv(url)

df1=df.mean()
df2=df.std()
df3=df.min()
df4=df.max()
df5=df.quantile()
print ("=============================Mean of the dataset==============================")
print(df1)
print ("============================STD of the dataset===============================")
print(df2)
print ("============================Min of the dataset===============================")
print(df3)
print ("=============================Max of the dataset==============================")
print(df4)
print ("=============================quntile of the dataset==============================")
print(df5)
print ("=============================Feature type of dataset==============================")

for col in df.columns:
  if df[col].dtype == 'int64' or df[col].dtype == 'float64':
   print(col, ': Numerical')
  elif df[col].dtype == 'object':
   print(col, ': Categorical')
  elif df[col].dtype == 'datetime64':
    print(col, ': Date/time')
  elif df[col].dtype == 'bool':
   print(col, ': Boolean')
  else:
    print(col, ': Text')
print ("=============================Check for null values==============================")
print(df.isnull().any())

print ("=============================Visualise1==============================")
df.plot(kind='line',x='Country', y='Health (Life Expectancy)')
plt.show()
print ("=============================Visualise1==============================")
df.plot(kind='scatter', x='Country', y='Health (Life Expectancy)')
plt.show()

print ("=============================Visualise1==============================")

# Create the plot
sns.scatterplot(x='Country', y='Health (Life Expectancy)', data=df)

# Customize the plot
sns.set_style('whitegrid')
plt.title('sns Plot')
plt.xlabel('Country')
plt.ylabel('Health')

# Show the plot
plt.show()
