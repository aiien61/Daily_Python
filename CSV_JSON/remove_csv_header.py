#! /usr/bin/env python3
# remove_csv_header.py - Removes the header from all CSV files in the current working directory
import csv, os

os.makedirs('HeaderRemoved', exist_ok=True)

# Loop through eveyr file in the current working directory
for csvfilename in os.listdir('.'):
    if not csvfilename.endswith('.csv'):
        continue

    print(f'Removing header from {csvfilename}...')

    # Read the CSV file in (skipping first row).
    csv_rows = []
    csv_file = open(csvfilename)
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if csv_reader.line_num == 1:
            continue
        csv_rows.append(row)
    
    csv_file.close()

    # Write out the CSV file.
    csv_file = open(os.path.join('HeaderRemoved', csvfilename), 'w', newline='')
    csv_writer = csv.writer(csv_file)
    for row in csv_rows:
        csv_writer.writerow(row)
    
    csv_file.close()