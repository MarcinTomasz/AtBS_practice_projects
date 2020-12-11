#Program that finds gaps in numbering of files and fills in those gaps.

import os, shutil

file_path = input('What file path do you want to check for missing number?   \n')

abs_file_path = os.path.abspath(file_path)

#for spam in range(1, 11):
#    new_file = open('C:\\Users\\novyp\\Desktop\\python_work\\AtBS\\AtBS_practice_projects\\fillinginthegaps\\spam%s.txt' % (spam), 'w')

base_name = os.path.basename(abs_file_path)
dir_name = os.path.dirname(abs_file_path)

print(abs_file_path)
print(dir_name)
print(base_name)
print(abs_file_path)

print('\nHere are the files in the directory:  \n' )

files = os.listdir(file_path)
for file in files:
    print(file)

number = 1
new_file_name = 'spam' + str(number - 1) + '.txt'

print(new_file_name)

while True:
    for file in abs_file_path:
        check_file = os.path.basename(abs_file_path) + 'spam' + str(number) + '.txt'
        
        if not os.path.exists(check_file):
            break
        
        
    
