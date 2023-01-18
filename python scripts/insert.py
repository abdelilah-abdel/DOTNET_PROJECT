import pandas as pd
import warnings
warnings.filterwarnings('ignore')

import os
import pandas as pd


df = pd.read_csv('finalnewdatal.csv')



# Read the Excel file


# Iterate over the rows in the dataframe
for index, row in df.iterrows():
    # Build the INSERT statement
    # insert_stmt = f"INSERT INTO Reviews  VALUES ('{row['HotelId']}', '{row['Date']}', {row['rate']}', '{row['title']}', '{row['Cleaned_R']}');"
   # insert_stmt = f"INSERT INTO Review    VALUES ({row['rating']}, '{row['new_reviews']}', {row['rate']}, '{row['title']}', '{row['review']}');"
    insert_stmt = f"INSERT INTO Review    VALUES ({row['rating']}, '{row['new_reviews']}');"

    # Print the INSERT statement
    print(insert_stmt)

