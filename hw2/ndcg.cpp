#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

int main(){
    vector<int> a;
    int count;
    cin >> count;
    while(1){
        int tmp;
        cin >> tmp;
        if (tmp == -1){
            break;
        }
        a.push_back(tmp);
    }
    double dcg = 0, idcg = 0;
    for(int i = 0; i < count; i++){
        dcg += a[i]/(log(i+2)/log(2));
    }
    sort(a.begin(), a.end());
    for(int i = a.size()-1; i >= a.size() - count; i--){
        int x = a.size() - i;
        idcg += a[i]/(log(x+1)/log(2));
    }
    cout << "dcg: " << dcg << endl;
    cout << "idcg: " << idcg << endl;
    cout << "nidcg: " << dcg/idcg << endl;    
}