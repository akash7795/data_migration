def add(*args):
    return ' + '.join(args)

def subtract(*args):
    return(" - ".join(args))

def multiply(*args):
    return(" * ".join(args))

def divide(*args):
    return(" / ".join(args))

def abs(colp):
    return("ABS({})".format(colp))

def ceil(colq):
    return("CEIL({})".format(colq))

def floor(colr):
    return("FLOOR({})".format(colr))

# def max(cols): - group by

def power(*args):
    pow_ = ",".join(args)
    return('POWER({})'.format(pow_))
