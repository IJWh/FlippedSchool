class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        int litvl = 0;
        map<char, int> remain_task;
        map<char, int>::iterator it;
        vector<int> ordered_rt;
        vector<int>::iterator it2;
        int cnt= n+1;
        
        //count every task
        for(auto iter = tasks.begin(); iter != tasks.end();iter++){
            it = remain_task.find(*iter);
            //count add
            if(it != remain_task.end()){
                it->second++;
            }
            //insert new task
            else{
                remain_task[*iter] = 1;
            }
        }
        
        for(it = remain_task.begin(); it != remain_task.end(); it++){
            ordered_rt.push_back(it->second);
        }
        
        while(ordered_rt.size()>0){
            //sorting remaining tasks as descending order
            sort(ordered_rt.begin(),ordered_rt.end(), greater<>());
            
            //additional idle
            if(cnt <= n){
                litvl+= n-cnt+1;
            }
            cnt = 0;
            for(it2=ordered_rt.begin(); it2!= ordered_rt.end(); it2++){
                (*it2)--;
                litvl++;
                cnt++;
                if(*it2 == 0){
                    ordered_rt.erase(it2);
                    it2--;
                }
                if(cnt > n){
                    break;
                }
            }
        }
        
        return litvl;
    }
};
