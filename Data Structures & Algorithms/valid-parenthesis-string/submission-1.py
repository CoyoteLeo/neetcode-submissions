class Solution:
    def checkValidString(self, s: str) -> bool:
        left_stack = []
        star_stack = []
        for idx, i in enumerate(s):
            if i == '(':
                left_stack.append(idx)
            elif i == '*':
                star_stack.append(idx)
            else:
                if not left_stack and not star_stack:
                    return False
                elif left_stack:
                    left_stack.pop()
                else:
                    star_stack.pop()

        while left_stack:
            if not star_stack or star_stack.pop() < left_stack.pop():
                return False

        return True