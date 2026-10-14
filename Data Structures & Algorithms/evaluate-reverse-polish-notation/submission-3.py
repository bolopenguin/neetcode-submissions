class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(["+", "-", "*", "/"])

        number_stack = []
        for token in tokens:
            if token not in operators:
                number_stack.append(int(token))
            else:
                num_two = number_stack.pop(-1)
                num_one = number_stack.pop(-1)
                if token == "+":
                    result =  num_one + num_two
                elif token == "-":
                    result =  num_one - num_two
                elif token == "*":
                    result =  num_one * num_two
                elif token == "/":
                    result = int(num_one / num_two)
                number_stack.append(result)
        
        return number_stack.pop()