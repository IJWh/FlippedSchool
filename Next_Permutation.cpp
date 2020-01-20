class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        /*
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
        */
        vector<int>::reverse_iterator it_front;
        vector<int>::iterator it_back, begin, end;
        bool swap = false;
        begin = nums.begin();
        end = nums.end()-1;
        
        //search location where descendent start(from behind)
        for(it_front = nums.rbegin()+1;it_front != nums.rend();it_front++){
            //location searched
            if(*it_front < *(it_front-1)){
                swap = true;
                break;
            }
        }
        
        //search location to switch with it_front
        if(swap){
            for(it_back = it_front.base();it_back != nums.end();it_back++){
                //search location which needs to be switched with it_front
                if(*it_back <= *it_front){
                    it_back--;
                    break;
                }
            }
            //if iterator reached to the end, relocate position
            if(it_back == nums.end()){
                it_back--;
            }
            
            //swap
            iter_swap(it_front, it_back);
            
            begin = it_front.base();
        }
        //reorder
        while(begin < end){
            iter_swap(begin, end);
            begin++;
            end--;
        }
    }
};
