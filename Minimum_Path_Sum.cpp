class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int min_sum;
        vector<vector<int>> grid_dp = grid;
        
        if(grid_dp.size() == 0){
            return 0;
        }
        
        for(int i=1;i< grid.size();i++){
            grid_dp[i][0] = grid_dp[i-1][0] + grid_dp[i][0];
        }
        
        for(int i=1;i< grid[0].size();i++){
            grid_dp[0][i] = grid_dp[0][i-1] + grid_dp[0][i];
        }
        
        for(int i=1;i< grid.size();i++){
            for(int j=1;j< grid[0].size();j++){
                grid_dp[i][j] = min(grid_dp[i-1][j],grid_dp[i][j-1]) + grid_dp[i][j];
            }
        }
        
        return grid_dp.back().back();
    }
};
