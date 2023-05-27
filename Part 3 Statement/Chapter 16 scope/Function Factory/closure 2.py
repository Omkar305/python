#function factory
'''
def f1():
    a=27
    def f2():
        def f3():
            print(a)
            def f4():
                print(a)
            f4()
        f3()
    f2()
f1()
'''

'''
def f1():
    o=29
    def f2():
        def f3():
            print(o)
            def f4():
                print(o)
            f4()
        f3()
    f2()
f1()
'''

'''
def add1():
    s=19
    def add2():
        def add3():
            print(s)
            def add4():
                print(s)
                def add5():
                    print(s)
                add5()
            add4()
        add3()
    add2()
add1()
'''

def add1():
    a=15
    def add2():
        b=34
        def add3():
            x=a+b
            print(x)
            def add4():
                c=87
                def add5():
                    d=99
                    def add6():
                        y=c+d
                        print(y)
                    add6()
                add5()
            add4()
        add3()
    add2()
add1()
                            
    


































