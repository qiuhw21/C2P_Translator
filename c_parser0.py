import ply.yacc as yacc
import json

from lexer import tokens

# Utility function for parsing error
def p_error(p):
    print("Syntax error in input at token", p)

# Program structure
def p_program(p):
    'program : statement_list'
    p[0] = ('program', p[1])

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + (p[2],)
    else:
        p[0] = (p[1],)

def p_statement(p):
    '''statement : var_declaration
                 | function_declaration
                 | expression_statement'''
    p[0] = p[1]

# Variable declarations
def p_var_declaration(p):
    '''var_declaration : type_specifier IDENTIFIER SEMICOLON
                       | type_specifier IDENTIFIER EQUALS expression SEMICOLON'''
    if len(p) == 4:
        p[0] = ('var_declaration', p[1], p[2])
    else:
        p[0] = ('var_declaration_init', p[1], p[2], p[4])


def p_type_specifier(p):
    '''type_specifier : INT
                      | FLOAT
                      | CHAR
                      | BOOL
                      | DOUBLE'''
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

def p_empty(p):
    'empty :'
    pass

# Compound statement (used in functions, loops, etc.)
def p_compound_statement(p):
    'compound_statement : LBRACE statement_list RBRACE'
    p[0] = ('compound_statement', p[2])

# Expression statements (like 'x = 5;')
def p_expression_statement(p):
    'expression_statement : expression SEMICOLON'
    p[0] = ('expression_statement', p[1])

# Expressions (like 'x + y', 'x = y', etc.)
def p_expression(p):
    '''expression : assignment_expression
                  | binary_expression
                  | term'''
    p[0] = p[1]

def p_binary_expression(p):
    '''binary_expression : expression PLUS expression
                         | expression MINUS expression
                         | expression TIMES expression
                         | expression DIVIDE expression
                         | expression MOD expression
                         | expression AND expression
                         | expression OR expression
                         | expression LESS expression
                         | expression LESSEQUAL expression
                         | expression GREATER expression
                         | expression GREATEREQUAL expression
                         | expression DOUBLEEQUAL expression
                         | expression NOTEQUAL expression'''
    p[0] = ('binary_expression', p[1], p[2], p[3])

# Assignment expressions (like 'x = y')
def p_assignment_expression(p):
    'assignment_expression : IDENTIFIER EQUALS expression'
    p[0] = ('assignment_expression', p[1], p[3])

# In the lexer
tokens += ('CHAR_LITERAL', 'BOOL_LITERAL')

# Add regular expressions for these literals in the lexer
def t_CHAR_LITERAL(t):
    r"'.'"
    return t

def t_BOOL_LITERAL(t):
    r'true|false'
    return t

# In the parser, handle these new literals in the `term` rule
def p_term(p):
    '''term : IDENTIFIER
            | NUMBER
            | FLOAT_NUMBER
            | CHAR_LITERAL
            | BOOL_LITERAL
            | LPAREN expression RPAREN'''
    p[0] = ('term', p[1])


# Build the parser
parser = yacc.yacc(start='program')

# Function to parse and return JSON
def parse_to_json(data):
    result = parser.parse(data)
    return json.dumps(result, indent=4)

if __name__ == '__main__':

    # Test input for declaration
    data_declaration = 'int x;'
    result = parser.parse(data_declaration)
    print("Declaration Test:", result)

    # Test input for assignment
    data_assignment = 'x = 5;'
    result = parser.parse(data_assignment)
    print("Assignment Test:", result)

    data = '''
    int x = 10;
    char y = 'a';
    bool flag = true;
    if (x > 0) {
        x++;
    }
    '''

    # Parse
    print("\nParsed tree:")
    json_result = parse_to_json(data)
    print(json_result)
