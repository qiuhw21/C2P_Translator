// 测试代码：计算器

int calculate(char s[]) {
    int result = 0;
    int num = 0;
    int sign = 1;
    for (int i = 0; s[i] != '\0'; i++) {
        char c = s[i];
        if (c >= '0' && c <= '9') {
            num = 10 * num + (c - '0');
        } else if (c == '+') {
            result = result + sign * num;
            num = 0;
            sign = 1;
        } else if (c == '-') {
            result = result + sign * num;
            num = 0;
            sign = -1;
        }
        // Add more conditions for '*', '/' and parentheses if needed
    }
    result = result + sign * num;
    return result;
}

int main() {
    char expression[] = "1 + 2 - 3";
    printf("Result: %d\n", calculate(expression));
    return 0;
}
