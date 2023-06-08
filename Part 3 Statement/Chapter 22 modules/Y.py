def catch1(c1,c2):
    result1=c1+c2
    print('catch1:',result1)
    def catch2(d1,d2):
        result2=d1**d2
        print('catch2:',result2)
    return catch2
