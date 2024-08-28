class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n=len(goal)
        for i in range(n):
            if(s==goal):
                return True
            goal = goal[-1]+goal[:-1]
        return False
