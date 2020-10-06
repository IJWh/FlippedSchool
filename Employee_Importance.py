# https://leetcode.com/problems/employee-importance/
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        val = 0
        
        def add_total(emp: Employee):
            cur_val = emp.importance
            for sub in emp.subordinates:
                for sub_emp in employees:
                    if sub_emp.id == sub:
                        cur_val += add_total(sub_emp)
            return cur_val
                
        for e in employees:
            if e.id == id:
                val = add_total(e)
                break
                
        return val
            
