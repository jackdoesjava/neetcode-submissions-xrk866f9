class Solution:
    def calPoints(self, operations: List[str]) -> int:
        if not operations:
            return 0

        stack = [] # storing valid scores
        for op in operations: # each operation
            if op == "+":
                stack.append(stack[-1] + stack[-2]) # last two scores (most recent)
            elif op == "D":
                stack.append(2 * stack[-1])
            elif op == "C":
                stack.pop() # remove most recent score
            else:
                stack.append(int(op))

        return sum(stack)