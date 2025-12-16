class Solution:
    def decodeString(self, s: str) -> str:
        stack_nums = []
        stack_str = []
        current_num = 0
        current_str = ""
        
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                stack_nums.append(current_num)
                stack_str.append(current_str)
                current_num = 0
                current_str = ""
            elif char == ']':
                num = stack_nums.pop()
                prev_str = stack_str.pop()
                current_str = prev_str + current_str * num
            else:
                current_str += char
        
        return current_str  