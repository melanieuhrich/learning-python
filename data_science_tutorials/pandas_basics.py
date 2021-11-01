# Pandas --
    # -- a high-level data manipulation tool
    # -- built on the Numpy package
    # -- key data structure is called the DataFrame
    # -- DataFrames allow you to store and manipluate tabular data in rows of observations and columns of variables



# creating a DataFrame using a dictionary
dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
brics = pd.DataFrame(dict)
# prints in a tabular format
print(brics)



# pandas automatically assigned a key for each country as the numerical values 0 through 4

# setting the index for brics manually
brics.index = ['BR', 'RU', 'IN', 'CH', 'SA']

# prints with the country code in place of the numerical index
prints(brics)



# creating a DataFrame by importing a csv file
import pandas as pd

# import the cars.csv data: cars
cars = pd.read_csv('cars.csv')

# prints in a tabular format 
print(cars)



# indexing a DataFrame using square bracket notation 

# import pandas and cars.csv
import pandas as pd 
cars = pd.read_csv('cars.csv', index_col = 0)

# single brackets will output country column as Pandas Series
print(cars['cars_per_cap'])

# double brackets will ouput country column as Pandas DataFrame
print(cars[['cars_per_cap']])

# print out DataFrame with country and drives_right columns
print(cars[['cars_per_cap', 'country']])



# square brackets can also be used to access observations (rows) from a DataFrame

# import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# print out first 4 observations
print(cars[0:4])

# print out fifth and sixth observation 
print(cars[4:6])



# to perform a data selection operation 

# loc is label-based
# prints out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])

# iloc is integer index-based
# prints out observation for Japan
print(cars.iloc[2]) 