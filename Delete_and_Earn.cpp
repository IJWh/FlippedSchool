class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
                int result = 0, last, cnc;
        int arr[10000];
        
        for(int i=0;i<10000;i++){
            arr[i]=0;
        }
        for(int i=0;i<nums.size();i++){
            arr[nums[i]]+= nums[i];
        }
        last = 0;
        
        cnc = 0;
        for(int i=0;i<10000;i++){
            if(arr[i] == 0){
                cnc = 0;
                last = result;
                continue;
            }else{
                cnc++;
                if(cnc <= 2){
                    arr[i] += last;
                }else if(cnc ==3){
                    arr[i] += arr[i-2];
                }
                else{
                    arr[i] += max(arr[i-3], arr[i-2]);
                }
                result = max(arr[i],result);
            }
        }
        
        

        return result;
    }
};
