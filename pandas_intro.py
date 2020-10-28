import pandas as pd

test = pd.read_csv("data.csv")[:5]

"""
Since .iterrows() returns each DataFrame row as a tuple of (index, pandas Series) pairs, 
you can either split this tuple and use the index and row-values separately
"""

for i, row in test.iterrows():
    print(i)
    print(row)
    print(type(row))


for row_tuple in test.iterrows():
    print(row_tuple)
    print(type(row_tuple))

"""
Create a new column
"""
total_visit = []
for i, row in test.iterrows():
    first_num = row["VISIT_NUM"]
    second_num = row["VISIT_PAGE_NUM"]
    visit_number = first_num + second_num
    total_visit.append(visit_number)

test["total_visit"] = total_visit
print(test)

"""
Iterating with itertuples()
"""
# print pandas data 
for i in test.itertuples():
    print(i)

# .itertuples() returns special data type that called namedtuple
# To access row data, use a dot, No bracket 
for row in test.itertuples():
    visit = row.VISIT_NUM
    order = row.ORDER_NUM
    print(visit, order)

"""
Apply a function to a column in the pandas dataframe
with .apply()
When we use .apply(), we do not need to use for loop
The .apply() method let's you apply functions to all rows or columns of a DataFrame 
by specifying an axis.
"""

# Gather sum of all columns
test.apply(sum, axis=0)

# Sum of each row from two columns
test[['VISIT_NUM', 'VISIT_PAGE_NUM']].apply(sum, axis=1)

# Apply a lambda function
def event_confirm(EVENT1):
    if EVENT1 == 1:
        return "YES"
    else:
        return "NO"

test.apply(lambda row: event_confirm(row['EVENT1']), axis=1)

# Make a new colmun
def total_order(purchase, units):
    total = purchase * units
    return total

total = total_order(test['PURCHASE'].values, test['UNITS'].values)
print(total)

test['purchase_units'] = total
test.head()

"""
Compared to three methods to make a new cokumn
at the dataframe
"""
import numpy as np
import pandas as pd

#load data
baseball_df = pd.read_csv('baseball.csv')

#Make a function to predict 
def predict_win_perc(RS, RA):
    prediction = RS ** 2 / (RS ** 2 + RA ** 2)
    return np.round(prediction, 2)

# Use a loop and .itertuples() to collect each row's predicted win percentage
win_perc_preds_loop = []
for row in baseball_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA
    win_perc_pred = predict_win_perc(runs_scored, runs_allowed)
    win_perc_preds_loop.append(win_perc_pred)

# Apply predict_win_perc to each row of the DataFrame
win_perc_preds_apply = baseball_df.apply(lambda row: predict_win_perc(row['RS'], row['RA']), axis=1)

# Calculate the win percentage predictions using NumPy arrays
win_perc_preds_np = predict_win_perc(baseball_df['RS'].values, baseball_df['RA'].values)
baseball_df['WP_preds'] = win_perc_preds_np
print(baseball_df.head())