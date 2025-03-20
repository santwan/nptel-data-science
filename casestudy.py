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














