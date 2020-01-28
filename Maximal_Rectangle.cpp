class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        int Max_area = 0, area;
        int zero = '0';
        int height = matrix.size(), width;
        int num, cumul;//cumulative number
        vector<vector<int>> new_matrix;
        vector<int> mat_x;
        
        if(height == 0){
            return 0;
        }
        width = matrix[0].size();
        
        //duplicate matrix
        for(int i=0; i< height;i++){
            mat_x.clear();
            for(int j=0; j< width;j++){
                num = matrix[i][j]-zero;
                if(num == 0){
                    mat_x.push_back(0);
                }
                else{
                    cumul = 1;
                    for(int k = j+1; k < width; k++){
                        if(matrix[i][k]-zero == 0){
                            break;
                        }
                        else{
                            cumul++;
                        }
                    }
                    mat_x.push_back(cumul);
                }
            }
            new_matrix.push_back(mat_x);
        }
        
        
        //check each area;
        for(int j=0;j<width;j++){
            for(int i=0; i<height; i++){
                if(new_matrix[i][j] > 0){
                    area = new_matrix[i][j];
                    //check below i
                    for(int k=i+1; k<height; k++){
                        if(new_matrix[i][j] > new_matrix[k][j]){
                            break;
                        }
                        area += new_matrix[i][j];
                    }
                    for(int k=i-1; k>=0; k--){
                        if(new_matrix[i][j] > new_matrix[k][j]){
                            break;
                        }
                        area += new_matrix[i][j];
                    }
                    //check above i
                    
                    if(area > Max_area){
                        Max_area = area;
                    }
                }
            }
        }
        
        return Max_area;
    }
};
