#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___

# # K Nearest Neighbors Project 
# 
# Welcome to the KNN Project! This will be a simple project very similar to the lecture, except you'll be given another data set. Go ahead and just follow the directions below.
# ## Import Libraries
# **Import pandas,seaborn, and the usual libraries.**

# In[1]:
import pandas as pd
import  numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



# ## Get the Data
# ** Read the 'KNN_Project_Data csv file into a dataframe **

# In[2]:

df = pd.read_csv('KNN_Project_Data.csv')



# **Check the head of the dataframe.**

# In[23]:
df.head()




# # EDA
# 
# Since this data is artificial, we'll just do a large pairplot with seaborn.
# 
# **Use seaborn on the dataframe to create a pairplot with the hue indicated by the TARGET CLASS column.**

# In[4]:

sns.pairplot(df, hue='TARGET CLASS')



# # Standardize the Variables
# 
# Time to standardize the variables.
# 
# ** Import StandardScaler from Scikit learn.**

# In[5]:

from sklearn.preprocessing import StandardScaler

# ** Create a StandardScaler() object called scaler.**

scaler = StandardScaler()
# ** Fit scaler to the features.**

# In[7]:
scaler.fit(df.drop('TARGET CLASS', axis=1))





# **Use the .transform() method to transform the features to a scaled version.**

# In[8]:

transformed = scaler.transform(df.drop('TARGET CLASS', axis = 1))



# **Convert the scaled features to a dataframe and check the head of this dataframe to make sure the scaling worked.**

# In[9]:
scaled_df = pd.DataFrame(transformed)




# # Train Test Split
# 
# **Use train_test_split to split your data into a training set and a testing set.**

# In[10]:
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(scaled_df,df['TARGET CLASS'],test_size=0.30)




# # Using KNN
# 
# **Import KNeighborsClassifier from scikit learn.**

# In[12]:
from sklearn.neighbors import KNeighborsClassifier

# **Create a KNN model instance with n_neighbors=1**

# In[13]:
knn = KNeighborsClassifier(n_neighbors = 1)

# **Fit this KNN model to the training data.**

# In[14]:
knn.fit(X_train, y_train)
# Predictions and Evaluations
# Let's evaluate our KNN model!

# **Use the predict method to predict values using your KNN model and X_test.**

# In[24]:

pred = knn.predict(X_test)

# ** Create a confusion matrix and classification report.**

# In[16]:
from sklearn.metrics import confusion_matrix, classification_report

print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))


# # Choosing a K Value
# Let's go ahead and use the elbow method to pick a good K Value!
# 
# ** Create a for loop that trains various KNN models with different k values, then keep track of the error_rate for each of these models with a list. Refer to the lecture if you are confused on this step.**
errors = []
for i in range (1,50):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred = knn.predict(X_test)
    errors.append(np.mean(y_test != pred))




# **Now create the following plot using the information from your for loop.**

# In[20]:

plt.figure(figsize=(10,6))
plt.plot(range(1,50),errors,color='blue', linestyle='dashed', marker='o',
         markerfacecolor='red', markersize=10)
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')



# ## Retrain with new K Value
# 
# **Retrain your model with the best K value (up to you to decide what you want) and re-do the classification report and the confusion matrix.**

# In[21]:

knn = KNeighborsClassifier(n_neighbors=50)
knn.fit(X_train, y_train)
finalpred = knn.predict(X_test)
print(confusion_matrix(y_test, finalpred))
print(classification_report(y_test, finalpred))


# # Great Job!
