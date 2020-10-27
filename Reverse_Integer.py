# https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        pos_limit= str(0x7fffffff)
        neg_limit= str(0x80000000)
        list_x = list(str(x))
        
        start, end = 1 if x < 0 else 0, len(list_x)-1
        
        while start < end:
            tmp = list_x[start]
            list_x[start] = list_x[end]
            list_x[end] = tmp
            
            start, end = start+1, end-1
        
        str_x = ""
        
        start = 0
        if list_x[start] == "-":
            str_x += "-"
            start += 1
        
        for i in range(start,len(list_x)):
            str_x += list_x[i]
            
        if x >= 0:
            zero_cnt = "0" * (len(pos_limit)-len(str_x)) 
        else:
            zero_cnt = "0" * (len(pos_limit)-len(str_x)+1) 
        
        tmp_str = zero_cnt +str_x
        
        if (x >= 0 and tmp_str < pos_limit) or (x < 0 and tmp_str[1:] < neg_limit):
            return int(str_x)
        else:
            return 0
        
