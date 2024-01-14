# Instruction

## 运行方式

### 环境要求
- Python 3.8+
- PLY (Python Lex-Yacc)

### 运行指南
1. 确保已安装Python 3.8，并且安装了PLY库。
2. 在命令行或终端中，切换到项目所在目录。
3. 运行命令 `python mian.py -s <filename> -o <output_filename>`，其中`<filename>`为待解析的C语言源文件，`<output_filename>`为输出的python文件名。
例如，运行命令 `python main.py -s tests/sort.c -o sort.py`，则会将`tests/sort.c`翻译得到的python文件输出到`sort.py`文件中。

### 运行结果

#### 1. 测试代码
源代码：
```
// 测试代码：计算器
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>
#include <stdlib.h>
int calculate(char s[])
{
    int result = 0;
    int num = 0;
    int sign = 1;
    for (int i = 0; i < strlen(s); i++)
    {
        char c = s[i];
        if (c >= '0' && c <= '9')
        {
            int tmp = 0;
            if (c == '0')
            {
                tmp = 0;
            }
            if (c == '1')
            {
                tmp = 1;
            }
            if (c == '2')
            {
                tmp = 2;
            }
            if (c == '3')
            {
                tmp = 3;
            }
            if (c == '4')
            {
                tmp = 4;
            }
            if (c == '5')
            {
                tmp = 5;
            }
            if (c == '6')
            {
                tmp = 6;
            }
            if (c == '7')
            {
                tmp = 7;
            }
            if (c == '8')
            {
                tmp = 8;
            }
            if (c == '9')
            {
                tmp = 9;
            }

            num = 10 * num + tmp;
        }
        if (c == '+')
        {
            result = result + sign * num;
            num = 0;
            sign = 1;
        }
        if (c == '-')
        {
            result = result + sign * num;
            num = 0;
            sign = -1;
        }
        // Add more conditions for '*', '/' and parentheses if needed
    }
    result = result + sign * num;
    return result;
}

int main()
{
    char expression[] = "1 + 2 - 3";
    printf("Result: %d\n", calculate(expression));
    return 0;
}
```

运行结果：
```
> python main.py               
def calculate(s):
	result = 0
	num = 0
	sign = 1
	i = 0
	while i < len(s):
		c = s[i]
		if c >= '0' and c <= '9':
			tmp = 0
			if c == '0':
				tmp = 0
			if c == '1':
				tmp = 1
			if c == '2':
				tmp = 2
			if c == '3':
				tmp = 3
			if c == '4':
				tmp = 4
			if c == '5':
				tmp = 5
			if c == '6':
				tmp = 6
			if c == '7':
				tmp = 7
			if c == '8':
				tmp = 8
			if c == '9':
				tmp = 9
			num = 10 * num + tmp
		if c == '+':
			result = result + sign * num
			num = 0
			sign = 1
		if c == '-':
			result = result + sign * num
			num = 0
			sign = - 1
		i += 1
	result = result + sign * num
	return result
def main():
	expression = "1 + 2 - 3"
	print("Result: %d\n", calculate(expression))
	return 0
if __name__ == '__main__':
	main()

```
