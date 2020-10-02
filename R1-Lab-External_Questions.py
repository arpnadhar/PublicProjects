#!/usr/bin/env python
# coding: utf-8

# # External Lab

# # Part-1

# ## About the dataset
# 
# This is perhaps the best known database to be found in the pattern recognition literature. The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant.  One class is linearly separable from the other 2; the latter are NOT linearly separable from each other.
# 
# Attribute Information:
#    1. sepal length in cm
#    2. sepal width in cm
#    3. petal length in cm
#    4. petal width in cm
#    5. class: 
#       -- Iris Setosa
#       -- Iris Versicolour
#       -- Iris Virginica

# ### Read the dataset and store it in the dataframe named Iris

# In[205]:


import pandas as pd
Iris = pd.read_csv("Iris_external.csv")
Iris


# ### Find out the datatypes of each and every column

# In[206]:


Iris.dtypes


# ### Print top 10 & bottom 10 samples from the dataframe

# In[207]:


Iris.head(10)


# In[208]:


Iris.tail(10)


# ### Find the shape of the dataset

# In[209]:


Iris.shape


# ### Set the index of the dataframe to be the first column

# In[210]:


#Iris.set_index(Iris.columns[0])
Iris.index = Iris.iloc[:,0]
Iris


# In[ ]:





# ### Use iloc function to print all the rows of the 3rd column 

# In[211]:


Iris.iloc[:, 2]


# ### Slicing
# Print only the Sepal width and Sepal Length for first 10 rows 

# In[212]:


Iris.iloc[0:10, 0:2]


# ### Using Logical statements for indexing
# Print all the columns of row which has class name "Iris-setosa"

# In[213]:


Iris[Iris['Class'] == 'Iris-setosa']


# ### Multiply Sepal Length and width and store it under the column name "SepalExtra" in the same Iris dataframe

# In[214]:


Iris['SepalExtra'] = Iris['Sepal Length (in cm)'] * Iris['Sepal Width in (cm)']


# In[215]:


Iris


# ### Find out the mean and variance for each column but for class column 

# In[216]:


columns = Iris.columns

for i in columns:
    if(i!='Class'):
        print("Mean of column %s is->  %f and variance is -> %f"%(i, Iris[i].mean(), Iris[i].var()))


# ### Write a function that accepts two numbers as input and prints them - Pass the Sepal length and sepal width of 5th row and print the output

# In[217]:


printfunc = lambda num1, num2 : print("Sepal Length of 5th row is is %f and sepal width is %f"%(num1, num2))
printfunc(Iris.iloc[4,0], Iris.iloc[4,1])


# ### Find the range of all the columns in the dataset
# 
# *Range = Max value - Min value (in the column)*

# In[218]:


import numpy as np
numericColumns = Iris.select_dtypes(np.number)
numericRange = numericColumns.max() - numericColumns.min()

stringColumns = Iris.select_dtypes(object)
stringRange = stringColumns.max() + '-' + stringColumns.min()

numericRange.append(stringRange)


# ### Sort the entire dataset according to the column Petal width

# In[219]:


Iris.sort_values(by='Petal width (in cm)', inplace=True)
Iris


# ### Remove the new column "SepalExtra" from the dataframe

# In[220]:


Iris.drop('SepalExtra', axis=1, inplace=True)
Iris


# ### Take only the top 10 rows of the dataset with only first 3 columns and store it in a dataframe named "IrisSubset" 

# In[221]:


IrisSubset = Iris.iloc[0:10,0:3]


# In[222]:


IrisSubset


# # Part-2

# ## The dataset HR contains information collected from the survey floated by a HR within the company.
# 
# 
# As a part of this lab, you are expected to answer the below questions

# ### Import numpy and Pandas 

# In[223]:


import numpy as np
import pandas as pd


# ### Import the dataset (Note: The dataset is in .txt format) - Make sure to use delimiters

# In[224]:


HRdata = pd.read_csv('HR_external.txt',sep='\s+', engine ='python')
HRdata


# ### Print the no of rows and columns in the dataset 

# In[225]:


print("Number of rows and columns in HR data are:")
HRdata.shape


# In[ ]:





# ### Find out the type of each and every column in the dataset 

# In[226]:


HRdata.dtypes


# In[ ]:





# ### Print out all the rows from 3rd column to 10th columns  

# In[227]:


HRdata.iloc[:,2:10]


# ### Find out the no of male & female employees in the company
# 
# *Hint: Use can use a condition to find out the no of 1s and 0s in gender and sum it*

# In[228]:


HRdata['Gender'].value_counts(dropna=False)

#Let us assume 1 is "Male" and "2" is female


# In[ ]:





# ### Find out the IQR for the column - Age 
# 
# *Hint: IQR - Interquartile range = 75th percentile - 25th percentile* 

# In[229]:


ageColumn = HRdata['Age']
Q1 = ageColumn.quantile(0.25)
Q3 = ageColumn.quantile(0.75)
print(Q3-Q1)


# ### Find out the mean, median and variance for the column - DailyRate 

# In[230]:


dailyRateColumn = HRdata['DailyRate']
print(" Mean of daily rate column is %f"%dailyRateColumn.mean())
print(" Median of daily rate column is %f"%dailyRateColumn.median())
print(" Variance of daily rate column is %f"%dailyRateColumn.var())


# ### Plot the attrition column (Since it is a categorical variable, chose the plot accordingly)

# In[231]:


HRdata['Attrition'].value_counts().plot(kind='bar')


# In[ ]:





# ### Plot Total working years using matplotlib plot function

# In[232]:


import matplotlib.pyplot as plt

HRdata.columns


# In[233]:


wrkYearsColumn = HRdata['TotalWorkingYears']
wrkYearsColumn.plot(kind = 'hist',bins = 10,figsize = (15,15))


# In[ ]:





# In[234]:


#Show Boxplot for working years to see mean median outliers
plt.boxplot(wrkYearsColumn) 
plt.show() 


# In[ ]:





# In[235]:


# scatter plot between total working years and age 
plt.scatter(wrkYearsColumn, HRdata['Age']) 
plt.show() 
  
# scatter plot between total working years and monthly income 
plt.scatter(wrkYearsColumn, HRdata['MonthlyIncome']) 
plt.show() 
  
# scatter plot between 
plt.scatter(wrkYearsColumn, HRdata['YearsAtCompany']) 
plt.show() 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




