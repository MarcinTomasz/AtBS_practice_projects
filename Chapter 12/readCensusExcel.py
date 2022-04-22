#! python3
#Tabulate population and number of census tracts for each country.

import openpyxl, pprint
print('Opening workbook...')
wb = openpyxl.load_workbook('desktop/censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')

countyData = {}

print('Reading rows...')
for row in range(2, sheet.get_highest_row() + 1):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value
    
