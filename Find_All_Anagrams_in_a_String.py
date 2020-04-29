# https://leetcode.com/problems/find-all-anagrams-in-a-string/
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        if len(p) > len(s):
            return result
        
        p_len = len(p)
        idx = 0
        while idx <(len(s)-p_len + 1):
            if s[idx] not in p:
                idx+=1
                continue
            s_ = list(s[idx:idx+p_len])
            p_ = list(p)
            while len(s_) > 0:
                if s_[0] in p_:
                    p_.remove(s_[0])
                    s_.remove(s_[0])
                else:
                    if s_[0] in p:
                        idx += 1
                    else:
                        idx += p_len - len(s_)
                    break
            if len(s_) == 0:
                result.append(idx)
            else:
                continue
                
            idx_tmp = idx
            while idx_tmp + p_len < len(s):
                if s[idx_tmp] == s[idx_tmp+p_len]:
                    idx_tmp += 1
                    result.append(idx_tmp)
                else:
                    break
            idx = idx_tmp + 1
        
        return result
