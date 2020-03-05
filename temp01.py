class C:
    def f1(self,a,b):
        return a+b

class D:
    def f1(self):
        cc = C()
        b=cc.f1(1,2)
        return b
dd = D()

print(dd.f1())