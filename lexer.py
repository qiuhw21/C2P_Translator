import ply.lex as lex

# Dictionary of reserved keywords
reserved = {
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'void': 'VOID',
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'return': 'RETURN',
    # ... add other reserved keywords here ...
    'break': 'BREAK',
    'continue': 'CONTINUE',
}

# List of token names including the reserved keywords
tokens = [
    'IDENTIFIER', 'INT_LITERAL', 'FLOAT_LITERAL', 'STRING_LITERAL', 'CHAR_LITERAL',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD', 'ASSIGN',
    'EQ', 'NEQ', 'LT', 'GT', 'LTE', 'GTE',
    'AND', 'OR', 'NOT', 'INC', 'DEC',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET',
    'SEMICOLON', 'COMMA',
    'COMMENT_SINGLE', 'COMMENT_MULTI'
] + list(reserved.values())

# Regular expressions for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_ASSIGN = r'='
t_EQ = r'=='
t_NEQ = r'!='
t_LT = r'<'
t_GT = r'>'
t_LTE = r'<='
t_GTE = r'>='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_INC = r'\+\+'
t_DEC = r'--'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_SEMICOLON = r';'
t_COMMA = r','

def t_INT_LITERAL(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FLOAT_LITERAL(t):
    r'\d+\.\d*'
    t.value = float(t.value)
    return t

def t_STRING_LITERAL(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t

def t_CHAR_LITERAL(t):
    r"\'([^\\\n]|(\\.))*?\'"
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Check for reserved words
    return t

def t_COMMENT_SINGLE(t):
    r'//.*'
    pass  # Token discarded

def t_COMMENT_MULTI(t):
    r'/\*(.|\n)*?\*/'
    pass  # Token discarded

# Ignored characters (whitespace)
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Function to output token stream
def get_token_stream(data):
    lexer.input(data)
    token_stream = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        token_stream.append({
            'value': tok.value,
            'type': tok.type,
            'line': tok.lineno,
            'position': tok.lexpos
        })
    return token_stream

# Test input
if __name__ == '__main__':
    # data = '''
    # int x = 10;
    # char y = 'a';
    # bool flag = true;
    # if (x > 0) {
    #     x++;
    # }
    # '''

    data = '''
    int x = 10;
    float y = 5.5;
    char* str = "Hello";
    if (x > 0) {
        x++;
    }
    '''
    output = get_token_stream(data)
    for token in output:
        print(token)

    # with open('./tests/sort.c', 'r') as f:
    #     data = f.read()
    #     output = get_token_stream(data)
    #     for token in output:
    #         print(token)

