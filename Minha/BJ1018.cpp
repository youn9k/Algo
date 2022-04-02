#include<iostream>
using namespace std;

int main() {
    int n, m, ans;
    char boa[50][50] = {};
    char ca1[8][8] = {
        'B','W','B','W','B','W','B','W',
        'W','B','W','B','W','B','W','B',
        'B','W','B','W','B','W','B','W',
        'W','B','W','B','W','B','W','B',
        'B','W','B','W','B','W','B','W',
        'W','B','W','B','W','B','W','B',
        'B','W','B','W','B','W','B','W',
        'W','B','W','B','W','B','W','B'
    };
    char ca2[8][8] = {
        'W','B','W','B','W','B','W','B',
        'B','W','B','W','B','W','B','W',
        'W','B','W','B','W','B','W','B',
        'B','W','B','W','B','W','B','W',
        'W','B','W','B','W','B','W','B',
        'B','W','B','W','B','W','B','W',
        'W','B','W','B','W','B','W','B',
        'B','W','B','W','B','W','B','W'
    };
    cin >> n >> m;
    int nm = (n - 7) * (m - 7);
    int* xp = new int[nm];
    int* yp = new int[nm];
    int idx = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            cin >> boa[i][j];

    for (int i = 0; i < n - 7; i++) {
        for (int j = 0; j < m - 7; j++) {
            int ind1 = 0;
            int ind2 = 0;
            for (int k = 0; k < 8; k++) {
                for (int l = 0; l < 8; l++) {
                    if (boa[i + k][j + l] != ca1[k][l]) {
                        ind1++;
                    }
                    else if (boa[i + k][j + l] != ca2[k][l]) {
                        ind2++;
                    }

                }
            }
            xp[idx] = ind1;
            yp[idx] = ind2;
            idx++;
        }
    }
    ans = xp[0];
    for (int i = 0; i < nm; i++) {
        if (ans > xp[i]) ans = xp[i];
        if (ans > yp[i]) ans = yp[i];
    }
    cout << ans;
    delete[]xp;
    delete[]yp;
}