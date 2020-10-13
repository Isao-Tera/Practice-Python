"""datanase schema
A PostgreSQL database is set up in your local environment, 
which contains this database schema. 
It's been filled with some example data. 
You can use pandas to query the database using the read_sql() function.
You'll have to pass it a database engine, 
which has been defined for you and is called db_engine.
"""
import pandas as pd
# read data
data = pd.read_sql("""
SELECT fist_name, last_name
FROM "Customer"
ORDER BY last_name, first_name
""", db_engine)

# Confirm data
print(data.head(3))

# Confirm data information
print(data.info())