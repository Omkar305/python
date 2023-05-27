#function factory


def f1(num1):
    def f2(num2):
        return num1*num2
    return f2

a=f1(4)
print(a(5))

'''
def f1(num1):
    def f2(num2):
        return num1*num2
    return f2

a=f1(10)
print(a(8))
'''
