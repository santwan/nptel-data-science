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
print(np.unique(data['JobType']))
print(np.unique(data['occupation']))


#******* There exists '?' instead of sum

""" 
Go back and read teh data by including "na_values['?']" to consider '?' as NaN

"""
data = pd.read_csv('income.csv', na_values=[" ?"])

#=============================================
#Data pre-processing 
#=============================================

data.isnull().sum()


missing = data[data.isnull().any(axis=1)]
#axis=1 means to consider at least one column value is missing 

"""
Points to Note:
    1. Missing values in Jotype = 1809
    2. Missing values in Occupation = 1816
    3. There are 1809 rows where two specific column 
    that is occupatio  and jobtype have missing values
    4. 1816 - 1809 =  7 => You still have occupation unfilled for 
    these 7 rows, because, jobtype is never worked
"""

data2 = data.dropna(axis = 0)
#dropping all the rows in the dataset where the NaN or null value is present 

#Relationship between independent variable
#correlation =  data2.corr()
correlation = data2.select_dtypes(include=['number']).corr()
#print(correlation)
#None of the numerical variables are corelated


#=============================================================================
#Cross Tables and Data Visualization
#===============================================================================
# Extracting the columns name
data2.columns
print(data2.dtypes)


#===========================
#Gender proportion table:
    
gender = pd.crosstab( index = data2["gender"], columns = 'count', normalize = True )

print(gender)


#===========================
#Gender vs salary status:
    
gender_salstat = pd.crosstab(index = data2["gender"], columns = data2["SalStat"], margins = True, normalize= "index")

print(gender_salstat)


#===========================
# Frequency Distribution of 'Salary status'

salstat = sns.countplot(data2['SalStat'])
"""
75% of people's salary status is <= 50000
25% od peoples salary status is > 50000
"""

###################   Histogram of Age ######################
sns.distplot(data2['age'], bins=10, kde=False)
#Conlusion : People with age 20-45 are high in frequency

###################   Box Plot - Age vs salary  status ################
# A bivariate analysis to check how age is affecting the salary  status
sns.boxplot(x='SalStat', y='age', data=data2)
data2.groupby('SalStat')['age'].median()


#==============================================================================
#Logistic Regression
#=========================================================================================
data2['SalStat'] = data2['SalStat'].map({' less than or equal to 50,000':0, ' greater than 50,000':1})
print(data2) #integer encoding

new_data = pd.get_dummies(data2, drop_first=True) #one hot encoding #converting catagorical data to dummi

#Storing teh column names
columns_list = list(new_data.columns)
print(columns_list)

#Separating the input names from the data
features = list(set(columns_list)-set(['SalStat']))
print(features)

#Storing the output values in y
y = new_data['SalStat'].values
print(y)

#Splitting the data into train and test











