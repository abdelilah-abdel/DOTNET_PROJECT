import csv
import os

# specify the directory containing the CSV files
directory = '/home/abdel/Documents/DOTNET_Project/Data backup/DataRepo'

# specify the name of the output file
output_file = 'merged.csv'

# create an empty list to store the rows from the individual CSV files
rows = []

# iterate over the files in the directory
for filename in os.listdir(directory):
    # only process CSV files
    if filename.endswith('.csv'):
        # open the file and read the rows
        with open(f'{directory}/{filename}', 'r') as f:
            reader = csv.reader(f)
            # add the rows to the list
            rows.extend(list(reader))

# write the rows to the output file
with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print(f'Successfully merged {len(os.listdir(directory))} files into {output_file}.')