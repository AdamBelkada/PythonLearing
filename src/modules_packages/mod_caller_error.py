try:
    import baz
except ImportError:
    print ('Module not found')
try:
    from mod import baz
except ImportError:
    print ('object not found in module')