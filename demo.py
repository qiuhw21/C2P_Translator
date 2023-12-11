import ply.lex as lex
import ply.yacc as yacc

# ---- Lexer part ----

# List of token names
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'SEMICOLON',
    'ID',
    'EQUALS',
    'INT'
)

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_EQUALS = r'='
t_INT = r'int'

# Identifiers and reserved words
reserved = {
    'int': 'INT'
}

# Regular expressions with some action code
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')    # Check for reserved words
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# ---- Parser part ----

# Parsing rules

def p_statement_decl(p):
    'statement : INT ID SEMICOLON'
    p[0] = ('declare-int', p[2])

def p_statement_assign(p):
    'statement : ID EQUALS expression SEMICOLON'
    p[0] = ('assign', p[1], p[3])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = ('number', p[1])

def p_expression_id(p):
    'expression : ID'
    p[0] = ('identifier', p[1])

def p_error(p):
    print("Syntax error in input!")

# Add a new top-level rule to handle multiple statements
def p_program(p):
    '''program : program statement
               | statement'''
    if len(p) == 3:
        p[0] = (p[1], p[2])
    else:
        p[0] = (p[1],)

# Build the parser
parser = yacc.yacc(start='program')


# ---- Testing the Lexer and Parser ----

data = '''
int x;
x = 5 + 3;
'''

# Give the lexer input
lexer.input(data)

# Tokenize
print("Tokens:")
while True:
    tok = lexer.token()
    if not tok: 
        break
    print(tok)

# Parse
print("\nParsed tree:")
result = parser.parse(data)
print(result)
