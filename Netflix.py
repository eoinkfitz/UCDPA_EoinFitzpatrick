import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime

netflix_data=pd.read_csv("netflix_titles.csv")


print(netflix_data.head())
print(netflix_data.shape)

missing_values_count = netflix_data.isnull().sum()
print(missing_values_count[0:5])

droprows= netflix_data.dropna()
print(netflix_data.shape,droprows.shape)

dropcolumns = netflix_data.dropna(axis=1)
print(netflix_data.shape,dropcolumns.shape)

print(netflix_data.isnull().sum())
#axis 0 is rows
#axis 1 is columns

#bfill takes value before
#ffill

cleaned_data=netflix_data.fillna(method="bfill").fillna(method="ffill")
print(cleaned_data["director"])
print(cleaned_data.isnull().sum())

#we can see now how the difference in director when we print the clean_data info

#dropping duplicate values

print(netflix_data.shape)
print(cleaned_data.shape)

noduplicates=netflix_data.drop_duplicates(subset=["director","cast","country"])

print(netflix_data.shape,noduplicates.shape)

#testing the blue to green

#we can see we dropped ~350 rows with these duplicates




