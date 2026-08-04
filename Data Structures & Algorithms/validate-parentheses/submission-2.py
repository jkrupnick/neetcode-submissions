class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for letter in s:
            match letter:
                case "(":
                    stack.append(letter)
                case "{":
                    stack.append(letter)
                case "[":
                    stack.append(letter)
                case ")":
                    if not stack:
                        return False
                    if stack.pop() != "(":
                        return False
                case "}":
                    if not stack:
                        return False
                    if stack.pop() != "{":
                        return False
                case "]":
                    if not stack:
                        return False
                    if stack.pop() != "[":
                        return False
        if not stack:
            return True
        else:
            return False
        