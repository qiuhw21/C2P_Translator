#include <stdio.h>
#include <string.h>

int isPalindrome(char *s) {
    int length = strlen(s);
    for (int i = 0; i < length / 2; i++) {
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
