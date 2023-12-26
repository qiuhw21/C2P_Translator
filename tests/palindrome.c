// 测试代码：判断字符串是否为回文
int strlen(char s[]) {
    int length = 0;
    while (s[length] != '\0') {
        length++;
    }
    return length;
}

int isPalindrome(char s[]) {
    int length = strlen(s);
    int i;
    for (i = 0; i < length / 2; i++) {
        if (s[i] != s[length - i - 1]) {
            return 0;
        }
    }
    return 1;
}

int main() {
    char s[] = "abbcdcbba";
    if (isPalindrome(s)) {
        printf("True\n");
    } else {
        printf("False\n");
    }
    return 0;
}
