class Solution:
    def judgeCircle(self, moves: str) -> bool:
        sumx = 0
        sumy = 0 
        for i in moves:
            if i == "U":
                sumy += 1
            if i == "D":
                sumy -= 1
            if i == "R":
                sumx += 1
            if i == "L":
                sumx -= 1
            
        if sumx == 0 and sumy == 0:
            return True
        else:
            return False
