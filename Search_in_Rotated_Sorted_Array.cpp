class Solution {
public:
    int search(vector<int>& nums, int target) {
        int index, front, mid, end;
        index= -1;
        front = 0;
        mid = nums.size()/2;
        end = nums.size()-1;
        
        //search pivot
        /* 4 cases
        1. target < nums(mid) && target > nums(front)
        2. target > nums(mid) && target < nums(end)
        3. target < nums(mid) && target < nums(end) - pivot included
            3.1 nums(mid) > nums(end)
            3.2 nums(mid) < nums(end)
        4. target > nums(mid) && target > nums(front) - pivot included
            4.1 nums(mid) > nums(front)
            4.2 nums(mid) < nums(front)
        
        
        left? right?
        */
        while(front <= mid && mid <= end){
            //target found;
            if(nums[front]==target){
                index = front;
                break;
            }else if(nums[mid]==target){
                index = mid;
                break;
            }else if(nums[end] == target){
                index = end;
                break;
            }
            
            //adjust location
            //case 1
            if(target > nums[front] && target < nums[mid]){
                //to left
                mid--;
                end = mid;
                front++;
                mid = (front+end)/2;
            }
            //case 2
            else if(target < nums[end] && target > nums[mid]){
                //to right
                mid++;
                end--;
                front = mid;
                mid = (front+end)/2;
            }
            //case 3
            else if(target < nums[end] && target < nums[mid]){
                //case 3.1
                if(nums[mid] > nums[end]){
                    //to right
                    mid++;
                    end--;
                    front = mid;
                    mid = (front+end)/2;
                }
                //case 3.2
                else{
                    //to left
                    mid--;
                    end = mid;
                    front++;
                    mid = (front+end)/2;
                }
            }
            //case 4
            else if(target > nums[front] && target > nums[mid]){
                //case 4.1
                if(nums[front] < nums[mid]){
                    //to right
                    mid++;
                    end--;
                    front = mid;
                    mid = (front+end)/2;
                }
                //case 4.2
                else{
                    //to left
                    mid--;
                    end = mid;
                    front++;
                    mid = (front+end)/2;
                }
            }
            else{
                cout << "unexpected case "<< endl;
                break;
            }
        }
        return index;
    }
};
