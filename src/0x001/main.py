import pandas as pd
df1 = pd.read_csv("./Datasets/tmdb_5000_credits.csv", low_memory=False)
df2 = pd.read_csv("./Datasets/tmdb_5000_movies.csv", low_memory=False)


# merge the 2 data sets on the id column
df1.columns = ['id', 'title', 'cast', 'crew']
df2 = df2.merge(df1, on='id')
print(df2.head())


print('Count of the Dataset is: ', df2.count(), "\n")
# Shape of the Dataset is:  (4803, 23)
print('Shape of the Dataset is: ', df2.shape, "\n")
mean = df2['vote_average'].mean()
print("Mean is: ", mean, '\n')  # Mean is:  6.092171559442016

# Choosing the films that have a rating more than 90% of the others
m = df2['vote_count'].quantile(0.9)
# 1838.4000000000015
print('Films who has rating more than 90% of other films\n', m)
print("\n")


median = df2['vote_average'].median()
print("Median is: ", median, '\n')  # Median is: 6.2

mode = df2['vote_average'].mode()
# Mode is: 0    6.0    1    6.5     Name: vote_average, dtype: float64
print("Mode is: ", mode, '\n')

MaximumValue = df2['vote_average'].agg(max)
print("max: ", MaximumValue, '\n')  # max:  10.0
MinimumValue = df2['vote_average'].agg(min)
print("min: ",  MinimumValue, '\n')  # min:  0.0

range = MaximumValue - MinimumValue
print("Range is: ", range)  # Range is:  10.0


m = df2['vote_average'].quantile([0.9, 0.5, 0.25])
print('Quartiles is: ', m)
print("\n")

# Quartiles is:  0.90    7.3
# 0.50    6.2
# 0.25    5.6
# Name: vote_average, dtype: float64


variance = df2['vote_average'].var()
print('Variance is: ', variance, "\n")  # Variance is:  1.4270982196241189

std = df2['vote_average'].std()
# Standard Deviation  is:  1.1946121628478923
print('Standard Deviation  is: ', std, "\n")
