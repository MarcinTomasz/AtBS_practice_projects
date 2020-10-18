import re

password = input('Enter your password: '  )

pwRegex1 = re.compile(r'\w{8,}')
pwRegex2 = re.compile(r'\d+')
pwRegex3 = re.compile(r'[A-Z]+')
pwRegex4 = re.compile(r'[a-z]+')

mo1 = pwRegex1.search(password)
mo2 = pwRegex2.search(password)
mo3 = pwRegex3.search(password)
mo4 = pwRegex4.search(password)


if mo1 == None or mo2 == None or mo3 == None or mo4 == None:
    print('You have a weak password.')
else:
    print('That is a strong password.')
