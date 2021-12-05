import pandas as pd

pd.set_option('display.max_columns', 20)

raw_vg_sales = pd.read_csv('Week 8 - vgsales.csv')

first_thousand = raw_vg_sales.iloc[:1000,:]

# Build a function
def subset_data(df, row_select, col_select):
  # DOCSTRING
  """
  This function is used to dynamically slice data from 
  a users dataframe. 

  row_select: this represents the rows the user wants
  col_select: this is the columns
  """
  # Magic happens
  subset = df.iloc[row_select, col_select]
  
  # return this value
  return subset



first_row = subset_data(raw_vg_sales, 0, [0,1,2,3])
tenth_row = subset_data(raw_vg_sales, 10, [0, 1, 2, 3])

for row in range(0, len(first_thousand)):
  print(subset_data(first_thousand, row, [0, 1, 2]))

