class Solution {
public:
    string longestPalindrome(string s) {
        string lp="";
        string sub;
        int start, end;
        
        //case substring with obb numbers
        for(int i=0;i<s.length();i++){
            start = i;
            end = i;
            while(start>=0 && end <s.length()){
                //case not palindrome
                if(s[start] != s[end]){
                    break;
                }
                start--;
                end++;
            }
            //undo last point move
            start++;
            end--;
            sub = s.substr(start, end-start+1);
            
            //update longest substring
            if(sub.length() > lp.length()){
                lp = sub;
            }
        }
        
        //case substring with even numbers
        for(int i=0;i<s.length();i++){
            start = i;
            end = i+1;
            //case not palindrome
            if(s[start] != s[end]){
                continue;
            }
            while(start>=0 && end <s.length()){
                if(s[start] != s[end]){
                    break;
                }
                start--;
                end++;
            }
            //undo last point move
            start++;
            end--;
            sub = s.substr(start, end-start+1);
            //update longest substring
            if(sub.length() > lp.length()){
                lp = sub;
            }
        }
        return lp;
    }
};
