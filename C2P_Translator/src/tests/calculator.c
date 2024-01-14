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
