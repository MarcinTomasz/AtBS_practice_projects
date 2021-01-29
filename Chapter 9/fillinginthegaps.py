#Program that finds gaps in numbering of files and fills in those gaps.

import os, shutil, re 

file_path = input('What file path do you want to check for missing number?   \n')

abs_file_path = os.path.abspath(file_path)

prefix = input('What prefix, including the numbering, would you like to check: ')

#Regex to find the chosen sequentially named files.
ordered_regex = re.compile(r'({0})(\d*)(.*)(\..*)'.format(prefix))

found = [] #Keeps track of numbering of files with chosen prefix.

#Filewalk to find files with chosen prefix
for folders, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        
        if ordered_regex.search(filename) is not None:
            #Determine length of numbering digits(to be used in new names)
            num_length = int(len(ordered_regex.search(filename).group(2)))

            #Find extension of files (for later naming)
            extension = ordered_regex.search(filename).group(4)

            #Number of files with chosen prefix
            found.append(ordered_regex.search(filename).group(2))

    ordered = sorted([int(x) for x in found])

#Loop to check for correct numbering based on amount of files found
for number in range(1, len(found) + 1):

    #Calculate amount of 0's to prepend to reconstruct original format
    zeroes = '0' * (nu,_length - len(str(number)))

    #Recreate path of what should be then next file
    current_file = '{}/{}{}{}'.format(folder, prefix, zeroes, number, extension)

    #Check if the file exists
    if os.path.exists(current_file) is False:
        #Find numbering of actual next file and format path
        next_num = ordered[number - 1]
        next_zeroes = '0' * (num_length - len(str(next_num)))
        next_file = (folder + '/' + prefix + str(next_zeroes) + str(next_num) + extension)
        
        #Rename actual to desired with shutil move
        shutil.move(next_file, current_file)

print('File numbering has been fixed.')
