from lexer import tokens

# Utility function for parsing error
def p_error(p):
    print("Syntax error in input at token", p)

# Placeholder function for empty productions
def p_empty(p):
    'empty :'
    pass

# Program structure
def p_program(p):
    'program : declaration_list'
    p[0] = ('program', p[1])

def p_declaration_list(p):
    '''declaration_list : declaration_list declaration
                        | declaration'''
    if len(p) == 3:
        p[0] = p[1] + (p[2],)
    else:
        p[0] = (p[1],)

def p_declaration(p):
    '''declaration : var_declaration
                   | function_declaration'''
                #    | class_declaration
                #    | ...'''  # Add more declaration types
    p[0] = p[1]

# Variable declarations
def p_var_declaration(p):
    'var_declaration : type_specifier IDENTIFIER SEMICOLON'
    p[0] = ('var_declaration', p[1], p[2])

def p_type_specifier(p):
    '''type_specifier : INT
                      | FLOAT
                      | CHAR
                      | BOOL'''
                    #   | ...'''  # Add more types
    p[0] = p[1]

# Function declarations
def p_function_declaration(p):
    'function_declaration : type_specifier IDENTIFIER LPAREN param_list RPAREN compound_statement'
    p[0] = ('function_declaration', p[1], p[2], p[4], p[6])

def p_param_list(p):
    '''param_list : param_list COMMA param
                  | param
                  | empty'''
    if len(p) == 4:
        p[0] = p[1] + (p[3],)
    elif len(p) == 2:
        p[0] = (p[1],) if p[1] is not None else ()
    else:
        p[0] = ()

def p_param(p):
    'param : type_specifier IDENTIFIER'
    p[0] = ('param', p[1], p[2])

# Compound statement (used in functions, loops, etc.)
def p_compound_statement(p):
    'compound_statement : LBRACE statement_list RBRACE'
    p[0] = ('compound_statement', p[2])

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | empty'''
    if len(p) == 3:
        p[0] = p[1] + (p[2],)
    else:
        p[0] = ()

# Define more statement types (expression, conditional, loop, etc.)
def p_statement(p):
    '''statement : expression_statement
                 | compound_statement
                 | selection_statement
                 | iteration_statement
                 | return_statement'''
    p[0] = p[1]

# Expression statements (like 'x = 5;')
def p_expression_statement(p):
    'expression_statement : expression SEMICOLON'
    p[0] = ('expression_statement', p[1])

# Expressions (like 'x + y', 'x = y', etc.)
def p_expression(p):
    '''expression : assignment_expression
                  | binary_expression
                  | term'''  # Example for additional expression types
    p[0] = p[1]

def p_binary_expression(p):
    '''binary_expression : expression PLUS expression
                         | expression MINUS expression
                         | expression TIMES expression
                         | expression DIVIDE expression'''
    p[0] = ('binary_expression', p[1], p[2], p[3])

def p_term(p):
    '''term : IDENTIFIER
            | NUMBER'''
    p[0] = ('term', p[1])

# Assignment expressions (like 'x = y')
def p_assignment_expression(p):
    'assignment_expression : IDENTIFIER EQUALS expression'
    p[0] = ('assignment_expression', p[1], p[3])

# Selection statements (like 'if' and 'if-else')
def p_selection_statement(p):
    '''selection_statement : IF LPAREN expression RPAREN statement
                           | IF LPAREN expression RPAREN statement ELSE statement'''
    if len(p) == 6:
        p[0] = ('selection_statement', p[3], p[5])
    else:
        p[0] = ('selection_statement', p[3], p[5], p[7])

# Iteration statements (like 'while' and 'for')
def p_iteration_statement(p):
    '''iteration_statement : WHILE LPAREN expression RPAREN statement
                           | FOR LPAREN expression_statement expression_statement expression RPAREN statement'''
    if len(p) == 6:
        p[0] = ('iteration_statement', p[3], p[5])
    else:
        p[0] = ('iteration_statement', p[3], p[4], p[5], p[7])

# Return statements
def p_return_statement(p):
    '''return_statement : RETURN SEMICOLON
                        | RETURN expression SEMICOLON'''
    if len(p) == 3:
        p[0] = ('return_statement',)
    else:
        p[0] = ('return_statement', p[2])


parser = yacc.yacc(start='program')


# Test input for declaration
data_declaration = 'int x;'
result = parser.parse(data_declaration)
print("Declaration Test:", result)

# Test input for assignment
data_assignment = 'x = 5;'
result = parser.parse(data_assignment)
print("Assignment Test:", result)

# Parse
print("\nParsed tree:")
result = parser.parse(data)
print(result)
