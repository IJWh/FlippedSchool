#https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        k_dict = {}
        tmp_list = []
        result_list = []
        
        for i in words:
            if i in k_dict:
                k_dict[i] += 1
            else:
                k_dict[i] = 1
                
        k_dict = {k: v for k, v in sorted(k_dict.items(), key=lambda item: item[1])}
        k_dict_r_keys = list(reversed(list(k_dict.keys())))
        
        tmp_list.append(k_dict_r_keys[0])

        for i in k_dict_r_keys[1:]:
            if k_dict[i] == k_dict[tmp_list[0]]:
                tmp_list.append(i)
            else:
                result_list += sorted(tmp_list)
                tmp_list = [i]
                
        result_list += sorted(tmp_list)

        return result_list[:k]
