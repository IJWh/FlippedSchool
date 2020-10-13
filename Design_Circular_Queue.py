#https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.MCQ = [0] * k
        self.MCQ_start = 0
        self.MCQ_end = 0
        self.MCQ_len = k
        self.MCQ_cnt = 0
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        
        self.MCQ[self.MCQ_end] = value
        self.MCQ_end = (self.MCQ_end + 1) % self.MCQ_len
        self.MCQ_cnt += 1
        return True
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.MCQ_start = (self.MCQ_start + 1) % self.MCQ_len
        self.MCQ_cnt -= 1
        return True
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.MCQ[self.MCQ_start]
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.MCQ[(self.MCQ_end - 1) % self.MCQ_len ]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.MCQ_cnt == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.MCQ_cnt == self.MCQ_len
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
