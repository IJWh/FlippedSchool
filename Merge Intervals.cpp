//https://leetcode.com/problems/merge-intervals/

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> result;
        vector<vector<int>> itv = intervals;
        vector<int> merged;
        int start, end;
        sort(itv.begin(), itv.end());
        
        //입력값 유무 확인
        if(itv.size()==0){
            return result;
        }
        
        start = itv[0][0];
        end = itv[0][1];
        
        for(int i=1;i<itv.size();i++){
            //병합 가능 여부 확인
            if(itv[i][0] <= end){
                //병합 가능시 end값 갱신(필요시)
                if(end < itv[i][1]){
                    end = itv[i][1];
                }
            }
            else{
                //추가 병합 불가시 기존 값 저장
                merged.push_back(start);
                merged.push_back(end);
                result.push_back(merged);
                merged.clear();
                start = itv[i][0];
                end = itv[i][1];
            }
        }
        //마지막 값 저장 여부 확인
        if(result.size() == 0 || itv[itv.size()-1][1] != result[result.size()-1][1]){
            merged.push_back(start);
            merged.push_back(end);
            result.push_back(merged);
        }
        //결과 출력
        return result;
    }
};
