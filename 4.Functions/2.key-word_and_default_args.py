# default args

def greet(name, msg='Hello',):
    return msg + ' ' + name


print(greet('Sri'))


# Keyword args

def name(fname, lname, ):
    return fname+' '+lname


print(name(lname='K', fname='Srivatsav'))
