class Node:
    def __init__(self, value, operator="", children=[], parent=None):
        self.value = value
        self.operator = operator
        self.children = children
        self.parent = parent

    def addChild(self, childValue, childOperator):
        child = Node(childValue, childOperator, children=[], parent=self)
        self.children.append(child)

    def evaluate(self):
        for child in self.children:
            if child.operator == "+":
                self.value += child.evaluate()
            elif child.operator == "-":
                self.value -= child.evaluate()
        return self.value
    
    def print(self):
        print(f"{self.operator} {self.value}")
        for child in self.children:
            print("\t", end="")
            child.print()



class Solution:
    def removeWhitespace(self, s:str) -> str:
        return "".join([c for c in s if c != " "])

    def createCompGraph(self, s: str) -> Node:
        root = Node(value=0, operator="", children=[], parent=None)
        s = self.removeWhitespace(s)
        curr = root

        digits = [str(d) for d in range(0, 10)]
        i = 0
        operator = "+"

        while i < len(s):
            char = s[i]
            # check if digit
            if char in digits:
                # get full number
                while i < len(s) - 1 and s[i+1] in digits:
                    char = char + s[i+1]
                    i += 1
                curr.addChild(childValue=int(char), childOperator=operator)
            elif char == "+":
                operator = "+"
            elif char == "-":
                operator = "-"
            elif char == "(":
                curr.addChild(childValue=0, childOperator=operator)
                curr = curr.children[-1]     
                operator = "+"           
            elif char == ")":
                curr = curr.parent
            i += 1

        return root
    
    def calculate(self, s: str) -> int:
        compGraph = self.createCompGraph(s)
        result = compGraph.evaluate()
        return result

print(Solution().calculate("(1+1)-3"))