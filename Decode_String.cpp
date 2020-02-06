class Solution {
public:
    string decodeString(string s) {
        string decodeS = s;
        string result = "";
        string str = "";
        string right_str = "";
        stack<int> repeat;
        stack<string> sub;
        int inner = 0;
        int max_inner;
        int pt, pt2,pt_n;
        int rnum;
        int A = 'A';
        
        
        
        while(decodeS.length() > 0){
            //case repeat
            if(decodeS[0] < A ){
                //extract number
                pt = decodeS.find('[');
                str = decodeS.substr(0,pt);
                repeat.push(stoi(str));
                decodeS = decodeS.substr(pt);
                
                inner=1;
                for(pt = 1; pt < decodeS.length();pt++){
                    if(decodeS[pt] == '['){
                        inner++;
                    }else if(decodeS[pt] == ']'){
                        inner--;
                    }

                    if(inner == 0){
                        break;
                    }
                }
                sub.push(decodeS.substr(1,pt-1));
                decodeS = decodeS.substr(pt+1);
            }
            //case non-repeat
            else{
                repeat.push(1);
                pt = decodeS.find('[');
                if(pt != -1){
                    //find number position
                    for(pt_n = 0;pt_n < pt; pt_n++){
                        if(decodeS[pt_n] < A){
                            break;
                        }
                    }
                    sub.push(decodeS.substr(0,pt_n));
                    decodeS = decodeS.substr(pt_n);
                }else{
                    sub.push(decodeS);
                    decodeS = "";
                }
            }
            
            //decode string
            while(!repeat.empty()){
                //test additional repeating
                str = sub.top();
                pt = str.find('[');
                max_inner = 0;
                if(pt != -1){
                    sub.pop();
                    
                    inner = 1;
                    for(pt2 = pt+1; pt2<str.length();pt2++){
                        if(str[pt2] == '['){
                            inner++;
                            max_inner = inner>max_inner?inner:max_inner;
                        }else if(str[pt2] == ']'){
                            inner--;
                        }

                        if(inner == 0){
                            break;
                        }
                    }
                    
                    //search part which will be checked later
                    right_str = str.substr(pt2+1) + right_str;
                    
                    //push part which is not going to repeat
                    //find num size of num first
                    for(pt_n = 0; pt_n < pt; pt_n++){
                        if(str[pt_n] < A){
                            break;
                        }
                    }
                    sub.push(str.substr(0,pt_n));
                    
                    //push inner repeat num
                    repeat.push(stoi(str.substr(pt_n,pt-pt_n)));
                    
                    //find inner string
                    str = str.substr(pt+1, pt2-pt-1);
                    
                    //push inner string
                    sub.push(str);
                    
                    if(max_inner > 1){
                        continue;
                    }
                }
                rnum = repeat.top();
                repeat.pop();
                str = "";
                while(rnum){
                    str+=sub.top();
                    rnum--;
                }
                sub.pop();
                if(sub.size() > 0){
                    str = sub.top()+str;
                    sub.pop();
                }
                if(right_str.length() > 0){
                    str = str + right_str;
                }
                right_str = "";
                sub.push(str);
            }
            result += sub.top();
            sub.pop();
        }
        
        return result;
    }
};
