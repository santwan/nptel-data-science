# -*- : utf-8 -*-
"""
@author : Santwan
"""
#========================================================
#CLASSIFYING PERSONAL INCOME
#========================================================
########### Required Packages ##############################
#To work with the dataframe
import pandas as pd

#To perform numerical operations
import numpy as np

#To visualize the data
import seaborn as sns 

#To partition the data
from sklearn.model_selection import train_test_split
#train_test_split from sklearn.model_selection is used to 
# split a dataset into training and testing sets. 
# It randomly partitions the data, allowing you to train a model on one subset
# and evaluate its performance on another.

#Importing Library for Logistic regression
from sklearn.linear_model import LogisticRegression


# Importing performance metrics - accuracy score and confusion
from sklearn.metrics import accuracy_score, confusion_matrix

########################################################################################

#Importing the data into the spider
data_income = pd.read_csv('income.csv')


#creating a copy of original data 
data = data_income.copy()


"""
#Exploratory data analysis

#1. Getting to know the data 
#2. Data preprocessing (missing values)
#3. Cross table and data visualization
"""
#===============================================================
#Getting to know the data
#===========================================================================================
#****** to check the variables' data type
print(data.info())

#***** To Check for missing values
data.isnull()

print("Data columns with null values:/n", data.isnull().sum())

#******* Summary of numerical variables
summary_num = data.describe()
print(summary_num)

#***** Summary of catagorical variable(object type)
summary_cate = data.describe(include = "O")
print(summary_cate)

#**********   Frequency of each categories
data['JobType'].value_counts()  #it gives how many types of job are in there and frequency of each job occurence 
data['occupation'].value_counts()


#*** Checking for unique classes
#print(np.unique(data['JobType']))
print(np.unique(data['occupation']))


#******* There exists '?' instead of sum

""" 
Go back and read teh data by including "na_values['?']" to consider '?' as NaN

"""
data = pd.read_csv('income.csv', na_values=[" ?"])
print(np.unique(data['JobType']))










