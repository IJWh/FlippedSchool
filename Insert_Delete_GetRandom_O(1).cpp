class RandomizedSet {
private:
    unordered_set<int> rds;
public:
    /** Initialize your data structure here. */
    RandomizedSet() {
        srand(time(0));
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        //insert failed, same key exists
        if(rds.find(val) != rds.end()){
            return false;
        }
        //insert sucess
        else{
            rds.insert(val);
            return true;
        }
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        //remove sucess
        if(rds.find(val) != rds.end()){
            rds.erase(val);
            return true;
        }
        //key does not exist, remove failed
        else{
            return false;
        }
    }
    
    /** Get a random element from the set. */
    int getRandom() {
        int selected;
        int random;
        auto it = rds.begin();
        
        random = rand()%rds.size();
        
        for(int i=0;i<random;i++){
            it++;
        }
        return *it;
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */
