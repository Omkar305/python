def get1(a1,a2):
    result1=a1/a2
    print('get1:',result1)
    def get2(b1,b2):
        result2=b1//b2
        print('get2:',result2)
    return get2
