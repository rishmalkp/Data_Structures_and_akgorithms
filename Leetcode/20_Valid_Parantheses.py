class Solution:
    def isValid(self, s):
        stack = []
        para = {
            '(':')',
            '[':']',
            '{':'}'
        }

        for char in s:
            if char in para.key():
                stack.append(para[char])
            elif not stack or stack[-1]!=char:
                return False
            else:
                stack.pop()
        return len(stack)==0