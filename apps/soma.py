import operator
class Soma:
    def __init__(self,a=None,b=None):
        self.a = a
        self.b = b

    def faz(self):
        return operator.add(self.a,self.b)
if __name__ == "__main__":
    s = Soma(2,3)
    print(s.faz())
