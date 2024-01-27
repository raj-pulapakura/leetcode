class Solution:
    def asteroidCollision(self, asteroids):
        if len(asteroids) == 1: return asteroids
        stack = [asteroids[0]]
        for i in range(1, len(asteroids)):
            asteroid = asteroids[i]
            if abs(asteroid) == abs(stack[-1]): 
                if stack[-1] > 0 and asteroid < 0:
                    stack.pop()
                else:
                    stack.append(asteroid)
            elif asteroid > 0:
                stack.append(asteroid)
            elif stack[-1] < 0 and asteroid < 0:
                stack.append(asteroid)
            else:
                while stack[-1] > 0 and abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                if len(stack) == 0:
                    stack = [asteroid]
        return stack
    
print(Solution().asteroidCollision([-2,-1,1,2]))