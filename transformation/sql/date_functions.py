def date_format(*args):
    return "DATE_FORMAT({arguments})".format(arguments=','.join(args))

def to_date(*args):
    return "TO_DATE({arguments})".format(arguments=','.join(args))

def to_timestamp(*args):
    return "TO_TIMESTAMP({arguments})".format(arguments=','.join(args))

def date_add(*args):
    return "DATE_ADD({arguments})".format(arguments=','.join(args))

def date_sub(*args):
    return "DATE_SUB({arguments})".format(arguments=','.join(args))

def date_diff(*args):
    return "DATEDIFF({arguments})".format(arguments=','.join(args))

def from_unixtime(*args):
    return "FROM_UNIXTIME({arguments})".format(arguments=','.join(args))

# Works only in Spark>=3.5.0
def date_part(*args):
    return "DATE_PART({arguments})".format(arguments=','.join(args))
