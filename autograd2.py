class Value:
    def __init__(self,data):
        self.data=data
        self.grad=0
        self._backward=lambda:None
        self._prev=set()
        self._op=''

a = Value(2.0)
b = Value(3.0)

c =a.data*b.data