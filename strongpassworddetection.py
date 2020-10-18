import re

password = input('Enter your password: '  )

pwRegex = re.compile(r'\w{8,}')

mo = pwRegex.search(password)

if mo == None:
    print('You have a weak password.')
else:
    print('That is a strong password.')


