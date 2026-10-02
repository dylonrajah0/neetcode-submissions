class Solution:
    def isValid(self, s: str) -> bool:

        openSet = set()
        closedSet = set()

        openSet.add('(')
        openSet.add('{')
        openSet.add('[')

        closedSet.add(')')
        closedSet.add('}')
        closedSet.add(']')

        matching = {
                    ')': '(',
                    '}': '{',
                    ']': '['
                }

        stack = []

        for char in s:

            if char in openSet:
                stack.append(char)

            elif char in closedSet:
                #stack is empty
                if not stack:
                    return False
            
                if stack[-1] != matching[char]:
                    return False

                stack.pop()

        return not stack