import pandas as pd
df = pd.read_csv('../Swiggy.csv')
df.columns = [c.lower() for c in df.columns] # PostgreSQL doesn't like capitals or spaces

from sqlalchemy import create_engine
engine = create_engine('postgresql://yashbaddid@localhost:5432/foodiefleet2')

df.to_sql("sample_data", engine)