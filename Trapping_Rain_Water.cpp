class Solution {
public:
    int trap(vector<int>& height) {
        int maxH, remain, check, h;
        
        remain = 0;
        
        if(height.size() == 0){
            return remain;
        }
        //find highest point
        maxH = 0;
        for(int i = 0; i< height.size(); i++){
            if(height[i] > maxH){
                maxH = height[i];
            }
        }
        
        //substract graph
        for(int i = 0; i< height.size(); i++){
            remain += maxH-height[i];
        }
        
        //from left-end
        check = 0;
        
        h = 0;
        while(height[check] != maxH){
            if(height[check] > h){
                h = height[check];
            }
            remain -= maxH - h;
            check++;
        }
        //from right-end
        check = height.size() - 1;
        
        h = 0;
        while(height[check] != maxH){
            if(height[check] > h){
                h = height[check];
            }
            remain -= maxH - h;
            check--;
        }
        
        return remain;
    }
};
