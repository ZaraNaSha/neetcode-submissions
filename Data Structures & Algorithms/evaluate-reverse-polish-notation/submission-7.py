class Solution:
    def __init__(self):
        self.operation = ['+','*','-','/']
    def opt(self,a:int,b:int,opt:str)->int:
        if opt=='+':
            return a+b
        elif opt=='*':
            return a*b
        elif opt=='-':
            return a-b
        else:
            return int(a/b)
    def evalRPN(self, tokens: List[str]) -> int:
        tmp = []
        for c in tokens:
            if c not in self.operation:
                tmp.append(int(c))
            else:
                if len(tmp)>=2:
                    b = (tmp.pop())
                    a = (tmp.pop())
                    tmp.append(self.opt(a,b,c))
            print(tmp)
        return tmp.pop()   