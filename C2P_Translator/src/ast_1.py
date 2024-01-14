def process_declaration_list(declaration_list):
    for declaration in declaration_list:
        process_declaration(declaration)

def process_declaration(declaration):
    declaration_type = declaration[0]
    if declaration_type == 'var_declaration':
        process_variable_declaration(declaration)
    elif declaration_type == 'function_declaration':
        process_function_declaration(declaration)
    elif declaration_type == 'function_definition':
        process_function_definition(declaration)
    elif declaration_type == 'array_declaration':
        process_array_declaration(declaration)
    # Add more cases for other declaration types as needed...

def process_variable_declaration(declaration):
    _, type_specifier, *rest = declaration
    identifier = rest[0]
    if len(rest) == 2:  # Variable declaration without initialization
        print(f"Variable Declaration: {type_specifier} {identifier};")
    elif len(rest) == 3:  # Variable declaration with initialization
        expression = rest[2]
        print(f"Variable Declaration: {type_specifier} {identifier} = {expression};")

def process_array_declaration(declaration):
    _, type_specifier, identifier, *rest = declaration
    if len(rest) == 1:  # Array declaration without initialization
        size = rest[0]
        print(f"Array Declaration: {type_specifier} {identifier}[{size}];")
    elif len(rest) == 2:  # Array declaration with initialization
        size, array_list = rest
        print(f"Array Declaration: {type_specifier} {identifier}[{size}] = {array_list};")

def process_function_declaration(declaration):
    _, type_specifier, identifier, param_list = declaration
    print(f"Function Declaration: {type_specifier} {identifier}({param_list});")

def process_function_definition(declaration):
    _, type_specifier, identifier, param_list, compound_statement = declaration
    print(f"Function Definition: {type_specifier} {identifier}({param_list}) {compound_statement};")
    process_compound_statement(compound_statement)

def process_param_list(param_list):
    for param in param_list:
        process_param(param)

def process_param(param):
    type_specifier, *rest = param
    if len(rest) == 1:  # Regular parameter
        identifier = rest[0]
        print(f"Parameter: {type_specifier} {identifier}")
    elif len(rest) == 4:  # Array parameter
        _, type_specifier, identifier, _ = rest
        print(f"Parameter: {type_specifier} {identifier}[]")
    elif len(rest) == 3:  # Pointer parameter
        _, type_specifier, identifier = rest
        print(f"Parameter: {type_specifier}* {identifier}")

# Similar functions can be added for other declaration types...

def process_compound_statement(compound_statement):
    _, statement_list = compound_statement
    print("Compound Statement:")
    process_statement_list(statement_list)

# You can continue adding functions for processing other parts of the AST

def process_statement_list(statement_list):
    for statement in statement_list:
        process_statement(statement)

def process_statement(statement):
    statement_type = statement[0]
    if statement_type == 'expression_statement':
        process_expression_statement(statement)
    elif statement_type == 'compound_statement':
        process_compound_statement(statement)
    # Add more cases for other statement types as needed...

def process_expression_statement(expression_statement):
    _, expression = expression_statement
    print(f"Expression Statement: {expression};")

