from typing import Any


class AdvancedNumber(object):
    def __init__(self, val) -> None:
        self.value = val
    
    def __repr__(self) -> str:
        return f"AdvancedNumber({self.value})"

    def __str__(self) -> str:
        return f"Value: {self.value}"
    
    def __add__(self,other):
        if isinstance(other, int) or isinstance(other, float):
            return AdvancedNumber(self.value + other)
        elif isinstance(other,AdvancedNumber):
            return AdvancedNumber(self.value + other.value)
        else:
            return NotImplemented
    
    def __sub__(self,other):
        if isinstance(other, int) or isinstance(other, float):
            return AdvancedNumber(self.value - other)
        elif isinstance(other,AdvancedNumber):
            return AdvancedNumber(self.value - other.value)
        else:
            return NotImplemented
    
    def __mul__(self,other):
        if isinstance(other, int) or isinstance(other, float):
            return AdvancedNumber(self.value * other)
        elif isinstance(other,AdvancedNumber):
            return AdvancedNumber(self.value * other.value)
        else:
            return NotImplemented
    
    def __truediv__(self,other):
        if isinstance(other, int) or isinstance(other, float):
            return AdvancedNumber(self.value / other)
        elif isinstance(other,AdvancedNumber):
            print("hey")
            return AdvancedNumber(self.value / other.value)
        else:
            return NotImplemented
    
    def __mod__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return AdvancedNumber(self.value % other)
        elif isinstance(other,AdvancedNumber):
            return AdvancedNumber(self.value % other.value)
        else:
            
            return NotImplemented
        
    def __lt__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.value < other
        elif isinstance(other,AdvancedNumber):
            return self.value < other.value
        else:
            return NotImplemented
    
    def __le__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.value <= other
        elif isinstance(other,AdvancedNumber):
            return self.value <= other.value
        else:
            return NotImplemented
        
    def __gt__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.value > other
        elif isinstance(other,AdvancedNumber):
            return self.value > other.value
        else:
            return NotImplemented
    
    def __ge__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.value >= other
        elif isinstance(other,AdvancedNumber):
            return self.value >= other.value
        else:
            return NotImplemented
        
    def __ne__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.value != other
        elif isinstance(other,AdvancedNumber):
            return self.value != other.value
        else:
            return NotImplemented
    
    def __hash__(self) -> int:
        return hash(self.value)
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, int) or isinstance(other, float):
            return self.value == other
        elif isinstance(other,AdvancedNumber):
            return self.value == other.value
        else:
            return NotImplemented    
    
    def __bool__(self):
        return self.value != 0
    
    def __call__(self) :
        return self.value**2
    
    def __format__(self, format_spec: str) -> str:
        return format(self.value, format_spec)
        
    def __del__(self):
        print(f"AdvancedNumber with value {self.value} is being destroyed")
        
                


# if __name__=='__main__':
#     obj = AdvancedNumber(5)
#     obj1 = AdvancedNumber(10)
#     print((obj1 / obj).value)
