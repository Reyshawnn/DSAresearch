class My_Own_Stack: #Class for list with designated stack functionality
    def __init__(self):
        self.list = []

#Methods for stack functionality enforcing LIFO basis
    def addStack(self,item): #in next level change this to *args
        self.list.append(item)

    def popStack(self):
        self.list.pop()

    def lastStack(self):
        print(self.list[len(self.list)-1])

    def checkStack(self):
        if self.list == None:
            print("This stack is empty")
        else:
            print(f"{self.list}")

    def numStack(self):
        return len(self.list)


    def balanceStack(self):
        checkStack = {}
        
        while (self.list):
            current_symbol = self.list.pop()
            match (current_symbol):
                case "}":
                    checkStack["}"] = "{"
                case ")":
                    checkStack[")"] = "("
                case "]":
                    checkStack["]"] = "["


                case "{":
                    if "}" in checkStack:
                        continue
                    else:
                        print("invalid")
                        valid_flag = 0
                        break
                case "(":
                    if ")" in checkStack:
                        continue
                    else:
                        print("invalid")
                        valid_flag = 0
                        break
                case "[":
                    if ")" in checkStack:
                        continue
                    else:
                        print("invalid")
                        valid_flag = 0
                        break
               
        else:
            print("valid")
'''
situation 1: 
Balanced Parentheses Check
'''

balance_this = My_Own_Stack()
balance_this.addStack("{")
balance_this.addStack("[")
balance_this.addStack("(")
balance_this.addStack(")")
balance_this.addStack("}")
balance_this.addStack("]")
balance_this.balanceStack()



