import os
import csv

# Creating a new path to copy the csv files after removing header
cwd_path = os.getcwd()
folder_path = os.path.join(cwd_path, 'header_removed')
os.makedirs(folder_path, exist_ok=True)

# Getting all the csv files in the current folder
csv_files = [file for file in os.listdir(cwd_path) if file.endswith('.csv')]
print(csv_files)

# Looping through the csv files
for file in csv_files:
    print('Removing contents from', file, '...')

    # Reading the contents of the csv files
    csv_file = open(file)
    csv_reader = csv.reader(csv_file)
    csv_data = list(csv_reader)

    # Removing the first row (assuming it is the header) from the csv file
    data_to_write = csv_data[1:]
    file_to_write = os.path.join(folder_path, file)

    # copying the contents of the file to the new file in the directory created above
    output_file = open(file_to_write, 'w', newline='')
    output_writer = csv.writer(output_file)
    for row in data_to_write:
        output_writer.writerow(row)
    output_file.close()
