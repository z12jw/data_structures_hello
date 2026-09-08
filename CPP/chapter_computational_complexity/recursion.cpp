#include "../utils/common.hpp"
#include <windows.h>

int fib(int n){
    if(n==1 | n==2){
        return n-1;
    }

    int res = fib(n-1) + fib(n-2);

    return res;
}

int main(){
    SetConsoleOutputCP(CP_UTF8); // 设置控制台输出为 UTF-8 编码，避免中文乱码

    int n = 5;
    int res;

    res = fib(n);
    cout << "\n斐波那契数列结果： res=" << res << endl;
}