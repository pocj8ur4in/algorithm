#include <cstdio>
#include <vector>

void n_and_m(int N, int M, std::vector<int>& vec){
    if (M == 0) {
        for(int i = 0; i < vec.size(); i++){
            printf("%d ", vec[i]);
        }

        printf("\n");

        return;
    }

    for(int i = 1; i < N + 1; i++) {
        int chk = 0;

        for (int j = 0; j < vec.size(); j++) {
            if (vec[j] == i) {
                chk++;
                break;
            }
        }

        if (chk == 0) {
            std::vector<int> tmp = vec;
            tmp.push_back(i);

            n_and_m(N, M - 1, tmp);
        }
    }
}

int main() {
    int N, M;

    scanf("%d %d", &N, &M);

    std::vector<int> vec;

    n_and_m(N, M, vec);
}
