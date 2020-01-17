class Solution {
public:
    string minWindow(string s, string t) {
        string result = "";
        string sub = "";
        unordered_set<string> window;
        unordered_map<char ,int> charCount;
        int count, start, end, minlength;
        
        count = 0;
        minlength = s.length();
        start = 0;
        
        //check character used in t
        for(int i=0;i<t.length();i++){
            if(charCount.find(t[i])!= charCount.end() ){
                charCount.find(t[i])->second++;
                
            }
            else{
                charCount.insert(make_pair(t[i],1));
            }
            count++;
        }
        
        //find substrings
            //find start point
        while(start< s.length()){
            if(charCount.find(s[start]) != charCount.end()){
                break;
            }
            start++;
        }
        
        end = start;
        while(start < s.length() && end < s.length()){
            //if s[end] is in string t
            if(charCount.find(s[end]) != charCount.end()){
                charCount.find(s[end])->second--;
                //decrease count only when new character is in t string and not in substring now
                if(charCount.find(s[end])->second >=0){
                    count--;
                }
            }
            //count == 0 > substring made
            //while(count ==0) > if count is 0 after moving start point, shorter substring exist
            while(count == 0){
                window.insert(s.substr(start,end-start+1));
                charCount.find(s[start])->second++;


                //count increase when necessary character is out
                if(charCount.find(s[start])->second > 0){
                    count++;
                }
                start++;
                //move start point to back
                while(start<s.length()){
                    if(charCount.find(s[start]) != charCount.end()){
                        //overused character, don't need it
                        if(charCount.find(s[start])->second <0){
                            charCount.find(s[start])->second++;
                        }
                        //reach to next start point
                        else{
                            break;
                        }
                    }
                    start++;
                }
            }
            end++;
        }
        
        
        
        //search shortest string
        for( auto iter = window.begin();iter!=window.end();iter++){
            sub = *iter;
            if(sub.length() <= minlength){
                result = sub;
                minlength = sub.length();
            }
        }
        
        return result;
    }
};
