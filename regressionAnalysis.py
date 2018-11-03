#Problem-Set-9 
#Due 11.4.18

#Import all the things
#import sqlite 
#import parsers
import pandas as pd
import numpy as np
import csv 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.linear_model import LogisticRegression

import matplotlib.pyplot as plt
################################################################################
# MONDAY WORK 
################################################################################
#I worked with Jacob Paul, Hannah Weber, Taylor Lawrence, Jack Sandberg 


#(a) AnalysisData
#Which will have, at a minimum, attributes called dataset (which holds the parsed dataset) and variables (which will hold a list containing the indexes for all of the variables in your data). 

class AnalysisData:
    #^ This is the initialization function
    #__ private reserved function that goes into Analysis
        
#Initialize (init) any attributes and handle preprocessing 
    def __init__(self):
        self.dataset= [] #expected this to be a list 
        self.variables= [] 
    
# Define a function 
    def parseFile(self,filename):
        #open the file
        self.dataset = pd.read_csv(filename)
        with open(filename) as csv_file:
            #if (self.type == "csv"):
                reader = csv.reader(csv_file)
                for row in reader: 
                    self.dataset.append(row)
                #else:
                    #self.data = open(filename).read()
                    

#(b) LinearAnalysis
#Which will contain your functions for doing linear regression and have at a minimum attributes called bestX (which holds the best X predictor for your data), targetY (which holds the index to the target dependent variable), and fit (which will hold how well bestX predicts your target variable).

#align initialized functions 
class LinearAnalysis:
    def __init__(self,targetY_input):
        self.bestX = "" 
        self.targetY = targetY_input 
        self.fit = ""
        
    def runSimpleAnalysis(self, data): 
        regr = LinearRegression()
        best_r2 = -1
        regr.fit(<candy>, <sugar>)
        regr.predict(<candy>)
        r2_score(<sugar>, <predicted values>)

#side notes: #depends on how you define your dataset and what you expect this value to be, assume we're looking for a column name, so try strings, integer = 0 or -1, list = [], dictionary = {}, () aren't a datatype  
#(c) LogisticAnalysis
#Which will contain your functions for doing logistic regression and have at a minimum attributes called bestX (which holds the best X predictor for your data), targetY (which holds the index to the target dependent variable), and fit (which will hold how well bestX predicts your target variable).

class LogisticAnalysis:  
    def __init__(self, targetY_input):
        self.bestX = ""
        self.targetY = targetY_input
        self.fit = ""


# PROBLEM 1. Using the candy-data.csv file in the repo, populate an AnalysisData object that will hold the data you'll use for today's problem set. You should read in the data from the CSV, store the data in the dataset variable, and initialize the xs (column name) and targetY variables appropriately. targetY should reference the variable describing whether or not a candy is chocolate.

data = AnalysisData()
data.parseFile("candy-data.csv")

#PROBLEM 2. Create a function to initialize a LinearAnalysis object that takes a targetY as its input parameter. Create the same function for LogisticAnalysis. Note that you will use the LinearAnalysis object to try to predict the amount of sugar in the candy and the LogisticAnalysis object to predict whether or not the candy is chocolate.

#See parts B and C

################################################################################
# WEDNESDAY WORK 
################################################################################
#PROBLEM 3. Add a function to the LinearAnalysis object called runSimpleAnalysis. This function should take in an AnalysisData object as a parameter and should use this object to compute which variable best predicts how much sugar a candy contains using a linear regression. 
#Print the variable name and the resulting fit (use LaTeX: R^2 R 2  to report the fit). Make sure your best predictor is NOT the same as the targetY variable. 

#Add a function 
#under part B
# Shows how you would use the object
analysisData = Parser("csv") 
analysisData.parseFile("candy-data.csv")
print(analysisData.data) 