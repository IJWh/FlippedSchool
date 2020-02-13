class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> num = nums;
        vector<int>::iterator it_back, begin, end;
        vector<int>::reverse_iterator it_front;
        int count = 0;
        bool redup;
        
        sort(num.begin(),num.end());
        count = num.size();
        for(int i=count -1;i>0;i--){
            count *= i;
        }
        result.push_back(num);
        count--;
        //find all the posible permutation
        while(count--){
            begin = num.begin();
            end = num.end()-1;
            
            for(it_front = num.rbegin()+1;it_front != num.rend();it_front++){
                //location searched
                if(*it_front < *(it_front-1)){
                    break;
                }
            }
            
            //case to save the last one
            if(it_front == num.rend()){
                result.push_back(num);
                break;
            }
            
            for(it_back = it_front.base();it_back != num.end();it_back++){
                //search location which needs to be switched with it_front
                if(*it_back <= *it_front){
                    it_back--;
                    break;
                }
            }
            //if iterator reached to the end, relocate position
            if(it_back == num.end()){
                it_back--;
            }



            //swap
            iter_swap(it_front, it_back);

            begin = it_front.base();
            //reorder
            while(begin < end){
                iter_swap(begin, end);
                begin++;
                end--;
            }
            
            //check reduplicant
            redup = true;
            for(int i=0;i<num.size();i++){
                if(num[i] != result.back()[i]){
                    redup = false;
                    break;
                }
            }
            if(!redup){
                result.push_back(num);
            }
            
        }
        return result;
    }
};
