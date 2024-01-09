import ply.yacc as yacc
from lexer import tokens  # Import the tokens from lexer.py
import json
import sys
import argparse

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
                   | function_declaration
                   | function_definition
                   | array_declaration'''
    p[0] = p[1]

# Variable Declarations
def p_var_declaration_1(p):
    '''var_declaration : type_specifier IDENTIFIER SEMICOLON
                          | type_specifier TIMES IDENTIFIER SEMICOLON'''
    if len(p) == 4:
        p[0] = ('var_declaration', p[1], p[2])
    else:
        p[0] = ('var_declaration', p[1], p[2], p[3])

def p_var_declaration_2(p):
    'var_declaration : type_specifier IDENTIFIER ASSIGN expression SEMICOLON'
    p[0] = ('var_declaration_init', p[1], p[2], p[4])

def p_array_declaration_1(p):
    'array_declaration : type_specifier IDENTIFIER LBRACKET expression RBRACKET SEMICOLON'
    p[0] = ('array_declaration', p[1], p[2], p[4])

def p_array_declaration_2(p):
    'array_declaration : type_specifier IDENTIFIER LBRACKET expression RBRACKET ASSIGN LBRACE array_list RBRACE SEMICOLON'
    p[0] = ('array_declaration_init', p[1], p[2], p[4], p[8])

def p_array_declaration_3(p):
    'array_declaration : type_specifier IDENTIFIER LBRACKET RBRACKET ASSIGN LBRACE array_list RBRACE SEMICOLON'
    p[0] = ('array_declaration_init', p[1], p[2], p[7])

def p_array_declaration_4(p):
    'array_declaration : type_specifier IDENTIFIER LBRACKET expression RBRACKET ASSIGN STRING_LITERAL SEMICOLON'
    p[0] = ('array_declaration_init', p[1], p[2], p[4], p[7])

def p_array_declaration_5(p):
    'array_declaration : type_specifier IDENTIFIER LBRACKET RBRACKET ASSIGN STRING_LITERAL SEMICOLON'
    p[0] = ('array_declaration_init', p[1], p[2], p[6])

def p_type_specifier(p):
    '''type_specifier : INT
                      | FLOAT
                      | CHAR
                      | VOID'''
    p[0] = p[1]

def p_array_list_1(p):
    'array_list : array_list COMMA expression'
    p[0] = p[1] + [p[3]]

def p_array_list_2(p):
    'array_list : expression'
    p[0] = [p[1]]

# Function Declarations and Definitions
def p_function_declaration(p):
    'function_declaration : type_specifier IDENTIFIER LPAREN param_list RPAREN SEMICOLON'
    p[0] = ('function_declaration', p[1], p[2], p[4])

def p_function_definition(p):
    'function_definition : type_specifier IDENTIFIER LPAREN param_list RPAREN compound_statement'
    p[0] = ('function_definition', p[1], p[2], p[4], p[6])

def p_param_list_1(p):
    'param_list : param_list COMMA param'
    p[0] = p[1] + [p[3]]

def p_param_list_2(p):
    'param_list : param'
    p[0] = [p[1]]

def p_param_list_empty(p):
    'param_list : empty'
    p[0] = []

def p_param_1(p):
    'param : type_specifier IDENTIFIER'
    p[0] = ('param', p[1], p[2])

def p_param_2(p):
    'param : type_specifier IDENTIFIER LBRACKET RBRACKET'
    p[0] = ('param', p[1], p[2], p[3], p[4])

def p_param_3(p):
    'param : type_specifier TIMES IDENTIFIER'
    p[0] = ('param', p[1], p[2], p[3])

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
                 | continue_statement
                 | break_statement
                 | var_declaration
                 | array_declaration
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

def p_assignment_expression_1(p):
    'assignment_expression : IDENTIFIER ASSIGN expression'
    p[0] = ('assignment_expression', p[1], p[3])

def p_assignment_expression_2(p):
    'assignment_expression : array_access ASSIGN expression'
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
                        | DEC IDENTIFIER
                        | IDENTIFIER INC
                        | IDENTIFIER DEC'''
    p[0] = ('unary_expression', p[1], p[2])

def p_term(p):
    '''term : IDENTIFIER
            | INT_LITERAL
            | FLOAT_LITERAL
            | CHAR_LITERAL
            | STRING_LITERAL
            | LPAREN expression RPAREN
            | function_call
            | array_access'''
    if len(p) == 2:
        # 对于单一元素的情况
        p[0] = ('term', p[1])
    elif len(p) == 4:
        # 对于括号内的表达式
        p[0] = ('paren_expression', p[2])

def p_function_call(p):
    'function_call : IDENTIFIER LPAREN argument_list RPAREN'
    p[0] = ('function_call', p[1], p[3])

def p_array_access(p):
    'array_access : IDENTIFIER LBRACKET expression RBRACKET'
    p[0] = ('array_access', p[1], p[3])

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
def p_selection_statement_1(p):
    'selection_statement : IF LPAREN expression RPAREN statement'
    p[0] = ('if_statement', p[3], p[5])

def p_selection_statement_2(p):
    'selection_statement : IF LPAREN expression RPAREN statement ELSE statement'
    p[0] = ('if_else_statement', p[3], p[5], p[7])

def p_iteration_statement(p):
    '''iteration_statement : WHILE LPAREN expression RPAREN statement
                           | FOR LPAREN expression_statement expression_statement expression RPAREN statement
                            | FOR LPAREN var_declaration expression_statement expression RPAREN statement'''
    if len(p) == 6:
        p[0] = ('while_statement', p[3], p[5])
    else:
        p[0] = ('for_statement', p[3], p[4], p[5], p[7])

def p_return_statement(p):
    'return_statement : RETURN expression SEMICOLON'
    p[0] = ('return_statement', p[2])

def p_continue_statement(p):
    'continue_statement : CONTINUE SEMICOLON'
    p[0] = ('continue_statement', p[1])

def p_break_statement(p):
    'break_statement : BREAK SEMICOLON'
    p[0] = ('break_statement', p[1])

# Build the parser
parser = yacc.yacc(start='program')

# Function to parse and return JSON
def parse_to_json(data):
    result = parser.parse(data)
    # print(result)
    return json.dumps(result, indent=4)

if __name__ == '__main__':
    # Create the parser
    arg_parser = argparse.ArgumentParser(description='Parse C code to JSON.')
    arg_parser.add_argument('-s', '--source', type=str, help='Path to the C source file')
    arg_parser.add_argument('-o', '--output', type=str, help='Path to the output JSON file')
    args = arg_parser.parse_args()

    if args.source:
        try:
            with open(args.source, 'r') as file:
                data = file.read()
        except FileNotFoundError:
            print(f"Error: File {args.source} not found.")
            sys.exit(1)
    else:
        # No file path provided; use default data
        data = '''
        int main() {
            int x;
            if (x > 5) {
                return x;
            }
            return 0;
        }
        '''
        # data = '''
        # int x = 10;
        # float y = 5.5;
        # char* str = "Hello";
        # if (x > 0) {
        #     x++;
        # }
        # '''
    # print(data)
    output = parse_to_json(data)

    if args.output:
        try:
            with open(args.output, 'w') as file:
                file.write(output)
        except FileNotFoundError:
            print(f"Error: File {args.output} not found.")
            sys.exit(1)
    else:
        print(output)
