//https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

class Solution {
public:
    int minDominoRotations(vector<int>& A, vector<int>& B) {
        int minRot;
        bool check[7];
        int Alist[7],Blist[7];

        for(int i=0;i<7;i++){
            check[i] = true;
            Alist[i] = 0;
            Blist[i] = 0;
        }
        check[0]=false;
        
        for(int i=0;i<A.size();i++){
            Alist[A[i]]++;
            Blist[B[i]]++;
            if(A[i] != 1 && B[i] != 1){
                check[1] = false;
            }
            if(A[i] != 2 && B[i] != 2){
                check[2] = false;
            }
            if(A[i] != 3 && B[i] != 3){
                check[3] = false;
            }
            if(A[i] != 4 && B[i] != 4){
                check[4] = false;
            }
            if(A[i] != 5 && B[i] != 5){
                check[5] = false;
            }
            if(A[i] != 6 && B[i] != 6){
                check[6] = false;
            }
        }
        //조건만족 불가
        if (!(check[1] || check[2] || check[3] || check[4] || check[5] || check[6])){
            return -1;
        }
        
        //조건만족, 최솟값 찾기
        minRot = 20000;
        for(int i=1;i<7;i++){
            if(check[i]){
                minRot = min(minRot, Alist[i]);
                minRot = min(minRot, Blist[i]);
                //겹치는 부분 제외
                if(Alist[i]+Blist[i] > A.size()){
                    minRot -= Alist[i]+Blist[i] - A.size();
                }
                break;
            }
        }

        
        
        return minRot;
    }
};
