# https://leetcode.com/problems/product-of-array-except-self/

# 간단하게 생각해볼수 있는 풀이법. list 중간에 0이 들어가면 꼬인다
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         all_product = reduce((lambda x, y: x * y), nums) 
#         result = []
        
#         for i in nums:
#             result.append(int(all_product / i))
            
#         return result

# -------------------------------------------------------------
# 0 갯수 세기    
# 사용하지 말라는 나눗셈 사용
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt = 0
        mult_nums = 1
        for num in nums:
            if num == 0:
                zero_cnt += 1
            else:
                mult_nums *= num
                
        if zero_cnt > 1:
            return [0] * len(nums)
        elif zero_cnt == 1:
            return [0 if num != 0 else mult_nums for num in nums]
        else:
            return [int(mult_nums/num) for num in nums]
        

    
# subarray 만들어서 풀기 시도
# TIME LIMIT EXCEEDED
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         left_list = []
#         right_list = nums[:]
#         result = []
#         for _ in range(len(nums)):
#             # right_list의 첫번째 값 임시 저장
#             tmp_num = right_list[0]
#             # right_list 줄이기
#             right_list = right_list[1:]
#             # 현재 값을 제외한 나머지 값만으로 리스트 구성
#             result.append(left_list+right_list)
#             # left_list로 임시 저장한값 옮기기
#             left_list.append(tmp_num)

#         return [reduce((lambda x, y: x * y), nums) for nums in result]

# -------------------------------------------------------------
# # Solution에 나와있는 답
# # left_product와 right_product를 각각 구해서 저장하는 방식
# # O(N)/O(N)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        
        L, R, answer = [0]*length, [0]*length, [0]*length
        L[0] = 1
        for i in range(1, length):
            L[i] = nums[i - 1] * L[i - 1]
            
        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            R[i] = nums[i + 1] * R[i + 1]
            
        for i in range(length):
            answer[i] = L[i] * R[i]
        
        return answer

# # Solution에 나와있는 답
# # O(N)/O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0]*length
        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]
        R = 1;
        for i in reversed(range(length)):

            answer[i] = answer[i] * R
            R *= nums[i]
        
        return answer
