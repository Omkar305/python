def div(a,b):
    if b==0:
        raise Exception("can't divide by zero")
    return a/b

try:
    result=div(10,0)
    print(result)
except Exception as e:
    print(e)
