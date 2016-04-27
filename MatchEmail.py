# -*- coding: utf-8 -*-
import re

#email = raw_input('Enter the email: ')
email = ['894736464@qq.com', 'yuzhizhou@live.com', '__et@hello.org', 'bill.gates@microsoft.com',
'<Zhizhou Yu> swjtu@edu.org', '<Tom Cruse> tom@gmail.com']
for i in email:
    if re.match(r'^<[a-zA-Z]+\s[a-zA-Z]+>\s([0-9a-zA-Z]+)@[^\s]*(com|org)$', i):
        print '%s is a legal Email Address that with name!' % i
    elif re.match(r'^([0-9a-zA-Z]+)@[^\s]*(com|org)$', i):
        print '%s is a legal Email Address!' % i
    else:
        print '%s is an illegal Email Address!' % i
