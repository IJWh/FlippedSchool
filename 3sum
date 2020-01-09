//https://leetcode.com/problems/3sum/

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> set;
        int a, b, c, start, end, count;
        vector<int> list = nums;
        int a_end = list.size()-2;
        
        //리스트 오름차순 정렬
        sort(list.begin(), list.end());
        
        //반복문 a값
        for(int i = 0; i< a_end ; i++){
            a = list[i];
            //탈출조건, 첫번째 값이 0보다 클때
            if(a>0){
                break;
            }
            //중복검사 제외
            if(i >0 && a == list[i-1]){
                continue;
            }
            start = i+1;
            end = list.size()-1;
            while(start < end){
                b = list[start];
                c = list[end];
                
                if(a+b+c ==0){
                    set.push_back(a);
                    set.push_back(b);
                    set.push_back(c);
                    if(result.size() ==0 || set != result.back()){
                        result.push_back(set);
                    }
                    set.clear();
                    start++;
                    end--;
                }
                else if(a+b+c > 0){
                    //중복검사 제외
                    while(start < end && list[end] == c){
                        end--;
                    }
                }
                else{
                    //중복검사 제외
                    while(start < end && list[start] == b){
                        start++;
                    }
                }
            }
        }
        return result;
    }
};
