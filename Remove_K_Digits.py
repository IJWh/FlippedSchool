# https://leetcode.com/problems/remove-k-digits/
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        # if k == 1 or len(num)/2 == k:
        if len(num) == k:
            return "0"

        result = ""
        
        num_list = list(num)
        
        for i in range(len(num_list)):
            num_list[i] = int(num_list[i])
        
        # k-1개 자릿수 제거
        for i in range(k-1):
            if num_list[1] == 0:
                num_list.pop(0)
                while len(num_list)>0 and num_list[0] == 0:
                    num_list.pop(0)
            elif num_list[0] < num_list[1]:
                num_list.pop(1)
            else:
                num_list.pop(0)
        
        # 마지막 한 자릿수 제거
        if len(num_list) <= 1:
            return "0"
        elif num_list[1] == 0:
            num_list.pop(0)
            while len(num_list)>0 and num_list[0] == 0:
                num_list.pop(0)
        elif num_list[0] < num_list[1]:
            num_list.pop(1)
        elif num_list[0] > num_list[1]:
            num_list.pop(0)
        else:
            # 첫번째 자리와 2번째 자리가 같을때
            idx = 1
            while idx < len(num_list) and num_list[0] == num_list[idx]:
                idx += 1
            if idx > len(num_list):
                num_list.pop(0)
            elif idx >= len(num_list)-2:
                num_list.pop(max(num_list))
            else:
                num_list.pop(idx)
        
        if len(num_list) == 0:
                return "0"
        
        for i in num_list:
            result += str(i)
        """
        num_list = []
        
        for n in num:
            while k>0 and num_list and num_list[-1] > n:
                num_list.pop()
                k -= 1
            num_list.append(n)
            
        result = []
        if k > 0:
            result = num_list[:-k]
        else:
            result = num_list
        
        
        return "".join(result).lstrip('0') or "0"
