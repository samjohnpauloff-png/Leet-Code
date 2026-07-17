class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
       self.a=celsius+273.15
       self.b=celsius*1.80+32.00
       return (self.a,self.b)