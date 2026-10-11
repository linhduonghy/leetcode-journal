class Solution:

    def parseBoolExpr(self, expression: str) -> bool:

        stack = []
        for c in expression:
            if c == ',':
                continue
            elif c == ')':
                seen = set()
                while stack[-1] != '(':
                    seen.add(stack.pop())
                stack.pop()
                op = stack.pop()
                if op == '!':
                    stack.append('f' if 't' in seen else 't')
                elif op == '&':
                    stack.append('f' if 'f' in seen else 't')
                elif op == '|':
                    stack.append('t' if 't' in seen else 'f')
            else: stack.append(c)

        return stack[-1] == 't'




