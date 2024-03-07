def concat(*args):
    return "CONCAT({arguments})".format(arguments=','.join(args))

def upper(col):
    return "UPPER({arguments})".format(arguments=col)

def lower(col):
    return("LOWER({arguments})".format(arguments=col))

def strlen(col):
    return("LENGTH({arg})".format(arg=col))

def ltrim(col):
    return("ltrim({arg})".format(arg=col))

def rtrim(col):
    return("rtrim({arg})".format(arg=col))

def trim(col):
    return("trim({arg})".format(arg=col))

def concat_ws(*args):
    return("CONCAT_WS({arg})".format(arg=','.join(args)))
