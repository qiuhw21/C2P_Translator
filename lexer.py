import ply.lex as lex
import ply.yacc as yacc

# List of token names. This includes C++ language tokens like keywords, operators, and different types of literals.
keywords = {
    'int': 'INT',
    'float': 'FLOAT',
    'double': 'DOUBLE',
    'return': 'RETURN',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'void': 'VOID',
    'char': 'CHAR',
    'unsigned': 'UNSIGNED',
    'signed': 'SIGNED',
    'long': 'LONG',
    'short': 'SHORT',
    'bool': 'BOOL',
    'const': 'CONST',
    'static': 'STATIC',
    # ... more C++ keywords
}

tokens = [
    'IDENTIFIER', 'NUMBER', 'FLOAT_NUMBER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET',
    'SEMICOLON', 'COMMA', 'QUOTE', 'APOSTROPHE',
    'EQUALS', 'PLUSEQUAL', 'MINUSEQUAL', 'TIMESEQUAL', 'DIVEQUAL', 'MODEQUAL',
    'LESS', 'LESSEQUAL', 'GREATER', 'GREATEREQUAL',
    'DOUBLEEQUAL', 'NOTEQUAL',
    'AND', 'OR', 'NOT', 'XOR', 'BITAND', 'BITOR', 'BITNOT', 'BITXOR',
    'SHIFTLEFT', 'SHIFTRIGHT',
    'INCREMENT', 'DECREMENT',
    'STRING_LITERAL', 'CHAR_LITERAL',
    # ... more C++ token types
] + list(keywords.values())

# Regular expression rules for simple tokens
t_PLUS       = r'\+'
t_MINUS      = r'-'
t_TIMES      = r'\*'
t_DIVIDE     = r'/'
t_MOD        = r'%'
t_LPAREN     = r'\('
t_RPAREN     = r'\)'
t_LBRACE     = r'\{'
t_RBRACE     = r'\}'
t_LBRACKET   = r'\['
t_RBRACKET   = r'\]'
t_SEMICOLON  = r';'
t_COMMA      = r','
t_QUOTE      = r'"'
t_APOSTROPHE = r'\''

t_EQUALS        = r'='
t_PLUSEQUAL     = r'\+='
t_MINUSEQUAL    = r'-='
t_TIMESEQUAL    = r'\*='
t_DIVEQUAL      = r'/='
t_MODEQUAL      = r'%='

t_LESS          = r'<'
t_LESSEQUAL     = r'<='
t_GREATER       = r'>'
t_GREATEREQUAL  = r'>='

t_DOUBLEEQUAL   = r'=='
t_NOTEQUAL      = r'!='

t_AND           = r'&&'
t_OR            = r'\|\|'
t_NOT           = r'!'
t_XOR           = r'\^'

t_BITAND        = r'&'
t_BITOR         = r'\|'
t_BITNOT        = r'~'
t_BITXOR        = r'\^'

t_SHIFTLEFT     = r'<<'
t_SHIFTRIGHT    = r'>>'

t_INCREMENT     = r'\+\+'
t_DECREMENT     = r'--'

# Regular expressions for complex tokens
def t_FLOAT_NUMBER(t):
    r'\d+\.\d*'
    t.value = float(t.value)
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value, 'IDENTIFIER')  # Check for C++ keywords
    return t

def t_STRING_LITERAL(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = str(t.value)
    return t

def t_CHAR_LITERAL(t):
    r"\'([^\\\n]|(\\.))*?\'"
    t.value = str(t.value)
    return t

# Ignored characters (spaces, tabs)
t_ignore  = ' \t'

# Track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test input
data = '''
int x;
x = 5;
'''

data = '''
int x = 10;
char y = 'a';
bool flag = true;
if (x > 0) {
    x++;
}
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
