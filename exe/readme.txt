# Instruction

## 运行方式

### 环境要求
- Python 3.8+
- PLY (Python Lex-Yacc)

### 运行指南
1. 确保已安装Python 3.8，并且安装了PLY库。
2. 在命令行或终端中，切换到项目所在目录。
3. 运行命令 `python lexer.py -s <source_file>`，其中`<source_file>`为待分析的源代码文件，如不指定则默认为一段测试代码。

### 运行结果

#### 1. 测试代码
```
int x = 10;
float y = 5.5;
char* str = "Hello";
if (x > 0) {
    x++;
}
```
运行结果：
```
> python lexer.py
{'value': 'int', 'type': 'INT', 'line': 2, 'position': 9}
{'value': 'x', 'type': 'IDENTIFIER', 'line': 2, 'position': 13}
{'value': '=', 'type': 'ASSIGN', 'line': 2, 'position': 15}
{'value': 10, 'type': 'INT_LITERAL', 'line': 2, 'position': 17}
{'value': ';', 'type': 'SEMICOLON', 'line': 2, 'position': 19}
{'value': 'float', 'type': 'FLOAT', 'line': 3, 'position': 29}
{'value': 'y', 'type': 'IDENTIFIER', 'line': 3, 'position': 35}
{'value': '=', 'type': 'ASSIGN', 'line': 3, 'position': 37}
{'value': 5.5, 'type': 'FLOAT_LITERAL', 'line': 3, 'position': 39}
{'value': ';', 'type': 'SEMICOLON', 'line': 3, 'position': 42}
{'value': 'char', 'type': 'CHAR', 'line': 4, 'position': 52}
{'value': '*', 'type': 'TIMES', 'line': 4, 'position': 56}
{'value': 'str', 'type': 'IDENTIFIER', 'line': 4, 'position': 58}
{'value': '=', 'type': 'ASSIGN', 'line': 4, 'position': 62}
{'value': '"Hello"', 'type': 'STRING_LITERAL', 'line': 4, 'position': 64}
{'value': ';', 'type': 'SEMICOLON', 'line': 4, 'position': 71}
{'value': 'if', 'type': 'IF', 'line': 5, 'position': 81}
{'value': '(', 'type': 'LPAREN', 'line': 5, 'position': 84}
{'value': 'x', 'type': 'IDENTIFIER', 'line': 5, 'position': 85}
{'value': '>', 'type': 'GT', 'line': 5, 'position': 87}
{'value': 0, 'type': 'INT_LITERAL', 'line': 5, 'position': 89}
{'value': ')', 'type': 'RPAREN', 'line': 5, 'position': 90}
{'value': '{', 'type': 'LBRACE', 'line': 5, 'position': 92}
{'value': 'x', 'type': 'IDENTIFIER', 'line': 6, 'position': 106}
{'value': '++', 'type': 'INC', 'line': 6, 'position': 107}
{'value': ';', 'type': 'SEMICOLON', 'line': 6, 'position': 109}
{'value': '}', 'type': 'RBRACE', 'line': 7, 'position': 119}
```

