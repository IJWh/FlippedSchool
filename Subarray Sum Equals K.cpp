//https://leetcode.com/problems/subarray-sum-equals-k/

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int result = 0;
        int sum, left, right;
        vector<int> sums;
        
        //예외처리
        if(nums.size() == 0){
            return 0;
        }
        
        //0~현위치까지 더한 값을 지닌 배열
        sum = 0;
        for(int i=0;i<nums.size();i++){
            sum += nums[i];
            sums.push_back(sum);
        }
        
        //현위치~ 0까지 더한값을 빼면서 조건 만족하는 subarray찾기
        for(int i=sums.size()-1; i>=0; i--){
            if(sums[i] ==k){
                result++;
            }
            for(int j=i-1; j>=0; j--){
                if(sums[i]- sums[j] == k){
                    result++;
                }
            }
        }
        
        return result;
    }
};
