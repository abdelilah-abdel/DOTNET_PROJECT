import csv


def keep_first_5_columns(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        data = [row[:5] for row in csv_reader]

    with open(file_path, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)



keep_first_5_columns('/home/abdel/Documents/DOTNET_Project/Data backup/DataRepo/TEST/merged.csv')