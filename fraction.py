from math import gcd

class fractions:
    def __init__(self,nmrtr,dmrtr):
        print('hello python')
        self.nmrtr=nmrtr
        self.dmrtr=dmrtr

    def __str__(self):
        return f"{self.nmrtr}/{self.dmrtr}"
    
    def __add__(self,other):
        result_nmrtr=((self.nmrtr*other.dmrtr)+(self.dmrtr*other.nmrtr))
        result_dmrtr=self.dmrtr*other.dmrtr
       # return f"{result_nmrtr}/{result_dmrtr}"
        a,b=self.simplify(result_nmrtr,result_dmrtr)
        return f"{a}/{b}"
    def __sub__(self,other):
        result_nmrtr=((self.nmrtr*other.dmrtr)-(self.dmrtr*other.nmrtr))
        result_dmrtr=self.dmrtr*other.dmrtr
       # return f"{result_nmrtr}/{result_dmrtr}"
        a,b=self.simplify(result_nmrtr,result_dmrtr)
        return f"{a}/{b}"
    def __mul__(self,other):
        result_nmrtr=self.nmrtr*other.nmrtr
        result_dmrtr=self.dmrtr*other.dmrtr
       # return f"{result_nmrtr}/{result_dmrtr}"
        a,b=self.simplify(result_nmrtr,result_dmrtr)
        return f"{a}/{b}"
    def __truediv__(self,other):
        result_nmrtr=self.nmrtr*other.dmrtr
        result_dmrtr=self.dmrtr*other.nmrtr
       # return f"{result_nmrtr}/{result_dmrtr}"
        a,b=self.simplify(result_nmrtr,result_dmrtr)
        return f"{a}/{b}"
    

    def simplify(self,numer, denom):
      if denom == 0:
        raise ValueError("denominator cannot be zero")
      if numer == 0:
        return 0, 1
      g = gcd(numer, denom)
      a, b = numer // g, denom // g
      if b < 0:   # keep sign on numerator
        a, b = -a, -b
      return a, b
    def float_to_frac(self):
       pass
    def frac_to_float(self):
       pass

# examples


    



obj=fractions(4,5)
print(type(obj))
print(obj)

obj2=fractions(4,5)
print(obj+obj2)
print(obj-obj2)
print(obj*obj2)
print(obj/obj2)


