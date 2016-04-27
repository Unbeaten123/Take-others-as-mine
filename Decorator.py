# -*- coding: utf-8 -*-
#Decorator的使用
#The usage of decorator in python
import functools

def log(*text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if text:
                print 'begin call %s %s():' % (text[0], func.__name__)
                rst = func(*args, **kw)
                print 'end call %s %s():' % (text[0], func.__name__)
                return rst
            else:
                print 'begin call %s():' % (func.__name__)
                rst = func(*args, **kw)
                print 'end call %s():' % (func.__name__)
                return rst
        return wrapper
    return decorator

@log('test')
def now():
    print 'You are brilliant!'
now()
@log()
def now():
    print "You are brilliant!"
now()
@log('execute')
def now():
    print 'You are brilliant!'
now()
