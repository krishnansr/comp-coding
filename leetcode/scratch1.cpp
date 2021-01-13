#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    int num;
    long long_num;
    char string;
    float decimal;
    double long_decimal;
    scanf("%d %ld %s %f %lf", &num, &long_num, &string, &decimal, &long_decimal);
    // cout<<num<<endl;
    printf("%d\n%ld\n%c\n%f\n%lf", num, long_num, string, decimal, long_decimal);

    return 0;
}
