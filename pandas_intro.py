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
