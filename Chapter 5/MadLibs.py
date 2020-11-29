#Program to display a text file, ask for words to replace displayed text, print new text.

import re

f1 = 'The ADJECTIVE panda walked to the NOUN1 and then VERB. A nearby NOUN2 was unaffected by these events.'
MadLibsfile = open('C:\\Users\\novyp\\Desktop\\python_work\\AtBS\\AtBS_practice_projects\\MadLibs.txt')
f2 = MadLibsfile.read()
MadLibsfile.close()

print(f2)

new_adjective = input('\nReplace ADJECTIVE with: ')
new_noun1 = input('\nReplace NOUN1 with: ')
new_verb = input('\nRepalce VERB with: ')
new_noun2 = input('\nReplace NOUN2 with: ')

MadLibsRegexAdj = re.compile(r'ADJECTIVE')
f3 = MadLibsRegexAdj.sub(new_adjective, f2)

MadLibsRegexN1 = re.compile(r'NOUN1')
f4 = MadLibsRegexN1.sub(new_noun1, f3)

MadLibsRegexV = re.compile(r'VERB')
f5 = MadLibsRegexV.sub(new_verb, f4)

MadLibsRegexN2 = re.compile(r'NOUN2')
f6 = MadLibsRegexN2.sub(new_noun2, f5)

print(f6)

new_MadLibsfile = open('C:\\Users\\novyp\\Desktop\\python_work\\AtBS\\AtBS_practice_projects\\new_Madlibsfile.txt', 'w')
new_file = new_MadLibsfile.write(f6)

print(new_file)
new_MadLibsfile.close()
