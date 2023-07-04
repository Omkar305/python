class Adder:
    def __init__(self,data1):
        self.data1=data1

    def __add__(self,data2):
        return self.data1+data2

    def __radd__(self,data2):
        return data2+self.data1

    def __sub__(self,data2):
        return self.data1-data2

    def __rsub__(self,data2):
        return data2-self.data1

    def __mul__(self,data2):
        return self.data1*data2

    def __rmul__(self,data2):
        return data2*self.data1

x=Adder(5)
print(x.data1)

sum1=x+1
print('sum1:',sum1)

sum2=19+x
print('sum2:',sum2)

sum3=x+6+2+x-2-x*2
print('sum3:',sum3)













