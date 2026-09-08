#include "../utils/common.hpp"
int exponential(int n){
    int count = 0,base = 1;

    for(int i=0 ; i<n ; i++){
        for (int j=0 ; j<base ; j++){
            count++;
        }
        base = base * 2;
    }

    return count;
}

int main(){
    
    int n = 5;
    int res;

    res = exponential(n);
    cout << "细胞分裂结果：res=" << res <<endl;

}