class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int point = coins.size();
        vector<int> minchange;
        vector<int> coin;
        
        //exception 1
        if(amount == 0){
            return 0;
        }
        //dynamic programming
        
        //exclude useless coins
        for(int i=0;i<point;i++){
            if(coins[i] < amount){
                coin.push_back(coins[i]);
            }else if( coins[i] == amount){
                return 1;
            }
        }
        sort(coin.begin(),coin.end());
        point = coin.size();
        
        //exception 2
        if(coin.size() == 0){
            return -1;
        }
        //make a array which contains number of coins to make price. price = position
        for(int i=0;i<=amount;i++){
            minchange.push_back(amount+1);
        }
        minchange[0] = 0;
        
        //update basic coins
        for(int i=0;i<point;i++){
            minchange[coin[i]] = 1;
        }
        
        //calculate every position
        for(int i = 0; i<point;i++){
            for(int j = coin[i] ; j<=amount;j++){
                minchange[j] = min(minchange[j], minchange[j-coin[i]]+1);
            }
        }
        
        if(minchange[amount]== amount+1){
            return -1;
        }else{
            return minchange[amount];
        }
    }
};
