class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int temp;
        bool swap = false;
        vector<int>::reverse_iterator iter_front, iter_back;
        auto front = nums.begin();
        
        //search location to swap
        for(iter_front = nums.rbegin();iter_front != nums.rend();iter_front++){
            iter_back = nums.rbegin();
            while(iter_front != iter_back){
                //find location to swap
                if(*iter_front < *iter_back){
                    swap = true;
                    break;
                }
                iter_back++;
            }
            if(swap){
                break;
            }
        }

        if(swap){
            //reverse front
            front = iter_front.base();
            temp = *iter_front;
            *iter_front = *iter_back;
            *iter_back = temp;
        }
        
        
        sort(front, nums.end());
        return;
    }
};
