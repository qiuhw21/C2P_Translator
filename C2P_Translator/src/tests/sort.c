// 测试代码：冒泡排序
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void sort(int arr[], int n)
{
    int i;
    int j;
    int temp;
    for (int i = 0; i < n - 1; i++)
    {
        for (j = 0; j < n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int main()
{
    int arr[5] = {5, 8, 4, 5, 9};
    int n = 5;
    sort(arr, n);
    for (int i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }
    return 0;
}
