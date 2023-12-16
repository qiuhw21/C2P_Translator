# C2P_Translator 项目文档

## 项目概述
C2P_Translator 是一个旨在将 C 语言代码翻译成 Python 代码的工具。本项目聚焦于实现 C 语言的一个子集，支持基础的数据类型、变量声明、表达式、控制结构、函数以及输入/输出等核心特性。

### 小组成员与分工
- **邱皓炜**: 语义处理的实现，对抽象语法树进行语义分析，将其转化为 Python 代码。
- **童新荷**: 格式处理的实现，对转化出来的代码进行格式化，编写测试代码。
- **刘博非**: 词法分析、语法分析的实现，构建出抽象语法树。

### 开发进程
- **第一次提交**: 完成了词法分析器，可以识别 C 语言的关键字、标识符、常量、运算符和界符。

### 预计支持的语言特性

#### 数据类型
- 基本类型: `int`, `float`, `char`, `void`
- 数组（可选，但对于许多问题非常有用）

#### 变量和表达式
- 变量声明和初始化（例如：`int x;`, `int x = 10;`）
- 算术运算（例如：`+`, `-`, `*`, `/`, `%`）
- 逻辑运算（例如：`&&`, `||`, `!`）
- 比较运算（例如：`==`, `!=`, `<`, `>`, `<=`, `>=`）
- 赋值（例如：`=`）

#### 控制结构
- 条件语句：`if`, `else`
- 循环：`for`, `while`
- （可选）循环控制的 `break` 和 `continue`

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
   - `declaration : var_declaration | function_declaration`

3. **变量声明**:
   - `var_declaration : type_specifier IDENTIFIER SEMICOLON | type_specifier IDENTIFIER ASSIGN expression SEMICOLON`
   - `type_specifier : INT | FLOAT | CHAR | VOID`

4. **函数声明和定义**:
   - `function_declaration : type_specifier IDENTIFIER LPAREN param_list RPAREN compound_statement`
   - `param_list : param_list COMMA param | param | empty`
   - `param : type_specifier IDENTIFIER`
   - `compound_statement : LBRACE statement_list RBRACE`

5. **语句**:
   - `statement_list : statement_list statement | statement`
   - `statement : expression_statement | compound_statement | selection_statement | iteration_statement | return_statement`

6. **表达式**:
   - `expression_statement : expression SEMICOLON`
   - `expression : assignment_expression | binary_expression | term`
   - `assignment_expression : IDENTIFIER ASSIGN expression`
   - `binary_expression : expression PLUS expression | expression MINUS expression | ... (其他二元运算)`
   - `term : IDENTIFIER | NUMBER | LPAREN expression RPAREN`

7. **控制结构**:
   - `selection_statement : IF LPAREN expression RPAREN statement | IF LPAREN expression RPAREN statement ELSE statement`
   - `iteration_statement : WHILE LPAREN expression RPAREN statement | FOR LPAREN expression_statement expression_statement expression RPAREN statement`
   - `return_statement : RETURN expression SEMICOLON`

8. **输入/输出**（根据实现可能作为表达式或语句的一部分处理）
