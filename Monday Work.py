#Problem-Set-9 
#Due 11.4.18

#Imports
import sqlite 
import parsers
import pandas as pd
import numpy as np
import csv 
################################################################################
# MONDAY WORK 
################################################################################
#I worked with Jacob Paul, Hannah Weber, Taylor Lawrence, Jack Sandberg 

# PROBLEM 1. Using the candy-data.csv file in the repo, populate an AnalysisData object that will hold the data you'll use for today's problem set. You should read in the data from the CSV, store the data in the dataset variable, and initialize the xs (column name) and targetY variables appropriately. targetY should reference the variable describing whether or not a candy is chocolate.


Analysis Data: 
#Initialize any attributes and handle preprocessing 
def __init__(self,type):
    self.type = type
    self.data = []
   
    #open the csv 
    with open (targetfile, 'w') as csv_file:
        
# Define a function 
def parseFile(self, filename): 
    if (self.type == "csv"):
        reader = csv.reader(open(candy-data.csv))
        for row in reader: 
            self.data.append(row)
    else:
        self.data = open(candy-data.csv).read()


# Store the data in the dataset variable 

# Initialize the xs and targetY 
# Target 


#PROBLEM 2. Create a function to initialize a LinearAnalysis object that takes a targetY as its input parameter. Create the same function for LogisticAnalysis. Note that you will use the LinearAnalysis object to try to predict the amount of sugar in the candy and the LogisticAnalysis object to predict whether or not the candy is chocolate.

#Create the function
def LinearAnalysis()
# Use the LinearAnalysis object to predict the amount of sugar in the candy

# Use the LogisticAnalysis object to predict whether or not the candy is chocolate 

#PROBLEM 3. Add a function to the LinearAnalysis object called runSimpleAnalysis. This function should take in an AnalysisData object as a parameter and should use this object to compute which variable best predicts how much sugar a candy contains using a linear regression. Print the variable name and the resulting fit.

#Add a function 
# Shows how you would use the object
analysisData = Parser("csv") 
analysisData.parseFile("candy-data.csv")
print(analysisData.data)


#PROBLEM 4.Add a function to the LogisticAnalysis object called runSimpleAnalysis. This function should take in an AnalysisData object as a parameter and should use this object to compute which variable best predicts whether or not a candy is chocolate using logistic regression. Print the variable name and the resulting fit. Do the two functions find the same optimal variable? Does one outperform the other?  