# https://leetcode.com/problems/robot-bounded-in-circle/
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # 마지막 위치 = 첫 위치
        # 마지막 방향 != 첫 방향
        direction = 0
        position =[0,0]
        
        for inst in instructions:
            if inst == "L":
                direction = (direction + 90) % 360
            elif inst == "R":
                direction = (direction - 90) % 360
            else:
                if direction == 0:
                    position[1] += 1
                elif direction == 90:
                    position[0] += 1
                elif direction == 180:
                    position[1] -= 1
                else:
                    position[0] -= 1
        
        return position == [0,0] or direction != 0
