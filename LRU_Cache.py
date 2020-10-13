# https://leetcode.com/problems/lru-cache/

class LRUCache:

    def __init__(self, capacity: int):
        self.LRUC = {}
        self.capacity = capacity
        self.key_cnt = 0
        self.call_num = 0

    def get(self, key: int) -> int:
        self.call_num += 1
        if key not in self.LRUC:
            return -1
        self.LRUC[key][1] = self.call_num
        return self.LRUC[key][0]
        
        # return (self.LRUC).get(key,[-1,0])[0]

    def put(self, key: int, value: int) -> None:
        self.call_num += 1
        if key in self.LRUC:
            self.LRUC[key] = [value,self.call_num]
            return None
        if self.capacity == self.key_cnt:
            last_call_num = 40000
            last_call_key = 0
            for cur_key in self.LRUC:
                if last_call_num > self.LRUC[cur_key][1]:
                    last_call_num = self.LRUC[cur_key][1]
                    last_call_key = cur_key
            del self.LRUC[last_call_key]
            self.key_cnt -= 1
        self.LRUC[key] = [value,self.call_num]
        self.key_cnt += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
