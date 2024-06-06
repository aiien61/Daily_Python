#! /usr/bin/env python3
# read_census_excel.py - Tabulates population and number of census tracts for each country
import openpyxl, pprint
print('Opening workbook...')

wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
county_data = {}

# Fill in county_data with each county's population and tracts.
print('Reading row...')

for row in range(2, sheet.max_row + 1):
    # Each row in the spreadsheet has data for one census tract.
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    population = sheet['D' + str(row)].value

    # Make sure the key for this state exists.
    county_data.setdefault(state, {})

    # Make sure the key for this county in this state exists.
    county_data[state].setdefault(county, {'tract': 0, 'population': 0})

    # Each row represents one census tract, so increment by one.
    county_data[state][county]['tract'] += 1

    # Increase the county population by the population in this census tract.
    county_data[state][county]['population'] += int(population)

print('Writing results...')


result_file = open('census2010.py', 'w')
result_file.write('all_data = ' + pprint.pformat(county_data))
result_file.close()
print('Done.')