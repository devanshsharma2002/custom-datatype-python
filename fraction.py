from math import gcd

class fractions:
    def __init__(self,nmrtr,dmrtr):
        self.nmrtr=nmrtr
        self.dmrtr=dmrtr
        
        if dmrtr == 0:
          raise ValueError("denominator cannot be zero")

    def __str__(self):
        return f"{self.nmrtr}/{self.dmrtr}"
    def __repr__(self):
      a, b = self.simplify(self.nmrtr, self.dmrtr)
      return f"fractions({a}, {b})"

    
   #ARITHMETIC 
    def __add__(self,other):
        other = self._to_fraction(other)
        result_nmrtr=((self.nmrtr*other.dmrtr)+(self.dmrtr*other.nmrtr))
        result_dmrtr=self.dmrtr*other.dmrtr
       # return f"{result_nmrtr}/{result_dmrtr}"
        a,b=self.simplify(result_nmrtr,result_dmrtr)
        return f"{a}/{b}"
    def __sub__(self,other):
        other = self._to_fraction(other)
        result_nmrtr=((self.nmrtr*other.dmrtr)-(self.dmrtr*other.nmrtr))
        result_dmrtr=self.dmrtr*other.dmrtr
       # return f"{result_nmrtr}/{result_dmrtr}"
        a,b=self.simplify(result_nmrtr,result_dmrtr)
        return f"{a}/{b}"
    def __mul__(self,other):
        other = self._to_fraction(other)
        result_nmrtr=self.nmrtr*other.nmrtr
        result_dmrtr=self.dmrtr*other.dmrtr
       # return f"{result_nmrtr}/{result_dmrtr}"
        a,b=self.simplify(result_nmrtr,result_dmrtr)
        return f"{a}/{b}"
    def __truediv__(self,other):
        other = self._to_fraction(other)
        result_nmrtr=self.nmrtr*other.dmrtr
        result_dmrtr=self.dmrtr*other.nmrtr
       # return f"{result_nmrtr}/{result_dmrtr}"
        a,b=self.simplify(result_nmrtr,result_dmrtr)
        return f"{a}/{b}"
    
    def __radd__(self, other):
        # Handles other + self when other is int or compatible type
        return self.__add__(other)
    def __rsub__(self, other):
        # Handles other - self
        other = self._to_fraction(other)
        # Subtract self from other
        return other.__sub__(self)
    def __rmul__(self, other):
        # Handles other * self
        return self.__mul__(other)
    def __rtruediv__(self, other):
      # Handles other / self
      other = self._to_fraction(other)
      return other.__truediv__(self)

    
    #COMPARISION
    def __eq__(self,other):
       other = self._to_fraction(other)
       sn,sd=self.simplify(self.nmrtr,self.dmrtr)
       on,od=self.simplify(other.nmrtr,other.dmrtr)

       if sn==on and sd==od:
          return True
       else:
          return False
    def __ne__(self,other):
       other = self._to_fraction(other)
       sn,sd=self.simplify(self.nmrtr,self.dmrtr)
       on,od=self.simplify(other.nmrtr,other.dmrtr)

       if sn==on and sd==od:
          return False
       else:
          return True
       
    def __lt__(self,other):
       other = self._to_fraction(other)
       sn,sd=self.simplify(self.nmrtr,self.dmrtr)
       on,od=self.simplify(other.nmrtr,other.dmrtr)
       if self.frac_to_float()<other.frac_to_float():
          return True
       else:
          return False
    def __le__(self,other):
       other = self._to_fraction(other)
       
       sn,sd=self.simplify(self.nmrtr,self.dmrtr)
       on,od=self.simplify(other.nmrtr,other.dmrtr)
       if (self.frac_to_float()<=other.frac_to_float()):
          return True
       else:
          return False
    def __gt__(self,other):
       other = self._to_fraction(other)
       
       sn,sd=self.simplify(self.nmrtr,self.dmrtr)
       on,od=self.simplify(other.nmrtr,other.dmrtr)
       if (self.frac_to_float()>other.frac_to_float()):
          return True
       else:
          return False
    def __ge__(self,other):
       other = self._to_fraction(other)
       
       sn,sd=self.simplify(self.nmrtr,self.dmrtr)
       on,od=self.simplify(other.nmrtr,other.dmrtr)
       if (self.frac_to_float()>=other.frac_to_float()):
          return True
       else:
          return False
       
    #MISCELLENOUS
    def __neg__(self):
       sn,sd=self.nmrtr,self.dmrtr
       if sn>0:
          if sd>0:
             return -sn,sd
          elif sd<0:
             return sn,-sd
       if sn<0: 
          if sd>0:
             return -sn,sd
          elif sd<0:  
             return -sn,-sd
       if sn==0:
          if sd==0:
            print('division by 0 error')
            return 0
          else :
             return sn,sd
    
    def __abs__(self):
       sn,sd=self.nmrtr,self.dmrtr
       if sn>0:
          if sd>0:
             return sn,sd
          elif sd<0:
             return sn,-sd
       if sn<0: 
          if sd>0:
             return -sn,sd
          elif sd<0:  
             return -sn,-sd
       if sn==0:
          if sd==0:
            print('division by 0 error')
            return 0
          else :
             return sn,sd
    def __float__(self):
      return self.frac_to_float()
    
    #METHODS
    def _to_fraction(self, value):
      if isinstance(value, fractions):
        return value
      elif isinstance(value, int):
        return fractions(value, 1)
      elif isinstance(value, float):
        # Optional: convert float to fraction approx. or raise error
        raise TypeError("Float input not supported yet")
      else:
        raise TypeError(f"Unsupported type {type(value)}")

    
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
    
    def float_to_frac(self, f):
      """
      Converts a float to a fraction using continued fraction approximation 
      or by converting decimal places to numerator/denominator.
      """
      if not isinstance(f, float):
        raise TypeError("Input must be a float")

      # Convert float to string to count decimal places
      s = str(f)
      if '.' in s:
        decimal_places = len(s.split('.')[1])
        denom = 10 ** decimal_places
        numer = int(round(f * denom))
      else:
        # No decimal part
        numer = int(f)
        denom = 1

      a, b = self.simplify(numer, denom)
      return fractions(a, b)

    def frac_to_float(self):
       if self.dmrtr!=0:
          return round(self.nmrtr/self.dmrtr,3)
       else:
          print('division by 0')
          return 0
    def reciprocal(self):
       if self.dmrtr==0:
          raise ValueError("Numerator cannot be zero")
       else:
          return self.dmrtr,self.nmrtr
    def mixed_fraction(self):
      a, b = self.simplify(self.nmrtr, self.dmrtr)
      whole = a // b
      remainder = abs(a) % b
      if remainder == 0:
        return f"{whole}"
      else:
        return f"{whole} {remainder}/{b}"
      
    @staticmethod
    def str_to_frac(s):
      parts = s.split('/')
      if len(parts) == 1:
        numerator = int(parts[0])
        denominator = 1
      elif len(parts) == 2:
        numerator = int(parts[0])
        denominator = int(parts[1])
      else:
        raise ValueError("Invalid fraction string format")
      return fractions(numerator, denominator)



