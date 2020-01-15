class Solution {
public:
    bool isHappy(int n) {
        bool result = false;
        int total, remain;
        //input > int형 > max값 약 21억
        bitset<740> used(0);
        
        remain = n;
        total = 0;
        //happy number 찾기
        while(1){
            while(remain > 0){
                total += pow(remain%10,2);
                remain /=10;
            }
            //loop발생, happy number 불가능
            if(used.test(total)){
                break;
            }
            used.flip(total);
            //happy number 가능
            if(total == 1){
                result = true;
                break;
            }
            remain = total;
            total = 0;
        }
        return result;
    }
};
