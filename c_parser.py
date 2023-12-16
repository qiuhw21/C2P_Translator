import ply.yacc as yacc
from lexer import tokens  # Assuming you have a lexer file named 'lexer.py'
import json

precedence = (
    ('left', 'OR'),                  # Lowest precedence
    ('left', 'AND'),
    ('nonassoc', 'EQ', 'NEQ'),
    ('nonassoc', 'LT', 'LTE', 'GT', 'GTE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD'),
    ('right', 'UMINUS', 'NOT'),      # Highest precedence
)

# Utility function for parsing error
def p_error(p):
    print("Syntax error in input at token", p)

# Program structure
def p_program(p):
    'program : declaration_list'
    p[0] = ('program', p[1])

# Declarations
def p_declaration_list_1(p):
    'declaration_list : declaration_list declaration'
    p[0] = p[1] + [p[2]]

def p_declaration_list_2(p):
    'declaration_list : declaration'
    p[0] = [p[1]]

def p_declaration(p):
    '''declaration : var_declaration
                   | function_declaration'''
    p[0] = p[1]

# Variable Declarations
def p_var_declaration_1(p):
    'var_declaration : type_specifier IDENTIFIER SEMICOLON'
    p[0] = ('var_declaration', p[1], p[2])

def p_var_declaration_2(p):
    'var_declaration : type_specifier IDENTIFIER ASSIGN expression SEMICOLON'
    p[0] = ('var_declaration_init', p[1], p[2], p[4])

def p_type_specifier(p):
    '''type_specifier : INT
                      | FLOAT
                      | CHAR
                      | VOID'''
    p[0] = p[1]

# Function Declarations and Definitions
def p_function_declaration(p):
    'function_declaration : type_specifier IDENTIFIER LPAREN param_list RPAREN compound_statement'
    p[0] = ('function_declaration', p[1], p[2], p[4], p[6])

def p_param_list_1(p):
    'param_list : param_list COMMA param'
    p[0] = p[1] + [p[3]]

def p_param_list_2(p):
    'param_list : param'
    p[0] = [p[1]]

def p_param_list_empty(p):
    'param_list : empty'
    p[0] = []

def p_param(p):
    'param : type_specifier IDENTIFIER'
    p[0] = ('param', p[1], p[2])

def p_empty(p):
    'empty :'
    pass

def p_compound_statement(p):
    'compound_statement : LBRACE statement_list RBRACE'
    p[0] = ('compound_statement', p[2])

# Statements
def p_statement_list_1(p):
    'statement_list : statement_list statement'
    p[0] = p[1] + [p[2]]

def p_statement_list_2(p):
    'statement_list : statement'
    p[0] = [p[1]]

def p_statement(p):
    '''statement : expression_statement
                 | compound_statement
                 | selection_statement
                 | iteration_statement
                 | return_statement
                 | var_declaration
                 | empty'''
    p[0] = p[1]

# Expressions
def p_expression_statement(p):
    'expression_statement : expression SEMICOLON'
    p[0] = ('expression_statement', p[1])

def p_expression(p):
    '''expression : assignment_expression
                  | binary_expression
                  | unary_expression
                  | term'''
    p[0] = p[1]

def p_assignment_expression(p):
    'assignment_expression : IDENTIFIER ASSIGN expression'
    p[0] = ('assignment_expression', p[1], p[3])

def p_binary_expression(p):
    '''binary_expression : expression PLUS expression
                         | expression MINUS expression
                         | expression TIMES expression
                         | expression DIVIDE expression
                         | expression MOD expression
                         | expression EQ expression
                         | expression NEQ expression
                         | expression LT expression
                         | expression GT expression
                         | expression LTE expression
                         | expression GTE expression
                         | expression AND expression
                         | expression OR expression'''
    p[0] = ('binary_expression', p[2], p[1], p[3])

def p_unary_expression(p):
    '''unary_expression : MINUS expression %prec UMINUS
                        | NOT expression
                        | INC IDENTIFIER
                        | DEC IDENTIFIER'''
    p[0] = ('unary_expression', p[1], p[2])

def p_term(p):
    '''term : IDENTIFIER
            | INT_LITERAL
            | LPAREN expression RPAREN
            | function_call'''
    p[0] = ('term', p[1])

def p_function_call(p):
    'function_call : IDENTIFIER LPAREN argument_list RPAREN'
    p[0] = ('function_call', p[1], p[3])

def p_argument_list(p):
    '''argument_list : argument_list COMMA expression
                     | expression
                     | empty'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    elif len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = []

# Control Structures
def p_selection_statement(p):
    '''selection_statement : IF LPAREN expression RPAREN compound_statement
                           | IF LPAREN expression RPAREN compound_statement ELSE compound_statement'''
    if len(p) == 6:
        p[0] = ('if_statement', p[3], p[5])
    else:
        p[0] = ('if_else_statement', p[3], p[5], p[7])

def p_iteration_statement(p):
    '''iteration_statement : WHILE LPAREN expression RPAREN statement
                           | FOR LPAREN expression_statement expression_statement expression RPAREN statement'''
    if len(p) == 6:
        p[0] = ('while_statement', p[3], p[5])
    else:
        p[0] = ('for_statement', p[3], p[4], p[5], p[7])

def p_return_statement(p):
    'return_statement : RETURN expression SEMICOLON'
    p[0] = ('return_statement', p[2])

# Build the parser
parser = yacc.yacc(start='program')

# Function to parse and return JSON
def parse_to_json(data):
    result = parser.parse(data)
    print(result)
    return json.dumps(result, indent=4)

# Example usage
input_data = '''
int main() {
    int x;
    if (x > 5) {
        return x;
    }
    return 0;
}
'''
ast = parse_to_json(input_data)
print(ast)
