# https://leetcode.com/problems/reorder-data-in-log-files/

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dig_log = []
        let_log = []
        result_log = []
        
        for log in logs:
            identifier, content = log.split(" ", 1)
            if re.search('\d+', content):
                dig_log.append(log)
            else:
                let_log.append([content,identifier])
                
        let_log = sorted(let_log)
        
        for content, identifier in let_log:
            result_log.append("{} {}".format(identifier, content))
        
        result_log += dig_log
        
        return result_log