#### 2. 测试文件
```
> python lexer.py -s tests/sort.c
{'value': 'void', 'type': 'VOID', 'line': 1, 'position': 0}
{'value': 'sort', 'type': 'IDENTIFIER', 'line': 1, 'position': 5}
{'value': '(', 'type': 'LPAREN', 'line': 1, 'position': 9}
{'value': 'int', 'type': 'INT', 'line': 1, 'position': 10}
{'value': 'arr', 'type': 'IDENTIFIER', 'line': 1, 'position': 14}
{'value': '[', 'type': 'LBRACKET', 'line': 1, 'position': 17}
{'value': ']', 'type': 'RBRACKET', 'line': 1, 'position': 18}
{'value': ',', 'type': 'COMMA', 'line': 1, 'position': 19}
{'value': 'int', 'type': 'INT', 'line': 1, 'position': 21}
{'value': 'n', 'type': 'IDENTIFIER', 'line': 1, 'position': 25}
{'value': ')', 'type': 'RPAREN', 'line': 1, 'position': 26}
{'value': '{', 'type': 'LBRACE', 'line': 1, 'position': 28}
{'value': 'int', 'type': 'INT', 'line': 2, 'position': 34}
{'value': 'i', 'type': 'IDENTIFIER', 'line': 2, 'position': 38}
{'value': ',', 'type': 'COMMA', 'line': 2, 'position': 39}
{'value': 'j', 'type': 'IDENTIFIER', 'line': 2, 'position': 41}
{'value': ',', 'type': 'COMMA', 'line': 2, 'position': 42}
{'value': 'temp', 'type': 'IDENTIFIER', 'line': 2, 'position': 44}
{'value': ';', 'type': 'SEMICOLON', 'line': 2, 'position': 48}
{'value': 'for', 'type': 'FOR', 'line': 3, 'position': 54}
{'value': '(', 'type': 'LPAREN', 'line': 3, 'position': 58}
{'value': 'i', 'type': 'IDENTIFIER', 'line': 3, 'position': 59}
{'value': '=', 'type': 'ASSIGN', 'line': 3, 'position': 61}
{'value': 0, 'type': 'INT_LITERAL', 'line': 3, 'position': 63}
{'value': ';', 'type': 'SEMICOLON', 'line': 3, 'position': 64}
{'value': 'i', 'type': 'IDENTIFIER', 'line': 3, 'position': 66}
{'value': '<', 'type': 'LT', 'line': 3, 'position': 68}
{'value': 'n', 'type': 'IDENTIFIER', 'line': 3, 'position': 70}
{'value': '-', 'type': 'MINUS', 'line': 3, 'position': 72}
{'value': 1, 'type': 'INT_LITERAL', 'line': 3, 'position': 74}
{'value': ';', 'type': 'SEMICOLON', 'line': 3, 'position': 75}
{'value': 'i', 'type': 'IDENTIFIER', 'line': 3, 'position': 77}
{'value': '++', 'type': 'INC', 'line': 3, 'position': 78}
{'value': ')', 'type': 'RPAREN', 'line': 3, 'position': 80}
{'value': '{', 'type': 'LBRACE', 'line': 3, 'position': 82}
{'value': 'for', 'type': 'FOR', 'line': 4, 'position': 92}
{'value': '(', 'type': 'LPAREN', 'line': 4, 'position': 96}
{'value': 'j', 'type': 'IDENTIFIER', 'line': 4, 'position': 97}
{'value': '=', 'type': 'ASSIGN', 'line': 4, 'position': 99}
{'value': 0, 'type': 'INT_LITERAL', 'line': 4, 'position': 101}
{'value': ';', 'type': 'SEMICOLON', 'line': 4, 'position': 102}
{'value': 'j', 'type': 'IDENTIFIER', 'line': 4, 'position': 104}
{'value': '<', 'type': 'LT', 'line': 4, 'position': 106}
{'value': 'n', 'type': 'IDENTIFIER', 'line': 4, 'position': 108}
{'value': '-', 'type': 'MINUS', 'line': 4, 'position': 110}
{'value': 'i', 'type': 'IDENTIFIER', 'line': 4, 'position': 112}
{'value': '-', 'type': 'MINUS', 'line': 4, 'position': 114}
{'value': 1, 'type': 'INT_LITERAL', 'line': 4, 'position': 116}
{'value': ';', 'type': 'SEMICOLON', 'line': 4, 'position': 117}
{'value': 'j', 'type': 'IDENTIFIER', 'line': 4, 'position': 119}
{'value': '++', 'type': 'INC', 'line': 4, 'position': 120}
{'value': ')', 'type': 'RPAREN', 'line': 4, 'position': 122}
{'value': '{', 'type': 'LBRACE', 'line': 4, 'position': 124}
{'value': 'if', 'type': 'IF', 'line': 5, 'position': 138}
{'value': '(', 'type': 'LPAREN', 'line': 5, 'position': 141}
{'value': 'arr', 'type': 'IDENTIFIER', 'line': 5, 'position': 142}
{'value': '[', 'type': 'LBRACKET', 'line': 5, 'position': 145}
{'value': 'j', 'type': 'IDENTIFIER', 'line': 5, 'position': 146}
{'value': ']', 'type': 'RBRACKET', 'line': 5, 'position': 147}
{'value': '>', 'type': 'GT', 'line': 5, 'position': 149}
{'value': 'arr', 'type': 'IDENTIFIER', 'line': 5, 'position': 151}
{'value': '[', 'type': 'LBRACKET', 'line': 5, 'position': 154}
{'value': 'j', 'type': 'IDENTIFIER', 'line': 5, 'position': 155}
{'value': '+', 'type': 'PLUS', 'line': 5, 'position': 157}
{'value': 1, 'type': 'INT_LITERAL', 'line': 5, 'position': 159}
{'value': ']', 'type': 'RBRACKET', 'line': 5, 'position': 160}
{'value': ')', 'type': 'RPAREN', 'line': 5, 'position': 161}
{'value': '{', 'type': 'LBRACE', 'line': 5, 'position': 163}
{'value': 'temp', 'type': 'IDENTIFIER', 'line': 6, 'position': 181}
{'value': '=', 'type': 'ASSIGN', 'line': 6, 'position': 186}
{'value': 'arr', 'type': 'IDENTIFIER', 'line': 6, 'position': 188}
{'value': '[', 'type': 'LBRACKET', 'line': 6, 'position': 191}
{'value': 'j', 'type': 'IDENTIFIER', 'line': 6, 'position': 192}
{'value': ']', 'type': 'RBRACKET', 'line': 6, 'position': 193}
{'value': ';', 'type': 'SEMICOLON', 'line': 6, 'position': 194}
{'value': 'arr', 'type': 'IDENTIFIER', 'line': 7, 'position': 212}
{'value': '[', 'type': 'LBRACKET', 'line': 7, 'position': 215}
{'value': 'j', 'type': 'IDENTIFIER', 'line': 7, 'position': 216}
{'value': ']', 'type': 'RBRACKET', 'line': 7, 'position': 217}
{'value': '=', 'type': 'ASSIGN', 'line': 7, 'position': 219}
{'value': 'arr', 'type': 'IDENTIFIER', 'line': 7, 'position': 221}
{'value': '[', 'type': 'LBRACKET', 'line': 7, 'position': 224}
{'value': 'j', 'type': 'IDENTIFIER', 'line': 7, 'position': 225}
{'value': '+', 'type': 'PLUS', 'line': 7, 'position': 227}
{'value': 1, 'type': 'INT_LITERAL', 'line': 7, 'position': 229}
{'value': ']', 'type': 'RBRACKET', 'line': 7, 'position': 230}
{'value': ';', 'type': 'SEMICOLON', 'line': 7, 'position': 231}
{'value': 'arr', 'type': 'IDENTIFIER', 'line': 8, 'position': 249}
{'value': '[', 'type': 'LBRACKET', 'line': 8, 'position': 252}
{'value': 'j', 'type': 'IDENTIFIER', 'line': 8, 'position': 253}
{'value': '+', 'type': 'PLUS', 'line': 8, 'position': 255}
{'value': 1, 'type': 'INT_LITERAL', 'line': 8, 'position': 257}
{'value': ']', 'type': 'RBRACKET', 'line': 8, 'position': 258}
{'value': '=', 'type': 'ASSIGN', 'line': 8, 'position': 260}
{'value': 'temp', 'type': 'IDENTIFIER', 'line': 8, 'position': 262}
{'value': ';', 'type': 'SEMICOLON', 'line': 8, 'position': 266}
{'value': '}', 'type': 'RBRACE', 'line': 9, 'position': 280}
{'value': '}', 'type': 'RBRACE', 'line': 10, 'position': 290}
{'value': '}', 'type': 'RBRACE', 'line': 11, 'position': 296}
{'value': '}', 'type': 'RBRACE', 'line': 12, 'position': 298}
{'value': 'int', 'type': 'INT', 'line': 14, 'position': 301}
{'value': 'main', 'type': 'IDENTIFIER', 'line': 14, 'position': 305}
{'value': '(', 'type': 'LPAREN', 'line': 14, 'position': 309}
{'value': ')', 'type': 'RPAREN', 'line': 14, 'position': 310}
{'value': '{', 'type': 'LBRACE', 'line': 14, 'position': 312}
{'value': 'int', 'type': 'INT', 'line': 15, 'position': 318}
{'value': 'arr', 'type': 'IDENTIFIER', 'line': 15, 'position': 322}
{'value': '[', 'type': 'LBRACKET', 'line': 15, 'position': 325}
{'value': ']', 'type': 'RBRACKET', 'line': 15, 'position': 326}
{'value': '=', 'type': 'ASSIGN', 'line': 15, 'position': 328}
{'value': '{', 'type': 'LBRACE', 'line': 15, 'position': 330}
{'value': 5, 'type': 'INT_LITERAL', 'line': 15, 'position': 331}
{'value': ',', 'type': 'COMMA', 'line': 15, 'position': 332}
{'value': 8, 'type': 'INT_LITERAL', 'line': 15, 'position': 334}
{'value': ',', 'type': 'COMMA', 'line': 15, 'position': 335}
{'value': 4, 'type': 'INT_LITERAL', 'line': 15, 'position': 337}
{'value': ',', 'type': 'COMMA', 'line': 15, 'position': 338}
{'value': 9, 'type': 'INT_LITERAL', 'line': 15, 'position': 340}
{'value': '}', 'type': 'RBRACE', 'line': 15, 'position': 341}
{'value': ';', 'type': 'SEMICOLON', 'line': 15, 'position': 342}
{'value': 'int', 'type': 'INT', 'line': 16, 'position': 348}
{'value': 'n', 'type': 'IDENTIFIER', 'line': 16, 'position': 352}
{'value': '=', 'type': 'ASSIGN', 'line': 16, 'position': 354}
{'value': 'sizeof', 'type': 'IDENTIFIER', 'line': 16, 'position': 356}
{'value': '(', 'type': 'LPAREN', 'line': 16, 'position': 362}
{'value': 'arr', 'type': 'IDENTIFIER', 'line': 16, 'position': 363}
{'value': ')', 'type': 'RPAREN', 'line': 16, 'position': 366}
{'value': '/', 'type': 'DIVIDE', 'line': 16, 'position': 368}
{'value': 'sizeof', 'type': 'IDENTIFIER', 'line': 16, 'position': 370}
{'value': '(', 'type': 'LPAREN', 'line': 16, 'position': 376}
{'value': 'arr', 'type': 'IDENTIFIER', 'line': 16, 'position': 377}
{'value': '[', 'type': 'LBRACKET', 'line': 16, 'position': 380}
{'value': 0, 'type': 'INT_LITERAL', 'line': 16, 'position': 381}
{'value': ']', 'type': 'RBRACKET', 'line': 16, 'position': 382}
{'value': ')', 'type': 'RPAREN', 'line': 16, 'position': 383}
{'value': ';', 'type': 'SEMICOLON', 'line': 16, 'position': 384}
{'value': 'sort', 'type': 'IDENTIFIER', 'line': 17, 'position': 390}
{'value': '(', 'type': 'LPAREN', 'line': 17, 'position': 394}
{'value': 'arr', 'type': 'IDENTIFIER', 'line': 17, 'position': 395}
{'value': ',', 'type': 'COMMA', 'line': 17, 'position': 398}
{'value': 'n', 'type': 'IDENTIFIER', 'line': 17, 'position': 400}
{'value': ')', 'type': 'RPAREN', 'line': 17, 'position': 401}
{'value': ';', 'type': 'SEMICOLON', 'line': 17, 'position': 402}
{'value': 'for', 'type': 'FOR', 'line': 18, 'position': 408}
{'value': '(', 'type': 'LPAREN', 'line': 18, 'position': 412}
{'value': 'int', 'type': 'INT', 'line': 18, 'position': 413}
{'value': 'i', 'type': 'IDENTIFIER', 'line': 18, 'position': 417}
{'value': '=', 'type': 'ASSIGN', 'line': 18, 'position': 419}
{'value': 0, 'type': 'INT_LITERAL', 'line': 18, 'position': 421}
{'value': ';', 'type': 'SEMICOLON', 'line': 18, 'position': 422}
{'value': 'i', 'type': 'IDENTIFIER', 'line': 18, 'position': 424}
{'value': '<', 'type': 'LT', 'line': 18, 'position': 426}
{'value': 'n', 'type': 'IDENTIFIER', 'line': 18, 'position': 428}
{'value': ';', 'type': 'SEMICOLON', 'line': 18, 'position': 429}
{'value': 'i', 'type': 'IDENTIFIER', 'line': 18, 'position': 431}
{'value': '++', 'type': 'INC', 'line': 18, 'position': 432}
{'value': ')', 'type': 'RPAREN', 'line': 18, 'position': 434}
{'value': '{', 'type': 'LBRACE', 'line': 18, 'position': 436}
{'value': 'printf', 'type': 'IDENTIFIER', 'line': 19, 'position': 446}
{'value': '(', 'type': 'LPAREN', 'line': 19, 'position': 452}
{'value': '"%d "', 'type': 'STRING_LITERAL', 'line': 19, 'position': 453}
{'value': ',', 'type': 'COMMA', 'line': 19, 'position': 458}
{'value': 'arr', 'type': 'IDENTIFIER', 'line': 19, 'position': 460}
{'value': '[', 'type': 'LBRACKET', 'line': 19, 'position': 463}
{'value': 'i', 'type': 'IDENTIFIER', 'line': 19, 'position': 464}
{'value': ']', 'type': 'RBRACKET', 'line': 19, 'position': 465}
{'value': ')', 'type': 'RPAREN', 'line': 19, 'position': 466}
{'value': ';', 'type': 'SEMICOLON', 'line': 19, 'position': 467}
{'value': '}', 'type': 'RBRACE', 'line': 20, 'position': 473}
{'value': 'printf', 'type': 'IDENTIFIER', 'line': 21, 'position': 479}
{'value': '(', 'type': 'LPAREN', 'line': 21, 'position': 485}
{'value': '"\\n"', 'type': 'STRING_LITERAL', 'line': 21, 'position': 486}
{'value': ')', 'type': 'RPAREN', 'line': 21, 'position': 490}
{'value': ';', 'type': 'SEMICOLON', 'line': 21, 'position': 491}
{'value': 'return', 'type': 'RETURN', 'line': 22, 'position': 497}
{'value': 0, 'type': 'INT_LITERAL', 'line': 22, 'position': 504}
{'value': ';', 'type': 'SEMICOLON', 'line': 22, 'position': 505}
{'value': '}', 'type': 'RBRACE', 'line': 23, 'position': 507}
```

