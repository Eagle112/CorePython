#!/usr/bin/env python

from random import randrange, choice
from string import ascii_lowercase as lc
from time import ctime

tlds = ( 'com', 'edu', 'net', 'org', 'gov' )
123
456
789
for i in range(randrange(5, 11)):
    dtint = randrange(2**32)	# random date
    dtstr = ctime(dtint)	# date string
    llen = randrange(4, 7)	# login llen
    abc
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen, 13)	# domain dlen
    edf
    123
    dom = ''.join(choice(lc) for j in range(dlen))
    print '%s::%s@%s.%s::%d-%d-%d' % (dtstr, login,
        dom, choice(tlds), dtint, llen, dlen)
123123123123123123123123123

123123123