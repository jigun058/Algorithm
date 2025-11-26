#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;
    vector<string> G(N), R(N);
    for(int i = 0; i < N; i++){
        cin >> G[i];
        // 'X'는 덮여야 할 칸 → '?'로 표시
        R[i].resize(M);
        for(int j = 0; j < M; j++){
            R[i][j] = (G[i][j] == 'X' ? '?' : '.');
        }
    }

    auto canA = [&](int r, int c){
        if(r+1 >= N || c+3 >= M) return false;
        // 6개 칸 모두 아직 '?'
        if(R[r][c]   != '?') return false;
        if(R[r][c+3] != '?') return false;
        for(int k = 0; k < 4; k++){
            if(R[r+1][c+k] != '?') return false;
        }
        return true;
    };
    auto placeA = [&](int r, int c){
        R[r][c]   = 'A';
        R[r][c+3] = 'A';
        for(int k = 0; k < 4; k++){
            R[r+1][c+k] = 'A';
        }
    };
    auto canB = [&](int r, int c){
        if(c+1 >= M) return false;
        return R[r][c] == '?' && R[r][c+1] == '?';
    };
    auto placeB = [&](int r, int c){
        R[r][c]   = 'B';
        R[r][c+1] = 'B';
    };

    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            if(R[i][j] == '?'){
                if(canA(i,j)){
                    placeA(i,j);
                }
                else if(canB(i,j)){
                    placeB(i,j);
                }
                else{
                    // 덮을 수 없는 칸이 생기면 즉시 -1
                    cout << "-1\n";
                    return 0;
                }
            }
        }
    }

    // 성공적으로 전부 덮었으면 결과 출력
    for(int i = 0; i < N; i++){
        cout << R[i] << "\n";
    }
    return 0;
}