obj = fractions(4, 4)
print(type(obj))         # <class 'fractions'> (your class name)
print(obj)               # 1/1    (should be simplified)

obj2 = fractions(4, 5)
print(type(obj2))        # <class 'fractions'>
print(obj2)              # 4/5

print(obj + obj2)        # 9/5
print(obj - obj2)        # 1/5
print(obj * obj2)        # 4/5
print(obj / obj2)        # 5/4

# Comparisons
print('\ncomparision')
print(obj == obj2)       # False
print(obj != obj2)       # True
print(obj <= obj2)       # False
print(obj >= obj2)       # True
print(obj < obj2)        # False
print(obj > obj2)        # True

# Negation
neg = fractions(3, 5)
print('negetion')
print(-neg)              # -3/5

# Absolute value
print(abs(neg))          # 3/5

# Float conversion
print(float(neg))        # 0.6

# Reciprocal
print(neg.reciprocal())  # 5/3

# Test with integer operations
int_test = fractions(5, 2)
print(int_test + 1)      # 7/2
print(1 + int_test)      # 7/2
print(int_test - 1)      # 3/2
print(1 - int_test)      # -3/2
print(int_test * 2)      # 5/1
print(2 * int_test)      # 5/1
print(int_test / 2)      # 5/4
print(2 / int_test)      # 4/5

# Additional comparison with integer and float
# print(int_test == 2.5)   # True
# print(int_test < 3)      # True
# print(int_test > 1.5)    # True
# print(int_test == fractions(10, 4)) # True

# Zero value and error handling
zero = fractions(0, 5)
print(zero)              # 0/1
# reciprocal test should probably raise or handle divide-by-zero:
# print(zero.reciprocal()) # Error or handled logic

# Large values
large = fractions(100000, 25000)
print(large)             # 4/1  (simplified)

# Negative denominator
neg_den = fractions(4, -5)
print(neg_den)           # -4/5

# String conversion
print(str(obj2))         # 4/5
print(repr(obj2))        # fractions(4, 5)

a=fractions.str_to_frac('4/5')
print(a)