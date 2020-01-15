class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int maxlen, count, maximum, asc, start, end;
        bitset<96> asciiTable;
        
        
        asciiTable.reset();
        maxlen = 0;
        maximum = 0;
        count = 0;
        start = 0;
        end = 0;
        asc = ' ';
        
        
        //check alphabet used;
        for(int i=0;i<s.length();i++){
            asciiTable.set(s[i]-asc);
        }
        maximum = asciiTable.count();
        asciiTable.reset();
        
        
        //search substring
        while(end<s.length()){
           //check repeated character
            if(asciiTable.test(s[end]-asc)){
                //find same alphabet from start;
                while(s[start] != s[end]){
                    asciiTable.reset(s[start]-asc);
                    count--;
                    start++;
                }
                count--;
                start++;
            }
            asciiTable.set(s[end]-asc);
            end++;
            count++;
            
            
            
            //update maxlen
            if(maxlen < count){
                maxlen = count;
            }
            //maximum size reached
            if(maxlen == maximum){
                break;
            }
        }
        
        return maxlen;
    }
};
