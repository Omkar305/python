class Number:
    def __init__(self,data1,result=0):
        self.data1=data1
        self.result=result

    def __add__(self,data2):
        self.result=self.data1+data2
        return self.result

    def __sub__(self,data2):
        self.result=self.data1-data2
        return self.result

    def __mul__(self,data2):
        self.result=self.data1*data2
        return self.result

x=Number(10)
print('x:',x.data1)

sum1=x+3
print('sum1:',sum1)

sum2=x+10
print('sum2:',sum2)

sum3=x-15
print('sum3:',sum3)

sum4=x-5
print('sum4:',sum4)

sum5=x*2
print('sum5:',sum5)
