def bar():
    from mod import foo
    foo('corge')

print (bar())

# import * only allowed at module level, bellow statments won't work
def bar_all():
    from mod import *
    foo('corge')

print (bar_all())

