class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stored_numbers = []
        for i in tokens:
            if i == "+":
                stored_numbers.append(stored_numbers.pop() + stored_numbers.pop())
            elif i == "-":
                a = stored_numbers.pop()
                b = stored_numbers.pop()
                stored_number.append(b - a)
            elif i == "*":
                stored_numbers.append(stored_numbers.pop() * stored_numbers.pop())
            elif i == "/":
                a = stored_numbers.pop()
                b = stored_numbers.pop()
                stored_numbers.append(int(b / a))
            else:
                stored_numbers.append(int(i))
        return stored_numbers[0]
            

        