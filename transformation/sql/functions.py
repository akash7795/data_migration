import importlib

FUNCTION_MAP = {
    'ADD'    : 'data_migration.transformation.sql.numeric_functions.add',
    'SUBTRACT' : 'data_migration.transformation.sql.numeric_functions.subtract',
    'MULTIPLY' : 'data_migration.transformation.sql.numeric_functions.multiply',
    'DIVIDE' : 'data_migration.transformation.sql.numeric_functions.divide',
    'ABS' : 'data_migration.transformation.sql.numeric_functions.abs',
    'CEIL' : 'data_migration.transformation.sql.numeric_functions.ceil',
    'FLOOR' : 'data_migration.transformation.sql.numeric_functions.floor',
    'CONCAT' : 'data_migration.transformation.sql.string_functions.concat',
    'UPPER'  : 'data_migration.transformation.sql.string_functions.upper',
    'LOWER': 'data_migration.transformation.sql.string_functions.lower',
    'LENGTH': 'data_migration.transformation.sql.string_functions.strlen',
    'RTRIM': 'data_migration.transformation.sql.string_functions.Rtrim',
    'LTRIM': 'data_migration.transformation.sql.string_functions.ltrim',
    'CONCAT_WS': 'data_migration.transformation.sql.string_functions.concat_ws',
}

def get_function(function):
    function_path = FUNCTION_MAP[function.upper()]
    module_name, function_name = function_path.rsplit('.', 1)
    module = importlib.import_module(module_name)
    func = getattr(module, function_name)
    return func
