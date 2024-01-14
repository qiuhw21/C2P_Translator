# C2P_Translator 项目文档

## 项目概述
C2P_Translator 是一个旨在将 C 语言代码翻译成 Python 代码的工具。本项目聚焦于实现 C 语言的一个子集，支持基础的数据类型、变量声明、表达式、控制结构、函数以及输入/输出等核心特性。

### 小组成员与分工
- **邱皓炜**: 语义处理的实现，对抽象语法树进行语义分析，将其转化为 Python 代码。
- **童新荷**: 格式处理的实现，对转化出来的代码进行格式化，优化测试代码，预处理，后处理。
- **刘博非**: 词法分析、语法分析的实现，构建出抽象语法树，编写测试代码。

### 开发进程
- **第一次提交**: 完成了词法分析器，可以识别 C 语言的关键字、标识符、常量、运算符和界符。
- **第二次提交**: 完成了语法分析器，可以将 C 语言的代码转化为抽象语法树。
- **第三次提交**: 完成了语义处理，可以遍历语法分析树并在叶子节点处理输出。完成了格式化处理，添加了缩进，预处理，主函数添加，并对某些特定函数进行了专门的翻译处理。

### 预计支持的语言特性

#### 数据类型
- 基本类型: `int`, `float`, `char`, `void`
- 数组
- 字符串，以 `char` 数组的形式表示
- 为了简化实现，暂不支持指针、结构体、联合体等复杂类型

#### 变量和表达式
- 变量声明和初始化（例如：`int x;`, `int x = 10;`，注意一次只能声明一个变量）
- 算术运算（例如：`+`, `-`, `*`, `/`, `%`）
- 逻辑运算（例如：`&&`, `||`, `!`）
- 比较运算（例如：`==`, `!=`, `<`, `>`, `<=`, `>=`）
- 赋值（例如：`=`）

#### 控制结构
- 条件语句：`if`, `else`, `else if`
- 循环：`for`, `while`
- 循环控制的 `break` 和 `continue`

#### 函数
- 函数声明和定义
- 函数调用
- 返回语句

#### 输入/输出
- 基本的输入输出函数（例如：`printf`, `scanf`）

#### 注释
- 单行注释（`//`）和多行注释（`/* ... */`）

#### 语法规则表示

以下是这些元素如何转化为解析器的语法规则：

1. **程序结构**:
   - `program : declaration_list`

2. **声明**:
   - `declaration_list : declaration_list declaration | declaration`
   - `declaration : var_declaration | function_declaration | array_declaration`

3. **变量声明**:
   - `var_declaration : type_specifier IDENTIFIER SEMICOLON | type_specifier IDENTIFIER ASSIGN expression SEMICOLON`
   - `array_declaration : type_specifier IDENTIFIER LBRACKET INT_LITERAL RBRACKET SEMICOLON | type_specifier IDENTIFIER LBRACKET INT_LITERAL RBRACKET ASSIGN LBRACE array_list RBRACE SEMICOLON | type_specifier IDENTIFIER LBRACKET RBRACKET ASSIGN LBRACE array_list RBRACE SEMICOLON`
   - `type_specifier : INT | FLOAT | CHAR | VOID`
   - `array_list : array_list COMMA expression | expression`

4. **函数声明和定义**:
   - `function_declaration : type_specifier IDENTIFIER LPAREN param_list RPAREN compound_statement`
   - `param_list : param_list COMMA param | param | empty`
   - `param : type_specifier IDENTIFIER | type_specifier IDENTIFIER LBRACKET RBRACKET`
   - `compound_statement : LBRACE statement_list RBRACE`

5. **语句**:
   - `statement_list : statement_list statement | statement`
   - `statement : expression_statement | compound_statement | selection_statement | iteration_statement | return_statement | continue_statement | break_statement | var_declaration | array_declaration | empty`

6. **表达式**:
   - `expression_statement : expression SEMICOLON`
   - `expression : assignment_expression | binary_expression | unary_expression | term`
   - `assignment_expression : IDENTIFIER ASSIGN expression | array_access ASSIGN expression`
   - `binary_expression : expression PLUS expression | expression MINUS expression | ... (其他二元运算)`
   - `unary_expression : MINUS term | PLUS term | ... (其他一元运算)`
   - `term : IDENTIFIER | INT_LITERAL | FLOAT_LITERAL | STRING_LITERAL | LPAREN expression RPAREN | function_call | array_access`
   - `function_call : IDENTIFIER LPAREN argument_list RPAREN`
   - `array_access : IDENTIFIER LBRACKET expression RBRACKET`
   - `argument_list : argument_list COMMA expression | expression`

7. **控制结构**:
   - `selection_statement : IF LPAREN expression RPAREN statement | IF LPAREN expression RPAREN statement ELSE statement`
   - `iteration_statement : WHILE LPAREN expression RPAREN statement | FOR LPAREN expression_statement expression_statement expression RPAREN statement`
   - `return_statement : RETURN expression SEMICOLON`
   - `continue_statement : CONTINUE SEMICOLON`
   - `break_statement : BREAK SEMICOLON`

8. **输入/输出**（根据实现可能作为表达式或语句的一部分处理）

#### 注意事项
- **数组访问** (`array_access`) 被包含在表达式中，允许数组元素的读写。

## 项目实现

### 词法分析

词法分析使用了 `lex` 工具，将 C 语言的代码转化为 token 流。在`lexer.py`中，定义了词法分析器的规则，包括关键字、标识符、常量、运算符和界符。

### 语法分析

语法分析使用了 `yacc` 工具，将 token 流转化为抽象语法树。在`c_parser.py`中，定义了语法分析器的规则，包括程序结构、声明、变量和表达式、控制结构、函数、输入/输出等。

在实现语法分析时，遇到了一些自己写代码时没有注意到语法细节，例如变量的赋值属于表达式，而变量的声明属于语句，数组访问属于表达式，数组声明属于语句等。这些细节在实现时需要注意。

### 语义处理

语义处理对输入代码经过词法分析、语法分析生成的语法分析树进行深度优先遍历，然后在叶子节点对当前叶子元素进行输出，具体地，将其放入一个全局字符串数组。最后在根节点处理函数中返回该数组。

### 格式化处理

格式化处理对语义处理过程进行改进，在某些需要添加缩进的输出前添加一个"\t"，然后在需要换行的地方添加一个"\n"，例如：if expression:之后需要添加"\n\t"，但是过程中遇到一些问题，一些语句前不止添加一个"\t"，例如if语句嵌套，那么需要额外添加一个变量记录当前缩进量。除此之外，还对最初输入的c代码进行预处理，处理方式是单纯地将头文件声明以及宏定义去除，因为需要实现的四个测例并不需要python进行任何额外声明，因此这里简单化处理。最后还需要将生成的python代码最后加入main函数的调用。

