# C2P_Translator

本项目是一个C语言到Python的翻译器，将支持C语言的子集，能够将简单的C语言程序翻译成Python程序。

以下是预计支持的语言特性：

## Grammar

### Data Types
- Basic types: `int`, `float`, `char`, `void`
- Arrays (optional, but useful for many problems)

### Variables and Expressions
- Variable declaration and initialization (e.g., `int x;`, `int x = 10;`)
- Arithmetic operations (e.g., `+`, `-`, `*`, `/`, `%`)
- Logical operations (e.g., `&&`, `||`, `!`)
- Comparison operations (e.g., `==`, `!=`, `<`, `>`, `<=`, `>=`)
- Assignment (e.g., `=`)

### Control Structures
- Conditional statements: `if`, `else`
- Loops: `for`, `while`
- (Optional) `break` and `continue` for loop control

### Functions
- Function declaration and definition
- Function calls
- Return statements

### Input/Output
- Basic I/O functions (e.g., `printf`, `scanf`) for interaction

### Comments
- Single-line (`//`) and multi-line (`/* ... */`) comments

### Grammar Representation

Here's how these elements translate into grammar rules for a parser:

1. **Program Structure**: 
   - `program : declaration_list`

2. **Declarations**:
   - `declaration_list : declaration_list declaration | declaration`
   - `declaration : var_declaration | function_declaration`

3. **Variable Declarations**:
   - `var_declaration : type_specifier IDENTIFIER SEMICOLON | type_specifier IDENTIFIER ASSIGN expression SEMICOLON`
   - `type_specifier : INT | FLOAT | CHAR | VOID`

4. **Function Declarations and Definitions**:
   - `function_declaration : type_specifier IDENTIFIER LPAREN param_list RPAREN compound_statement`
   - `param_list : param_list COMMA param | param | empty`
   - `param : type_specifier IDENTIFIER`
   - `compound_statement : LBRACE statement_list RBRACE`

5. **Statements**:
   - `statement_list : statement_list statement | statement`
   - `statement : expression_statement | compound_statement | selection_statement | iteration_statement | return_statement`

6. **Expressions**:
   - `expression_statement : expression SEMICOLON`
   - `expression : assignment_expression | binary_expression | term`
   - `assignment_expression : IDENTIFIER ASSIGN expression`
   - `binary_expression : expression PLUS expression | expression MINUS expression | ... (other binary operations)`
   - `term : IDENTIFIER | NUMBER | LPAREN expression RPAREN`

7. **Control Structures**:
   - `selection_statement : IF LPAREN expression RPAREN statement | IF LPAREN expression RPAREN statement ELSE statement`
   - `iteration_statement : WHILE LPAREN expression RPAREN statement | FOR LPAREN expression_statement expression_statement expression RPAREN statement`
   - `return_statement : RETURN expression SEMICOLON`

8. **Input/Output** (treated as part of expressions or statements depending on the implementation)
