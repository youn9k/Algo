#include<iostream>
using namespace std;

int main() {
    int sum = 0;
    int boa[9] = { };
    for (int i = 0; i < 9; i++) {
        cin >> boa[i];
        sum += boa[i];
    }
   
    for(int i = 0; i < 8; i++) {
        for (int j = i + 1; j < 9; j++) {
            if (sum - boa[i] - boa[j] == 100) {
                boa[i] = -1; boa[j] = -1;
                break;
            }
        }
        if (boa[i] == -1) break;
    }
    for (int i = 0; i < 8; i++) {
        for (int j = 8; j > i; j--) {
            if (boa[j - 1] > boa[j]) {
                int t = boa[j - 1]; boa[j - 1] = boa[j]; boa[j] = t;
            }
        }
    }

    for (int i = 2; i < 9; i++) {
        cout << boa[i];
        if (i != 8) cout << endl;
        }
}