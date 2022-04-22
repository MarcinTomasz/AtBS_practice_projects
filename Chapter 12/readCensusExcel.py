#! python3
#Tabulate population and number of census tracts for each country.

import openpyxl, pprint

print('Opening workbook...')
wb = openpyxl.load_workbook('/Users/TC/Desktop/censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')

countyData = {}

print('Reading rows...')
for row in range(2, sheet.max_row + 1):
    state  = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop    = sheet['D' + str(row)].value
    
    #Make sure the key for this state exists.
    countyData.setdefault(state, {})

    #Make sure the key for this county in this state exists.
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

    #Each row represents one census tract, so increment by one.
    countyData[state][county]['tracts'] += 1

    #Increase the county population by the population in this census tract.
    countyData[state][county]['pop'] += int(pop)

#Open a new text file and write contents of countyData to it.
print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')